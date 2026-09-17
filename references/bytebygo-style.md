# ByteByteGo-inspired visual profile

Use this profile as the default visual language for educational system diagrams. It is inspired by the supplied references: clean editorial layouts, large titles, colored section panels, flat illustrations, and explicit flow. Do not copy ByteByteGo logos, trademarks, proprietary illustrations, or exact artwork.

## Output contract

- Generate a native `.excalidraw` scene by default.
- Do not create Mermaid as an intermediate or alternate output unless the user explicitly asks for Mermaid.
- Use `.excalidraw` templates for complete starting layouts. Use `.excalidrawlib` only when the user explicitly requests an importable Excalidraw stencil library; prefer creating/exporting that library through Excalidraw rather than hand-inventing its file schema.
- Use SVG or PNG only for supporting icons and illustrations. Prefer SVG when a sharp, flat icon is available.

## Visual objective

The diagram should teach one idea at a glance. It must answer a concrete question, show a directional story, and make relationships visible through position, containment, line style, and color. It should feel like an educational explainer rather than a dashboard, card grid, or generic architecture poster.

## Page recipes

Choose one recipe before placing elements:

### Architecture explainer

- Canvas target: approximately 1600x1000 for a normal overview; expand only when the content needs it.
- Reserve a 90-120 px header band.
- Put a small accent bar at the far left, followed by a large dark title and an optional cyan title pill.
- Add a thin divider below the header.
- Use one dominant flow area and one or two section panels, not a collection of equal cards.
- Use a tall vertical panel for a sequential pipeline when a subsystem has many stages.
- Put inputs on the left, processing in the middle, outputs on the right or bottom, and feedback loops in blue.

### Pattern board

- Use a strong colored canvas or a neutral canvas with two-by-two or two-by-three teaching panels.
- Each panel gets a large heading, one visual example, and one short takeaway.
- Use different visual patterns inside panels: sliding window as a highlighted range, binary search as a narrowing bracket, backtracking as a decision tree, and DFS as a traversal tree.
- Avoid turning every panel into identical text cards.

### Compact system map

- Use two or three large zones, each with a short title and a few concrete nodes.
- Prefer a single central spine and short feedback arrows over many crossing connectors.
- Use this recipe for a study or task system when the full architecture would be too dense.

## Visual vocabulary

- Section boundaries: rounded rectangles with a 3 px dashed accent stroke and a light semantic fill.
- Primary flow: dark ink, dotted or dashed arrows with clear arrowheads.
- Feedback or iteration: blue dashed arrows; label the feedback relationship.
- Comparison or cross-reference: magenta or violet dashed arrows.
- Processes: rounded rectangles only when containment carries meaning.
- Inputs and outputs: ellipses or simple illustrated objects.
- Hierarchies and timelines: lines, dots, and free-floating text instead of nested boxes.
- Titles and annotations: free-floating text; do not put every label inside a shape.
- Icons: flat, simple, consistently scaled, with a coherent stroke weight. Use supplied vault assets when available; do not invent a logo.

## Typography and spacing

- Use `fontFamily: 3` and `roughness: 0` for the clean technical look.
- Title: 44-64 px; section title: 26-36 px; module label: 20-28 px; supporting detail: 16-20 px.
- Use bold weight for titles and module names, regular weight for explanations.
- Keep labels to one or two lines. Widen the element instead of shrinking text.
- Leave at least 24 px between a shape and its text, and at least 48 px between major zones.
- Keep the main flow visually dominant; supporting annotations should not compete with it.

## Content density

- One diagram should have one teaching question.
- Aim for 3-7 major components and no more than 2-3 levels of visual nesting.
- For technical subjects, include concrete evidence: a real task, note, YAML field, query, event, API name, or small data example.
- For a study/task system, use real examples such as `Capture`, `Triage`, `Study session`, `Next action`, `Review`, and `Feedback`; avoid abstract labels such as `Module 1`.
- If the content does not fit, split it into an overview and detail diagram rather than compressing the canvas.

## Generation sequence

1. State the question and the one-sentence takeaway.
2. Select one page recipe and the reading direction.
3. Assign semantic roles to inputs, processes, decisions, outputs, and feedback.
4. Build the header and section boundaries first.
5. Place the main flow, then add evidence artifacts and icons.
6. Route arrows around shapes; never let a connector cross a label or land in empty space.
7. Render the `.excalidraw` file and inspect the image before delivery.

## Anti-patterns

- Do not default to a uniform grid of equal boxes.
- Do not use a title-only diagram with no visible relationships.
- Do not use many colors without semantic meaning.
- Do not use tiny text to fit an oversized information dump.
- Do not use emoji as a substitute for a consistent icon set unless the user asks for it.
