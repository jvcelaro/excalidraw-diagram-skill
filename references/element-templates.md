# Element Templates — ByteByteGo-inspired profile

Copy-paste JSON templates for each Excalidraw element type. The templates below are optimized for the default ByteByteGo-inspired educational style defined in `bytebygo-style.md`. Always use the exact colors from `color-palette.md`; do not invent colors inside a diagram.

## Shared defaults

Use these values on every element unless a template explicitly overrides them:

```json
{
  "fontFamily": 3,
  "roughness": 0,
  "opacity": 100,
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "fillStyle": "solid",
  "angle": 0,
  "isDeleted": false,
  "groupIds": [],
  "locked": false
}
```

Visual rules:

- Use `#202124` for ink and primary text.
- Use light semantic fills with dark semantic strokes from `color-palette.md`.
- Use rounded rectangles (`roundness.type: 3`) for panels and process blocks.
- Use `strokeStyle: "dashed"` for section boundaries.
- Use `strokeStyle: "dotted"` for the main explainer flow when the renderer supports it; use `"dashed"` as the safe fallback.
- Use no container for titles, annotations, and supporting labels.
- Keep text in a shape's `containerId`; keep the shape's `boundElements` paired with that text ID when bindings are used.
- Give every element a descriptive ID and a unique numeric `seed`.

## ByteByteGo page header

Use this group at the top of an explainer diagram. The accent bar, title, optional pill, subtitle, and divider should be separate elements so they can be moved independently.

```json
[
  {
    "type": "rectangle", "id": "header_accent",
    "x": 50, "y": 30, "width": 14, "height": 70,
    "strokeColor": "#35cdb0", "backgroundColor": "#35cdb0",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 100001,
    "version": 1, "versionNonce": 100001, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "header_title",
    "x": 92, "y": 28, "width": 600, "height": 62,
    "text": "Diagram title", "originalText": "Diagram title",
    "fontSize": 50, "fontFamily": 3, "textAlign": "left", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 100002,
    "version": 1, "versionNonce": 100002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  },
  {
    "type": "rectangle", "id": "header_pill",
    "x": 720, "y": 38, "width": 300, "height": 50,
    "strokeColor": "#27aac7", "backgroundColor": "#bdeefa",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 100003,
    "version": 1, "versionNonce": 100003, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "header_pill_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "header_pill_text",
    "x": 745, "y": 49, "width": 250, "height": 28,
    "text": "short context", "originalText": "short context",
    "fontSize": 24, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 100004,
    "version": 1, "versionNonce": 100004, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "header_pill", "lineHeight": 1.25
  },
  {
    "type": "text", "id": "header_subtitle",
    "x": 94, "y": 94, "width": 1220, "height": 28,
    "text": "One-sentence takeaway.", "originalText": "One-sentence takeaway.",
    "fontSize": 18, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
    "strokeColor": "#374151", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 100005,
    "version": 1, "versionNonce": 100005, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  },
  {
    "type": "line", "id": "header_divider",
    "x": 50, "y": 130, "width": 1670, "height": 0,
    "strokeColor": "#d1d5db", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 100006,
    "version": 1, "versionNonce": 100006, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "points": [[0, 0], [1670, 0]]
  }
]
```

Use when: the diagram needs a compact editorial frame that establishes title, context, takeaway, and reading boundary before the main scene.

## Section panel

Use section panels to create visual rooms such as `Sources`, `Ingestion`, `Transformation`, or `Serving`. Do not use a panel for every individual label.

```json
{
  "type": "rectangle", "id": "section_panel",
  "x": 60, "y": 180, "width": 420, "height": 360,
  "strokeColor": "#27aac7", "backgroundColor": "#bdeefa",
  "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "dashed",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 110001,
  "version": 1, "versionNonce": 110001, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null,
  "locked": false, "roundness": {"type": 3}
}
```

Use a free-floating section title, not a second box:

```json
{
  "type": "text", "id": "section_title",
  "x": 88, "y": 205, "width": 340, "height": 40,
  "text": "1 · section name", "originalText": "1 · section name",
  "fontSize": 30, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
  "strokeColor": "#202124", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 110002,
  "version": 1, "versionNonce": 110002, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null, "locked": false,
  "containerId": null, "lineHeight": 1.25
}
```

