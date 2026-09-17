# Editorial format router

Use this router after classifying the user's intent and writing a short editorial brief. Choose one primary format before placing elements. The format is a teaching decision: it determines the reading path and the visual grammar, while the ByteByteGo-inspired profile supplies the visual language.

## Required sequence

1. **Classify intent** — identify the question the diagram must answer: mechanism, structure, procedure, contrast, change over time, choice, recall, relationships, or reusable visual vocabulary.
2. **Write a short editorial brief** — state the audience, teaching question, one-sentence takeaway, scope, and the intended reading direction in a few lines.
3. **Choose the format** — use the routing table below; select the format that makes the core relationship visible with the least explanation.
4. **Build the scene** — choose the page recipe, map concepts to patterns, place the main flow, then add evidence and annotations.
5. **Render** — produce the native `.excalidraw` scene by default and render it to PNG.
6. **Evaluate** — inspect the image against the brief, the chosen format, and the visual quality checklist; fix and render again when needed.

If more than one format seems plausible, choose the one that makes the primary relationship structurally unavoidable. A secondary format may appear as a local pattern, but the page must still have one dominant reading grammar.

## Routing table

### Mechanism / how-it-works

- **When to use:** Explain behavior, transformation, or why an outcome follows from inputs and intermediate steps.
- **Structure of reading:** left-to-right or top-to-bottom causal flow: input → mechanism → output, with feedback or branches labeled.
- **Indispensable elements:** concrete input/output examples, named operations or stages, directional arrows, and at least one causal annotation explaining the key transition.
- **Antiuse:** Do not use it for a static inventory of components; use architecture instead.

### Architecture

- **When to use:** Explain parts, boundaries, ownership, and connections in a system or domain.
- **Structure of reading:** zones or layers first, then the dominant path through components; inputs enter from one side and outputs leave another.
- **Indispensable elements:** section boundaries, component responsibilities, real interfaces or data artifacts, and arrows for every meaningful relationship.
- **Antiuse:** Do not turn it into a uniform grid of labeled boxes with no behavior or flow.

### Workflow with gates

- **When to use:** Teach a repeatable process in which decisions, approvals, checks, or failure paths change what happens next.
- **Structure of reading:** ordered steps along a spine, with decision diamonds or gates branching to explicit next actions and a visible completion path.
- **Indispensable elements:** start/end, numbered or clearly ordered steps, gate criteria, pass/fail branches, and ownership or artifacts at the steps where they matter.
- **Antiuse:** Do not use it when the topic is merely a sequence with no meaningful branching; use a timeline or mechanism flow.

### Comparison

- **When to use:** Contrast two or more alternatives, states, strategies, or trade-offs.
- **Structure of reading:** parallel columns or lanes with aligned criteria, followed by a concise synthesis or decision point.
- **Indispensable elements:** shared comparison dimensions, visual contrast with semantic meaning, equivalent evidence on each side, and a clear takeaway about the difference.
- **Antiuse:** Do not use it to show a process that both options share; use a common flow with a branch.

### Evolution / timeline

- **When to use:** Show change across time, versions, stages of maturity, or historical progression.
- **Structure of reading:** a chronological spine with anchored milestones; use periods or eras as readable gaps or bands rather than disconnected cards.
- **Indispensable elements:** an explicit time direction, dated or ordered milestones, changes that explain why each transition matters, and a current or endpoint state.
- **Antiuse:** Do not use it when order is incidental and the real topic is dependency or causality; use mechanism or workflow.

### Decision

- **When to use:** Help someone choose an option based on constraints, priorities, or observable conditions.
- **Structure of reading:** criteria or questions lead through a small decision tree or matrix to recommendations, with trade-offs visible near the branch that creates them.
- **Indispensable elements:** decision criteria, meaningful branches, resulting actions/options, and a concise rule or rationale at the outcome.
- **Antiuse:** Do not use it as a disguised comparison table when there is no conditional choice.

### Cheat sheet / taxonomy

- **When to use:** Support quick lookup, recall, or classification of a bounded set of commands, terms, patterns, or categories.
- **Structure of reading:** grouped hierarchy with a strong scan path, short labels, and examples attached to the category they clarify.
- **Indispensable elements:** category headings, consistent notation, compact examples, and an explicit grouping principle.
- **Antiuse:** Do not use it to explain a multi-step causal story; a lookup grid cannot substitute for a flow.

### Concept map

- **When to use:** Reveal a network of related ideas, definitions, influences, or prerequisites when no single linear path dominates.
- **Structure of reading:** a central or bounded set of concepts with labeled relationships, clusters, and selective cross-links.
- **Indispensable elements:** named relationship types, readable clusters, a clear entry point, and enough spacing to distinguish primary from secondary links.
- **Antiuse:** A radial mind map is **not** the default when the topic contains causality, dependency, sequence, or gates; use a flow, architecture, workflow, or timeline so those relationships are encoded directly.

### Pattern board

- **When to use:** Teach several related visual or operational patterns side by side, especially when each pattern has its own compact example and takeaway.
- **Structure of reading:** a curated two-by-two or two-by-three set of teaching zones, with deliberate variation inside each zone and a shared title/question.
- **Indispensable elements:** one heading, one visual example, and one short takeaway per pattern, plus a common comparison frame.
- **Antiuse:** Do not use it as a general-purpose dashboard or a collection of equal cards for a single story.

## Format selection guardrails

- Preserve `.excalidraw` as the default output. Use Mermaid only when the user explicitly asks for a text-based Mermaid diagram.
- Keep the chosen format dominant; do not mix incompatible reading grammars merely to fit more content.
- Prefer concrete evidence for technical topics: real events, fields, commands, data, interfaces, or examples.
- If the brief cannot be taught clearly in one scene, split it into an overview and a detail scene instead of shrinking text or adding decorative containers.
