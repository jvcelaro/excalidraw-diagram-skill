# Color Palette & Brand Style

**This is the single source of truth for all colors and brand-specific styles.** To customize diagrams for your own brand, edit this file — everything else in the skill is universal.

The default profile is a ByteByteGo-inspired educational palette: high-contrast ink, bright cyan, mint, lavender, yellow, coral, and blue feedback. This is an original approximation for the user's vault, not a reproduction of ByteByteGo branding.

---

## Shape Colors (Semantic)

Colors encode meaning, not decoration. Each semantic purpose has a fill/stroke pair.

| Semantic Purpose | Fill | Stroke |
|------------------|------|--------|
| Primary/Neutral | `#ffffff` | `#202124` |
| Secondary/Cyan | `#bdeefa` | `#27aac7` |
| Tertiary/Mint | `#b8f0d8` | `#19a873` |
| Start/Trigger | `#ffd98a` | `#c78900` |
| End/Success | `#b8f0d8` | `#19a873` |
| Warning/Reset | `#ffd6d6` | `#d94a55` |
| Decision | `#fff0a8` | `#c78900` |
| AI/LLM | `#dcc8fa` | `#8643b8` |
| Inactive/Disabled | `#e5e7eb` | `#64748b` (use dashed stroke) |
| Error | `#ffc1c1` | `#d22f3a` |
| Comparison/Violet | `#c4c7ff` | `#3f55c9` |
| Accent/Pink | `#f0b6ee` | `#a33bd1` |

**Rule**: Always pair a darker stroke with a lighter fill for contrast.

---

## Text Colors (Hierarchy)

Use color on free-floating text to create visual hierarchy without containers.

| Level | Color | Use For |
|-------|-------|---------|
| Title | `#F8FAFC` | Section headings and major labels placed directly on the canvas |
| Subtitle | `#67E8F9` | Subheadings and title pills placed directly on the canvas |
| Body/Detail | `#E5E7EB` | Descriptions, annotations, and metadata placed directly on the canvas |
| On light fills | `#202124` | Text inside light-colored shapes |
| On dark fills | `#ffffff` | Text inside dark-colored shapes |

---

## Evidence Artifact Colors

Used for code snippets, data examples, and other concrete evidence inside technical diagrams.

| Artifact | Background | Text Color |
|----------|-----------|------------|
| Code snippet | `#1e293b` | Syntax-colored (language-appropriate) |
| JSON/data example | `#1e293b` | `#22c55e` (green) |

---

## Default Stroke & Line Colors

| Element | Color |
|---------|-------|
| Main arrows | Ink (`#202124`), usually dotted or dashed |
| Feedback arrows | Feedback blue (`#2f6edb`), dashed |
| Comparison arrows | Accent pink (`#a33bd1`), dashed |
| Structural lines (dividers, trees, timelines) | Ink (`#202124`) or Slate (`#64748b`) |
| Marker dots (fill + stroke) | Cyan (`#27aac7`) |

---

## Background

Use the **#181926 canvas** profile by default. Keep the semantic shape colors and visual grammar unchanged; adapt direct-on-canvas text to the dark-canvas hierarchy below.

| Profile | Canvas background | Canvas-level text guidance |
|---------|-------------------|----------------------------|
| Standard (default) | `#181926` | Use `#F8FAFC` for titles, `#67E8F9` for subtitles, and `#E5E7EB` for body/details directly on the canvas. |

| Property | Value |
|----------|-------|
| Default canvas background | `#181926` |
| Header divider | `#d1d5db` |
| Header accent bar | `#35cdb0` |