## Free-Floating Text (no container)
```json
{
  "type": "text",
  "id": "label1",
  "x": 100, "y": 100,
  "width": 200, "height": 25,
  "text": "Section Title",
  "originalText": "Section Title",
  "fontSize": 20,
  "fontFamily": 3,
  "textAlign": "left",
  "verticalAlign": "top",
  "strokeColor": "<title color from palette>",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "angle": 0,
  "seed": 11111,
  "version": 1,
  "versionNonce": 22222,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "containerId": null,
  "lineHeight": 1.25
}
```

## Line (structural, not arrow)
```json
{
  "type": "line",
  "id": "line1",
  "x": 100, "y": 100,
  "width": 0, "height": 200,
  "strokeColor": "<structural line color from palette>",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "angle": 0,
  "seed": 44444,
  "version": 1,
  "versionNonce": 55555,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "points": [[0, 0], [0, 200]]
}
```

## Small Marker Dot
```json
{
  "type": "ellipse",
  "id": "dot1",
  "x": 94, "y": 94,
  "width": 12, "height": 12,
  "strokeColor": "<marker dot color from palette>",
  "backgroundColor": "<marker dot color from palette>",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "angle": 0,
  "seed": 66666,
  "version": 1,
  "versionNonce": 77777,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false
}
```

## Rectangle
```json
{
  "type": "rectangle",
  "id": "elem1",
  "x": 100, "y": 100, "width": 180, "height": 90,
  "strokeColor": "<stroke from palette based on semantic purpose>",
  "backgroundColor": "<fill from palette based on semantic purpose>",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "angle": 0,
  "seed": 12345,
  "version": 1,
  "versionNonce": 67890,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": [{"id": "text1", "type": "text"}],
  "link": null,
  "locked": false,
  "roundness": {"type": 3}
}
```

## Text (centered in shape)
```json
{
  "type": "text",
  "id": "text1",
  "x": 130, "y": 132,
  "width": 120, "height": 25,
  "text": "Process",
  "originalText": "Process",
  "fontSize": 16,
  "fontFamily": 3,
  "textAlign": "center",
  "verticalAlign": "middle",
  "strokeColor": "<text color — match parent shape's stroke or use 'on light/dark fills' from palette>",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "angle": 0,
  "seed": 11111,
  "version": 1,
  "versionNonce": 22222,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "containerId": "elem1",
  "lineHeight": 1.25
}
```

## Arrow
```json
{
  "type": "arrow",
  "id": "arrow1",
  "x": 282, "y": 145, "width": 118, "height": 0,
  "strokeColor": "<arrow color — typically matches source element's stroke from palette>",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "angle": 0,
  "seed": 33333,
  "version": 1,
  "versionNonce": 44444,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "points": [[0, 0], [118, 0]],
  "startBinding": {"elementId": "elem1", "focus": 0, "gap": 2},
  "endBinding": {"elementId": "elem2", "focus": 0, "gap": 2},
  "startArrowhead": null,
  "endArrowhead": "arrow"
}
```

For curves: use 3+ points in `points` array.

## Process module

Use this for a concrete service or action inside a section. Keep the label to one or two lines and put the explanation outside the shape when it is longer.

```json
[
  {
    "type": "rectangle", "id": "process_module",
    "x": 100, "y": 280, "width": 240, "height": 86,
    "strokeColor": "#202124", "backgroundColor": "#2E2E2E",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 120001,
    "version": 1, "versionNonce": 120001, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "process_module_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "process_module_text",
    "x": 118, "y": 300, "width": 204, "height": 46,
    "text": "Azure Data Factory\nCopy Activity", "originalText": "Azure Data Factory\nCopy Activity",
    "fontSize": 21, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 120002,
    "version": 1, "versionNonce": 120002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "process_module", "lineHeight": 1.25
  }
]
```

## Data layer block

Use the semantic fill to distinguish raw, curated, and serving data. The text is intentionally concise; show paths or formats in a separate evidence card.

