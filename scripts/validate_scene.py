#!/usr/bin/env python3
"""Deterministically validate one or more native Excalidraw scene files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


HEX_COLOR_RE = re.compile(r"^#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")


def _is_hex_color(value: Any) -> bool:
    return isinstance(value, str) and bool(HEX_COLOR_RE.fullmatch(value))


def _collect_color_errors(value: Any, path: str, errors: list[str]) -> None:
    """Check Excalidraw color fields while allowing transparent fills."""
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            key_lower = key.lower()
            if key_lower.endswith("color"):
                if child == "transparent" and key_lower.endswith("backgroundcolor"):
                    continue
                if not _is_hex_color(child):
                    errors.append(
                        f"{child_path} must be a hex color (or 'transparent' for backgroundColor); got {child!r}"
                    )
            _collect_color_errors(child, child_path, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _collect_color_errors(child, f"{path}[{index}]", errors)


def _validate_scene(data: Any) -> list[str]:
    errors: list[str] = []

    if not isinstance(data, dict):
        return ["top level must be a JSON object"]

    if data.get("type") != "excalidraw":
        errors.append("type must be 'excalidraw'")

    elements = data.get("elements")
    if not isinstance(elements, list):
        errors.append("elements must be a list")
        elements = []
    elif not elements:
        errors.append("elements must not be empty")

    ids: set[str] = set()
    for index, element in enumerate(elements):
        location = f"elements[{index}]"
        if not isinstance(element, dict):
            errors.append(f"{location} must be an object")
            continue
        element_id = element.get("id")
        if not isinstance(element_id, str) or not element_id:
            errors.append(f"{location}.id must be a non-empty string")
        elif element_id in ids:
            errors.append(f"{location}.id duplicates element id {element_id!r}")
        else:
            ids.add(element_id)

        if element.get("type") == "text":
            text = element.get("text")
            if not isinstance(text, str) or not text.strip():
                errors.append(f"{location}.text must be non-empty for text elements")

    _collect_color_errors(data.get("appState", {}), "appState", errors)
    for index, element in enumerate(elements):
        _collect_color_errors(element, f"elements[{index}]", errors)

    for index, element in enumerate(elements):
        if not isinstance(element, dict):
            continue
        location = f"elements[{index}]"
        bound_elements = element.get("boundElements")
        if bound_elements is not None:
            if not isinstance(bound_elements, list):
                errors.append(f"{location}.boundElements must be a list or null")
            else:
                for binding_index, binding in enumerate(bound_elements):
                    binding_path = f"{location}.boundElements[{binding_index}]"
                    if not isinstance(binding, dict):
                        errors.append(f"{binding_path} must be an object")
                        continue
                    referenced_id = binding.get("id")
                    if referenced_id not in ids:
                        errors.append(
                            f"{binding_path}.id references missing element {referenced_id!r}"
                        )

        for binding_name in ("startBinding", "endBinding"):
            binding = element.get(binding_name)
            if binding is None:
                continue
            binding_path = f"{location}.{binding_name}"
            if not isinstance(binding, dict):
                errors.append(f"{binding_path} must be an object or null")
                continue
            referenced_id = binding.get("elementId")
            if referenced_id not in ids:
                errors.append(
                    f"{binding_path}.elementId references missing element {referenced_id!r}"
                )

        container_id = element.get("containerId")
        if container_id is not None and container_id not in ids:
            errors.append(
                f"{location}.containerId references missing element {container_id!r}"
            )

    return errors


def _scene_paths(arguments: list[str]) -> list[Path]:
    paths: list[Path] = []
    for argument in arguments:
        path = Path(argument)
        if path.is_dir():
            paths.extend(sorted(path.glob("*.excalidraw"), key=lambda item: str(item)))
        else:
            paths.append(path)
    return paths


def validate_file(path: Path) -> list[str]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        return ["file not found"]
    except OSError as exc:
        return [f"could not read file: {exc}"]
    except UnicodeDecodeError as exc:
        return [f"file is not valid UTF-8: {exc}"]
    except json.JSONDecodeError as exc:
        return [f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"]

    return _validate_scene(data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate native Excalidraw scene JSON without network access."
    )
    parser.add_argument(
        "scenes",
        nargs="+",
        help="one or more .excalidraw files, or directories containing them",
    )
    args = parser.parse_args(argv)

    paths = _scene_paths(args.scenes)
    if not paths:
        print("error: no .excalidraw scenes found", file=sys.stderr)
        return 1

    failed = 0
    for path in paths:
        errors = validate_file(path)
        if errors:
            failed += 1
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}")

    print(f"Validated {len(paths)} scene(s): {len(paths) - failed} passed, {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
