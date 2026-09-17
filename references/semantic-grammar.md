# Semantic grammar

Use this reference to decide what a visual element means before deciding how to draw it. A shape, line, boundary, or absence of a shape should carry a claim that survives when labels are removed. Use the semantic pairs in `color-palette.md` for any colors; this document does not define a palette.

## Visual roles

| Role | Visual grammar | Use when | Avoid when |
|---|---|---|---|
| Person / actor | A distinct participant node, usually free-floating or lightly bounded; show an action or message leaving the participant | A human, team, client, operator, or external party initiates, approves, owns, or receives something | The person is only a label for a responsibility that is better shown as a lane or boundary |
| System | A stable component node with a name and, when useful, an interface or responsibility inside it | A service, application, device, team-owned subsystem, or external integration performs work or holds state | The node has no behavior, ownership, or connection to explain |
| Data / artifact | An object-like artifact with visible sample content, schema, fields, document shape, or a clearly named payload | The thing is created, read, transformed, transported, stored, or used as evidence | A generic label such as “data” adds no information; use a relationship label or free text instead |
| Process | A bounded action or step whose interior represents work; name the operation with a verb | A transformation, computation, validation, handoff, or repeatable activity changes state or produces an effect | A container is only decorating a noun; use a node or free-floating label for a static concept |
| Decision | A branching condition with visibly distinct outcomes and criteria near the branch | The answer changes the next action, path, permission, or state | The “decision” is merely a grouping or an unexamined yes/no label |
| Output | A result or destination that makes completion, delivery, or changed state visible; show the resulting artifact when possible | The scene needs to answer what the process produces or where responsibility ends | The supposed output is actually an intermediate state or a destination with further work |
| Boundary / environment | A labeled region or lane that encloses elements sharing responsibility, trust, lifecycle, deployment context, or operating environment | Crossing the boundary changes ownership, access, reliability, or the meaning of a connection | It only groups similarly colored cards or makes the page look organized |
| Time | A line, ordered spine, dated marker, phase gap, or aligned lane that encodes order or duration | Sequence, evolution, latency, deadlines, or before/after state matters | Position is incidental and no temporal claim is being made |
| Risk / error | A visibly divergent state or path with a named failure, hazard, uncertainty, or consequence | Failure changes the path, requires mitigation, or is part of the teaching point | A warning is merely decorative or every step is colored as a risk |
| Observability | A probe, log, metric, trace, status, or evidence marker attached to the behavior it reveals | The question includes detection, diagnosis, confidence, SLOs, or proof that a step occurred | It is a generic “monitoring” box with no signal, owner, or observed behavior |

Use the smallest grammar that preserves the claim. A process can be a rectangle, but a sequence may be better represented by a line and markers; an artifact can be a visible payload rather than a generic card; an actor can be a participant at the edge rather than a large panel.

## Containment and responsibility

Containment communicates responsibility when the enclosing region answers at least one of these questions:

- Who owns or operates the enclosed elements?
- Which trust, deployment, data, or failure boundary do they share?
- Which phase, environment, or lifecycle contains them?
- Does crossing the boundary change the contract, authority, or routing of a connection?

In those cases, use a labeled boundary behind its contents and make crossings explicit. The boundary is a semantic object: its label should name the owner, environment, phase, or trust zone, and the contents should have a reason to belong there.

Do not use a box merely because several labels are nearby. Prefer no container for annotations, section titles, timeline labels, hierarchy labels, simple actors, and outputs that are already clear from their position or connection. Use a meaningful shape for a decision, process, artifact, or state only when its form adds information beyond typography.

## Quick test

For every element, state its role in one sentence: “This is an actor that requests…”, “This is an artifact that is read…”, or “This is a boundary that owns…”. If the sentence cannot be completed without referring to its color or visual decoration, the grammar is too weak. If removing the shape would not change the interpretation, remove the container.