```json
{
  "type": "rectangle", "id": "data_layer",
  "x": 100, "y": 280, "width": 260, "height": 100,
  "strokeColor": "#19a873", "backgroundColor": "#b8f0d8",
  "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 121001,
  "version": 1, "versionNonce": 121001, "isDeleted": false,
  "groupIds": [], "boundElements": [{"id": "data_layer_text", "type": "text"}],
  "link": null, "locked": false, "roundness": {"type": 3}
}
```

```json
{
  "type": "text", "id": "data_layer_text",
  "x": 120, "y": 305, "width": 220, "height": 52,
  "text": "SILVER / CURATED\nclean · deduplicated",
  "originalText": "SILVER / CURATED\nclean · deduplicated",
  "fontSize": 20, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
  "strokeColor": "#202124", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 121002,
  "version": 1, "versionNonce": 121002, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null, "locked": false,
  "containerId": "data_layer", "lineHeight": 1.25
}
```

Use `#ffd98a`/`#c78900` for `BRONZE / RAW`, `#b8f0d8`/`#19a873` for `SILVER / CURATED`, and `#c4c7ff`/`#3f55c9` for `GOLD / SERVING`.

## Main flow arrow

Use dark ink for the primary reading path. Prefer dotted lines for the explainer look; if the renderer or target Excalidraw version does not display dotted lines consistently, use dashed lines.

```json
{
  "type": "arrow", "id": "main_flow_arrow",
  "x": 360, "y": 323, "width": 120, "height": 0,
  "strokeColor": "#202124", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "dotted",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 122001,
  "version": 1, "versionNonce": 122001, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null, "locked": false,
  "points": [[0, 0], [120, 0]],
  "startBinding": {"elementId": "source_module", "focus": 0, "gap": 8},
  "endBinding": {"elementId": "target_module", "focus": 0, "gap": 8},
  "startArrowhead": null, "endArrowhead": "arrow"
}
```

## Feedback arrow

Use this only for reprocessing, monitoring feedback, quality gates, or user signals. The label should state what travels back.

```json
{
  "type": "arrow", "id": "feedback_arrow",
  "x": 980, "y": 620, "width": -420, "height": 0,
  "strokeColor": "#2f6edb", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "dashed",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 122002,
  "version": 1, "versionNonce": 122002, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null, "locked": false,
  "points": [[0, 0], [-180, 0], [-420, -160]],
  "startBinding": null, "endBinding": null,
  "startArrowhead": null, "endArrowhead": "arrow"
}
```

## Comparison or cross-reference arrow

Use the accent pink only when two branches are being compared or when a cross-reference is important but is not part of the main flow.

```json
{
  "type": "arrow", "id": "comparison_arrow",
  "x": 520, "y": 420, "width": 180, "height": -80,
  "strokeColor": "#a33bd1", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "dashed",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 122003,
  "version": 1, "versionNonce": 122003, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null, "locked": false,
  "points": [[0, 0], [90, 0], [180, -80]],
  "startBinding": null, "endBinding": null,
  "startArrowhead": null, "endArrowhead": "arrow"
}
```

## Evidence card

Use a dark card to show a real path, payload, query, event name, or small contract. This is preferred over a generic label in a technical diagram.

```json
[
  {
    "type": "rectangle", "id": "evidence_card",
    "x": 100, "y": 450, "width": 360, "height": 150,
    "strokeColor": "#1e293b", "backgroundColor": "#1e293b",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 123001,
    "version": 1, "versionNonce": 123001, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "evidence_card_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "evidence_card_text",
    "x": 122, "y": 470, "width": 316, "height": 110,
    "text": "OPENROWSET(\n  BULK '.../gold/orders',\n  FORMAT = 'PARQUET'\n)",
    "originalText": "OPENROWSET(\n  BULK '.../gold/orders',\n  FORMAT = 'PARQUET'\n)",
    "fontSize": 17, "fontFamily": 3, "textAlign": "left", "verticalAlign": "middle",
    "strokeColor": "#22c55e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 123002,
    "version": 1, "versionNonce": 123002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "evidence_card", "lineHeight": 1.25
  }
]
```

Use when: a concrete payload, path, query, event, or contract is the evidence behind a technical claim.

## Vertical pipeline

