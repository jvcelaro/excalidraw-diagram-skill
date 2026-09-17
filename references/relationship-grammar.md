# Relationship grammar

Use this reference when the scene teaches how things interact. A connection encodes a claim about direction, timing, authority, data, causality, or change. Choose line weight, dash pattern, arrowheads, and color for that claim using the available semantic palette; these are not a fixed aesthetic recipe.

## Relationship types

| Relationship | What the line must communicate | Useful treatment | Label when |
|---|---|---|---|
| Command / request | One participant asks another to perform an action; direction follows authority or invocation | Directional connector toward the receiver; distinguish the request from its result if both are shown | The action, method, permission, or caller is not obvious |
| Asynchronous event | A producer emits a fact or signal without requiring an immediate response | Directional connector with an event cue; avoid implying a synchronous return path | Name the event or topic, and show delivery/ordering semantics when they matter |
| Read / write | A component accesses or changes a data artifact | Direction toward the artifact for a read; toward the artifact with a write label, or a clearly distinct semantic treatment, for mutation | Always label when the same pair has both reads and writes |
| Data flow | A payload, record, token, or artifact moves or is transformed | Directional connector between artifact states or processing stages; attach the payload name or format | The moving thing, transformation, or unit is not visible from the nodes |
| Dependency | One element relies on another capability, condition, or resource | Use a non-causal dependency connector or dependency marker; do not make it look like runtime data flow | The dependency is architectural, optional, indirect, or easy to confuse with invocation |
| Feedback / retry | A later observation or result returns to an earlier step to improve, repeat, or correct it | Return connector routed outside the primary path; mark retry, feedback, or the triggering condition | Always label the reason or retry policy when it is not self-evident |
| Failure / escalation | A failed, unsafe, or blocked path moves to recovery, fallback, human review, or a higher owner | Divergent connector from the failure point to the handling path; make the consequence visible | Name the failure condition, escalation target, or recovery action |
| Comparison | Two elements are being related by a shared criterion, analogy, or contrast rather than a runtime path | Use a non-flow connector or aligned comparison mark; do not add an arrow unless direction is part of the claim | Label the criterion, evidence, or contrast being compared |
| Temporal transition | A state, version, phase, or capability changes over time | Connect ordered states along a time spine; use dates or transition conditions near the link | The reason, release, trigger, or effect of the transition needs explanation |

## Direction and labels

Use arrowheads only where direction matters. A line without an arrow can mean alignment, structure, comparison, or an undirected relation; it must not silently stand in for a flow. Place labels close to the segment they qualify, not in empty space between unrelated nodes.

Label connections that are non-obvious, overloaded, cross a boundary, carry a meaningful artifact, or represent an exception path. Short verb or noun phrases are enough: `POST /orders`, `emits OrderCreated`, `reads cache`, `retry ×3`, `escalates to on-call`, or `v2 → v3: schema change`. Do not label every obvious adjacency; excess labels flatten the hierarchy.

## Routing rules

- Establish the primary path first, then route feedback, failure, and cross-reference paths around it.
- Bind connectors to the actual source and target elements. A line that merely passes near a node does not communicate a relationship.
- Keep synchronous request/response, asynchronous event, data movement, and dependency visually distinguishable even when they share endpoints.
- When multiple relationships share a pair of nodes, use parallel routes or explicit labels; never rely on position alone.
- Cross a boundary only for a relationship that genuinely crosses ownership, trust, environment, or phase. Make the crossing legible.
- Prefer one clear connector per claim. Split a compound relationship into separate labeled connectors when the timing or direction differs.

The goal is semantic legibility, not a universal line style. If a chosen stroke or color is unavailable, preserve the distinction with direction, dash pattern, routing, label, or an adjacent marker rather than inventing a new palette.
