# Human quality rubric

Use this short review after the deterministic validator and after rendering the scene. Mark each item as **pass**, **needs work**, or **not applicable**, and record one concrete observation for every item that needs work.

## Automatable vs. human review

The validator can catch structural defects: valid JSON, the Excalidraw type, non-empty elements, unique IDs, valid color fields, non-empty text elements, and references to existing elements in bindings and containers. Rendering can expose clipping, overlap, and unreadable text. The questions below require human judgment; they should not be reduced to rigid content or aesthetic regex checks.

## Review questions

1. **Question and takeaway** — Is the teaching question clear, and does the scene make one main takeaway easy to state?
2. **Dominant format** — Does the chosen grammar (flow, architecture, comparison, timeline, decision, map, or pattern board) match the teaching job?
3. **Reading and hierarchy** — Is there an obvious entry point and reading direction? Are the most important elements visually dominant without cramped or empty regions?
4. **Relations and boundaries** — Do arrows, lines, proximity, and labels communicate the intended relationships? Are ownership, phases, and system boundaries unambiguous?
5. **Concrete evidence** — Where the topic is technical, does the scene show enough real data, event names, API names, or examples to support the claim?
6. **Visual consistency** — Are color semantics, typography, stroke treatment, spacing, and shape vocabulary used consistently?
7. **Rendered integrity** — After rendering, is every text element readable and unclipped, with no accidental overlaps, broken arrows, or missing content?

A scene is ready when every applicable item passes and the validator reports success. If a human item fails, revise the scene and render again; if only an automated check fails, fix the JSON structure before delivery.