Use a tall panel when a subsystem contains an ordered sequence. Place one step per row, connect the steps vertically, and keep the labels short.

```json
{
  "type": "rectangle", "id": "vertical_pipeline_panel",
  "x": 1400, "y": 180, "width": 250, "height": 760,
  "strokeColor": "#19a873", "backgroundColor": "#b8f0d8",
  "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "dashed",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 124001,
  "version": 1, "versionNonce": 124001, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null, "locked": false,
  "roundness": {"type": 3}
}
```

Recommended internal sequence:

```text
Parser → Canonicalization → Feature extraction → Quality gate → Publish
```

Use small marker dots or compact white process modules inside the panel rather than five large nested boxes.

## Pattern-board panel

For a two-by-two teaching board, use a colored canvas and four distinct visual constructions inside it. The panel headings remain free-floating and each panel should contain one example plus one takeaway.

```json
{
  "type": "rectangle", "id": "pattern_board_canvas",
  "x": 60, "y": 180, "width": 1180, "height": 780,
  "strokeColor": "#3f55c9", "backgroundColor": "#c4c7ff",
  "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "solid",
  "roughness": 0, "opacity": 100, "angle": 0, "seed": 125001,
  "version": 1, "versionNonce": 125001, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null, "locked": false,
  "roundness": {"type": 3}
}
```

Do not place four identical rectangles inside this canvas. Use a highlighted range, narrowing bracket, tree, and timeline/cycle to make each concept visually different.

## Responsibility / environment panel

Use a single semantic panel when a region needs to state who owns it and where it runs. Keep the responsibility and environment in one concise label.

```json
[
  {
    "type": "rectangle", "id": "responsibility_panel",
    "x": 60, "y": 180, "width": 380, "height": 150,
    "strokeColor": "#27aac7", "backgroundColor": "#bdeefa",
    "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "dashed",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 130001,
    "version": 1, "versionNonce": 130001, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "responsibility_panel_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "responsibility_panel_text",
    "x": 84, "y": 222, "width": 332, "height": 66,
    "text": "Data Platform\nBatch · trusted environment", "originalText": "Data Platform\nBatch · trusted environment",
    "fontSize": 21, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 130002,
    "version": 1, "versionNonce": 130002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "responsibility_panel", "lineHeight": 1.25
  }
]
```

Use when: ownership, runtime, trust zone, or deployment context changes the meaning of the components inside a region.

## Numbered phase

Use a compact rounded process block with a leading ordinal to make phase order visible without adding a separate badge.

```json
[
  {
    "type": "rectangle", "id": "phase_01",
    "x": 100, "y": 280, "width": 250, "height": 78,
    "strokeColor": "#202124", "backgroundColor": "#ffffff",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 131001,
    "version": 1, "versionNonce": 131001, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "phase_01_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "phase_01_text",
    "x": 120, "y": 301, "width": 210, "height": 36,
    "text": "01 · Validate input", "originalText": "01 · Validate input",
    "fontSize": 20, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 131002,
    "version": 1, "versionNonce": 131002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "phase_01", "lineHeight": 1.25
  }
]
```

Use when: a workflow has named stages and the ordinal is part of the explanation, not just decoration.

## Gate / decision

Use the decision fill and diamond geometry for a condition that branches the flow.

```json
[
  {
    "type": "diamond", "id": "quality_gate",
    "x": 480, "y": 270, "width": 190, "height": 120,
    "strokeColor": "#c78900", "backgroundColor": "#fff0a8",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 132001,
    "version": 1, "versionNonce": 132001, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "quality_gate_text", "type": "text"}],
    "link": null, "locked": false, "roundness": null
  },
  {
    "type": "text", "id": "quality_gate_text",
    "x": 520, "y": 310, "width": 110, "height": 40,
    "text": "Passes\nquality gate?", "originalText": "Passes\nquality gate?",
    "fontSize": 18, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 132002,
    "version": 1, "versionNonce": 132002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "quality_gate", "lineHeight": 1.25
  }
]
```

Use when: the reader must follow an explicit yes/no, pass/fail, or safe/unsafe branch.

## Actor swimlane

Use one dashed lane per actor or owner; keep the actor label free-floating and bind only the work item to its process shape.

