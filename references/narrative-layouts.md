# Narrative layouts

Use only a layout that changes what the viewer can understand. Select one dominant layout after choosing the format; combine layouts only when the secondary one clarifies a local relationship without competing with the main reading path.

## Flow in two phases

**Problem solved:** Makes a meaningful phase boundary visible when the same process has a setup/execute, prepare/commit, or ingest/serve split.

**Use when:** The handoff, pause, contract change, or different responsibility between phases explains the outcome. Give each phase its own reading path and show the small number of cross-phase artifacts or signals.

**Avoid when:** The break is only a visual grouping, or the process is one uninterrupted flow. A divider cannot substitute for a real change in semantics.

## Before / after

**Problem solved:** Shows the effect of a change by aligning the initial and resulting states around the transformation that matters.

**Use when:** A migration, refactor, intervention, decision, or policy changes structure, behavior, or responsibility. Keep shared criteria aligned and make the delta visible.

**Avoid when:** The story has several causal stages, or the two sides are alternatives rather than temporal states. Use comparison for alternatives and a causal flow for multiple steps.

## Overview + zoom

**Problem solved:** Preserves orientation while exposing the detail needed to teach one critical subsystem, interaction, or artifact.

**Use when:** A technical scene needs both a system-level path and one inspectable detail. Keep the overview compact and connect the zoom to the exact component, boundary, or transition it expands.

**Avoid when:** The detail is not necessary to answer the teaching question, or the overview and zoom tell separate stories that should be separate scenes. Do not shrink the whole diagram to fit both.

## Timeline causal

**Problem solved:** Distinguishes “this happened next” from “this caused that” across events, latency, versions, or state changes.

**Use when:** Timing, ordering, delay, trigger, or the reason for a transition matters. Put events on a time spine and label causal links or external conditions separately from mere chronology.

**Avoid when:** Order is incidental or the real structure is dependency, ownership, or a repeatable workflow. Use architecture, workflow, or mechanism flow instead.

## Swimlanes / gates

**Problem solved:** Shows who acts at each step and where a decision, approval, validation, or failure path changes the route.

**Use when:** Responsibility changes between actors or systems and gates are part of the process. Align lanes to participants and place the gate at the point where its result affects the next action.

**Avoid when:** There is only one actor, no meaningful branch, or lanes would be empty scaffolding. Use a simple flow or timeline when ownership is not part of the lesson.

## Comparison matrix with evidence

**Problem solved:** Makes alternatives comparable on the same dimensions while preventing unsupported claims from looking like facts.

**Use when:** The viewer must choose or understand trade-offs across two or more options. Align criteria, show equivalent evidence on each side, and end with a synthesis or decision rule.

**Avoid when:** The options share a process that should be shown once, or the matrix would hide causal behavior. Use a branched common flow or decision layout instead.

## Rail / pipeline vertical

**Problem solved:** Keeps a long, ordered process readable when horizontal space is limited or when every stage needs a compact annotation and artifact.

**Use when:** A sequence has a stable spine, repeated stages, or many top-to-bottom dependencies. Attach inputs, outputs, checks, and evidence to the rail; reserve side branches for exceptions or feedback.

**Avoid when:** The main point is parallelism, dense cross-linking, or a two-dimensional system boundary. A vertical rail can falsely imply serial execution.