```json
[
  {
    "type": "rectangle", "id": "actor_lane",
    "x": 60, "y": 180, "width": 520, "height": 180,
    "strokeColor": "#64748b", "backgroundColor": "#e5e7eb",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "dashed",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 133001,
    "version": 1, "versionNonce": 133001, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "actor_lane_label",
    "x": 84, "y": 202, "width": 180, "height": 28,
    "text": "Actor · Data steward", "originalText": "Actor · Data steward",
    "fontSize": 18, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 133002,
    "version": 1, "versionNonce": 133002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  },
  {
    "type": "rectangle", "id": "actor_lane_task",
    "x": 250, "y": 250, "width": 260, "height": 70,
    "strokeColor": "#202124", "backgroundColor": "#ffffff",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 133003,
    "version": 1, "versionNonce": 133003, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "actor_lane_task_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "actor_lane_task_text",
    "x": 270, "y": 267, "width": 220, "height": 36,
    "text": "Approve exception", "originalText": "Approve exception",
    "fontSize": 19, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 133004,
    "version": 1, "versionNonce": 133004, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "actor_lane_task", "lineHeight": 1.25
  }
]
```

Use when: ownership or handoff is part of the story and each action should be read within an actor's responsibility boundary.

## Legend

Use a small three-item key for the semantic colors actually used in the scene; omit unused items.

```json
[
  {
    "type": "ellipse", "id": "legend_trigger_dot",
    "x": 80, "y": 180, "width": 14, "height": 14,
    "strokeColor": "#c78900", "backgroundColor": "#ffd98a",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 134001,
    "version": 1, "versionNonce": 134001, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false
  },
  {
    "type": "text", "id": "legend_trigger_label",
    "x": 104, "y": 176, "width": 110, "height": 24,
    "text": "Trigger", "originalText": "Trigger",
    "fontSize": 16, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
    "strokeColor": "#374151", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 134002,
    "version": 1, "versionNonce": 134002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  },
  {
    "type": "ellipse", "id": "legend_decision_dot",
    "x": 240, "y": 180, "width": 14, "height": 14,
    "strokeColor": "#c78900", "backgroundColor": "#fff0a8",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 134003,
    "version": 1, "versionNonce": 134003, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false
  },
  {
    "type": "text", "id": "legend_decision_label",
    "x": 264, "y": 176, "width": 110, "height": 24,
    "text": "Decision", "originalText": "Decision",
    "fontSize": 16, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
    "strokeColor": "#374151", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 134004,
    "version": 1, "versionNonce": 134004, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  },
  {
    "type": "ellipse", "id": "legend_feedback_dot",
    "x": 400, "y": 180, "width": 14, "height": 14,
    "strokeColor": "#2f6edb", "backgroundColor": "#2f6edb",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 134005,
    "version": 1, "versionNonce": 134005, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false
  },
  {
    "type": "text", "id": "legend_feedback_label",
    "x": 424, "y": 176, "width": 110, "height": 24,
    "text": "Feedback", "originalText": "Feedback",
    "fontSize": 16, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
    "strokeColor": "#374151", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 134006,
    "version": 1, "versionNonce": 134006, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  }
]
```

Use when: color semantics are important enough that the reader should not infer them from shape alone.

## Comparison columns (two or three)

Use parallel columns for shared criteria. Keep two columns for a binary comparison or retain all three for a three-way trade-off.

```json
[
  {
    "type": "rectangle", "id": "comparison_column_a",
    "x": 80, "y": 240, "width": 260, "height": 180,
    "strokeColor": "#3f55c9", "backgroundColor": "#c4c7ff",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 135001,
    "version": 1, "versionNonce": 135001, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "comparison_column_a_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "comparison_column_a_text",
    "x": 104, "y": 288, "width": 212, "height": 84,
    "text": "Option A\nfast · opaque", "originalText": "Option A\nfast · opaque",
    "fontSize": 21, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 135002,
    "version": 1, "versionNonce": 135002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "comparison_column_a", "lineHeight": 1.25
  },
  {
    "type": "rectangle", "id": "comparison_column_b",
    "x": 380, "y": 240, "width": 260, "height": 180,
    "strokeColor": "#3f55c9", "backgroundColor": "#ffffff",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 135003,
    "version": 1, "versionNonce": 135003, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "comparison_column_b_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "comparison_column_b_text",
    "x": 404, "y": 288, "width": 212, "height": 84,
    "text": "Option B\nslower · visible", "originalText": "Option B\nslower · visible",
    "fontSize": 21, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 135004,
    "version": 1, "versionNonce": 135004, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "comparison_column_b", "lineHeight": 1.25
  },
  {
    "type": "rectangle", "id": "comparison_column_c",
    "x": 680, "y": 240, "width": 260, "height": 180,
    "strokeColor": "#3f55c9", "backgroundColor": "#2E2E2E",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 135005,
    "version": 1, "versionNonce": 135005, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "comparison_column_c_text", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "comparison_column_c_text",
    "x": 704, "y": 288, "width": 212, "height": 84,
    "text": "Option C\nbalanced · costly", "originalText": "Option C\nbalanced · costly",
    "fontSize": 21, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 135006,
    "version": 1, "versionNonce": 135006, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "comparison_column_c", "lineHeight": 1.25
  }
]
```

Use when: the teaching job is to compare alternatives along the same criterion; delete column C for a two-column scene.

## Evolution marker

Use an arrowed spine with version markers to show ordered change in state, capability, or schema.

```json
[
  {
    "type": "arrow", "id": "evolution_spine",
    "x": 100, "y": 260, "width": 640, "height": 0,
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 136001,
    "version": 1, "versionNonce": 136001, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "points": [[0, 0], [640, 0]],
    "startBinding": null, "endBinding": null,
    "startArrowhead": null, "endArrowhead": "arrow"
  },
  {
    "type": "ellipse", "id": "evolution_v1_marker",
    "x": 150, "y": 253, "width": 14, "height": 14,
    "strokeColor": "#27aac7", "backgroundColor": "#27aac7",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 136002,
    "version": 1, "versionNonce": 136002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false
  },
  {
    "type": "text", "id": "evolution_v1_label",
    "x": 122, "y": 286, "width": 70, "height": 24,
    "text": "v1", "originalText": "v1",
    "fontSize": 17, "fontFamily": 3, "textAlign": "center", "verticalAlign": "top",
    "strokeColor": "#374151", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 136003,
    "version": 1, "versionNonce": 136003, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  },
  {
    "type": "ellipse", "id": "evolution_v2_marker",
    "x": 410, "y": 253, "width": 14, "height": 14,
    "strokeColor": "#27aac7", "backgroundColor": "#27aac7",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 136004,
    "version": 1, "versionNonce": 136004, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false
  },
  {
    "type": "text", "id": "evolution_v2_label",
    "x": 382, "y": 286, "width": 70, "height": 24,
    "text": "v2", "originalText": "v2",
    "fontSize": 17, "fontFamily": 3, "textAlign": "center", "verticalAlign": "top",
    "strokeColor": "#374151", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 136005,
    "version": 1, "versionNonce": 136005, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  },
  {
    "type": "ellipse", "id": "evolution_v3_marker",
    "x": 670, "y": 253, "width": 14, "height": 14,
    "strokeColor": "#19a873", "backgroundColor": "#b8f0d8",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 136006,
    "version": 1, "versionNonce": 136006, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false
  },
  {
    "type": "text", "id": "evolution_v3_label",
    "x": 642, "y": 286, "width": 70, "height": 24,
    "text": "v3", "originalText": "v3",
    "fontSize": 17, "fontFamily": 3, "textAlign": "center", "verticalAlign": "top",
    "strokeColor": "#374151", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 136007,
    "version": 1, "versionNonce": 136007, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  }
]
```

Use when: releases, versions, migrations, or capability changes must be read in temporal order.

## Confidence boundary

Use a dashed boundary with one label to separate verified material from inferred or assumed material.

```json
[
  {
    "type": "rectangle", "id": "confidence_boundary",
    "x": 60, "y": 180, "width": 620, "height": 260,
    "strokeColor": "#64748b", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "dashed",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 137001,
    "version": 1, "versionNonce": 137001, "isDeleted": false,
    "groupIds": [], "boundElements": [{"id": "confidence_boundary_label", "type": "text"}],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "confidence_boundary_label",
    "x": 84, "y": 198, "width": 280, "height": 28,
    "text": "Verified boundary", "originalText": "Verified boundary",
    "fontSize": 19, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
    "strokeColor": "#64748b", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 137002,
    "version": 1, "versionNonce": 137002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "confidence_boundary", "lineHeight": 1.25
  }
]
```

Use when: the scene must distinguish evidence-backed content from assumptions, estimates, or content outside the known boundary.

## Feedback / retry loop

Use two bound process nodes, a forward connector, and an externally routed return connector. Label the return with the retry reason or policy.

```json
[
  {
    "type": "rectangle", "id": "retry_attempt",
    "x": 120, "y": 260, "width": 220, "height": 76,
    "strokeColor": "#202124", "backgroundColor": "#2E2E2E",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 138001,
    "version": 1, "versionNonce": 138001, "isDeleted": false,
    "groupIds": [], "boundElements": [
      {"id": "retry_attempt_text", "type": "text"},
      {"id": "retry_forward", "type": "arrow"},
      {"id": "retry_feedback", "type": "arrow"}
    ],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "retry_attempt_text",
    "x": 140, "y": 281, "width": 180, "height": 36,
    "text": "Attempt", "originalText": "Attempt",
    "fontSize": 20, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 138002,
    "version": 1, "versionNonce": 138002, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "retry_attempt", "lineHeight": 1.25
  },
  {
    "type": "rectangle", "id": "retry_observe",
    "x": 500, "y": 260, "width": 220, "height": 76,
    "strokeColor": "#19a873", "backgroundColor": "#b8f0d8",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 138003,
    "version": 1, "versionNonce": 138003, "isDeleted": false,
    "groupIds": [], "boundElements": [
      {"id": "retry_observe_text", "type": "text"},
      {"id": "retry_forward", "type": "arrow"},
      {"id": "retry_feedback", "type": "arrow"}
    ],
    "link": null, "locked": false, "roundness": {"type": 3}
  },
  {
    "type": "text", "id": "retry_observe_text",
    "x": 520, "y": 281, "width": 180, "height": 36,
    "text": "Observe result", "originalText": "Observe result",
    "fontSize": 20, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 138004,
    "version": 1, "versionNonce": 138004, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": "retry_observe", "lineHeight": 1.25
  },
  {
    "type": "arrow", "id": "retry_forward",
    "x": 340, "y": 298, "width": 160, "height": 0,
    "strokeColor": "#202124", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "dotted",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 138005,
    "version": 1, "versionNonce": 138005, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "points": [[0, 0], [160, 0]],
    "startBinding": {"elementId": "retry_attempt", "focus": 0, "gap": 8},
    "endBinding": {"elementId": "retry_observe", "focus": 0, "gap": 8},
    "startArrowhead": null, "endArrowhead": "arrow"
  },
  {
    "type": "arrow", "id": "retry_feedback",
    "x": 610, "y": 336, "width": -380, "height": 100,
    "strokeColor": "#2f6edb", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "dashed",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 138006,
    "version": 1, "versionNonce": 138006, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "points": [[0, 0], [0, 100], [-380, 100], [-380, 0]],
    "startBinding": {"elementId": "retry_observe", "focus": 0, "gap": 8},
    "endBinding": {"elementId": "retry_attempt", "focus": 0, "gap": 8},
    "startArrowhead": null, "endArrowhead": "arrow"
  },
  {
    "type": "text", "id": "retry_feedback_label",
    "x": 290, "y": 378, "width": 160, "height": 24,
    "text": "retry ×3", "originalText": "retry ×3",
    "fontSize": 16, "fontFamily": 3, "textAlign": "center", "verticalAlign": "top",
    "strokeColor": "#2f6edb", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
    "roughness": 0, "opacity": 100, "angle": 0, "seed": 138007,
    "version": 1, "versionNonce": 138007, "isDeleted": false,
    "groupIds": [], "boundElements": null, "link": null, "locked": false,
    "containerId": null, "lineHeight": 1.25
  }
]
```

Use when: an observation, quality result, or user signal causes an earlier step to repeat or improve.
