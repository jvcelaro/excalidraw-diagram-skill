# Acceptance cases

These cases are intentionally small structural regressions. Each prompt is expected to produce one dominant reading grammar, an editable title, concrete evidence, and a review against `references/quality-rubric.md`.

## 1. ETL end-to-end na Azure

- **Prompt:** "Explique um ETL end-to-end na Azure, da chegada de `orders.csv` até uma tabela analítica pronta para BI, mostrando responsabilidades e artefatos concretos."
- **Formato dominante esperado:** architecture / pipeline.
- **Sinais estruturais esperados:** labeled Azure zones; left-to-right ingest -> transform -> serve flow; explicit boundary crossings; arrows bound to components; sample CSV/schema and SQL evidence; editable title.
- **Pontos de revisão humana da rubrica:** question/takeaway is visible; architecture is not a uniform card grid; ownership of ingestion, compute, and serving is unambiguous; evidence is readable; arrows do not cross labels or panels.

## 2. OAuth 2.0

- **Prompt:** "Mostre como OAuth 2.0 Authorization Code com PKCE leva o usuário do login ao acesso limitado a uma API, destacando o que é mecanismo e o que é proteção de segurança."
- **Formato dominante esperado:** mechanism / how-it-works.
- **Sinais estruturais esperados:** actor/client/authorization-server/resource-server roles; causal sequence with authorization code then token; concrete `code_challenge=S256`, token scope, and API request evidence; no implication that the client receives the user password.
- **Pontos de revisão humana da rubrica:** reading order is obvious; security boundary and token scope are clear; request/response arrows are distinguished from redirects; key transition explains why PKCE reduces code interception risk.

## 3. CI/CD com aprovação e rollback

- **Prompt:** "Desenhe um workflow de CI/CD com build, testes, aprovação de produção, canary deploy, health gate e rollback explícito quando a métrica falha."
- **Formato dominante esperado:** workflow with gates.
- **Sinais estruturais esperados:** ordered spine; approval and health decision diamonds; pass and fail branches; explicit rollback path; ownership/artifact labels; concrete YAML evidence such as `environment: production` and `rollback: on_failure`.
- **Pontos de revisão humana da rubrica:** gates actually change the route; failure path is not decorative; start/end and completion are visible; rollback arrow is routed outside the main path; evidence is legible.

## 4. REST vs GraphQL

- **Prompt:** "Compare REST e GraphQL para uma tela que precisa de usuário, pedidos e totais, usando exemplos equivalentes de request/response e concluindo quando cada abordagem é mais adequada."
- **Formato dominante esperado:** comparison.
- **Sinais estruturais esperados:** parallel REST and GraphQL lanes; shared comparison dimensions; equivalent concrete HTTP/query evidence; explicit synthesis or decision rule; editable title.
- **Pontos de revisão humana da rubrica:** same criteria align across lanes; contrast is semantic rather than decorative; endpoint/query behavior is accurate; synthesis states the trade-off without claiming one universal winner.

## 5. Evolução do Redis

- **Prompt:** "Mostre a evolução do Redis de key-value simples para estruturas de dados, cluster, streams e operação em escala, explicando o que cada mudança habilitou."
- **Formato dominante esperado:** evolution / timeline.
- **Sinais estruturais esperados:** chronological spine with ordered milestones; transition labels; endpoint/current-state marker; concrete commands such as `SET`, `HSET`, `XADD`, and `CLUSTER SLOTS`; editable title.
- **Pontos de revisão humana da rubrica:** order is unmistakable; each milestone explains capability change; the timeline is not a row of disconnected cards; command evidence supports the claim; date/version simplifications are clearly treated as teaching scope.

## 6. Batch vs micro-batch vs streaming

- **Prompt:** "Ajude a escolher entre batch, micro-batch e streaming usando latência exigida, tamanho da janela de reprocessamento e complexidade operacional como critérios."
- **Formato dominante esperado:** decision.
- **Sinais estruturais esperados:** decision diamonds or gates; meaningful branches; concrete latency examples (`nightly`, `5 min`, `event-by-event`); three explicit recommendations; rationale adjacent to each outcome.
- **Pontos de revisão humana da rubrica:** criteria drive branches instead of merely labeling options; recommendations preserve trade-offs; no hidden fourth option; reading path is clear from question to outcome.

## 7. Ecossistema de ferramentas de dados

- **Prompt:** "Crie um cheat sheet curto do ecossistema de dados, agrupando ingestão, orquestração, transformação, armazenamento, processamento e BI com um exemplo de comando ou artefato por grupo."
- **Formato dominante esperado:** cheat sheet / taxonomy.
- **Sinais estruturais esperados:** grouped hierarchy; category headings; compact real examples such as `kafka-console-producer`, `dbt run`, `COPY`, and `SELECT`; a scan path that does not imply a causal pipeline.
- **Pontos de revisão humana da rubrica:** grouping principle is explicit; lookup density remains readable; examples are attached to the right category; the scene does not pretend the tools form one mandatory stack.

## 8. DFS/BFS/sliding window/backtracking

- **Prompt:** "Monte um pattern board para DFS, BFS, sliding window e backtracking, com um mini exemplo visual e uma regra de reconhecimento para cada padrão."
- **Formato dominante esperado:** pattern board.
- **Sinais estruturais esperados:** four teaching zones; deliberately different internal visuals: traversal tree, level frontier, highlighted window, and decision tree; one short takeaway per pattern; concrete arrays/edges/pseudocode.
- **Pontos de revisão humana da rubrica:** each panel teaches a distinct pattern; examples are not four uniform text cards; scanning order is intentional; labels and mini diagrams remain readable at export size.

## 9. Git: working directory, staging, local e remote

- **Prompt:** "Explique a passagem de mudanças entre working directory, staging area, local repository e remote repository, incluindo os comandos que movem ou inspecionam cada estado."
- **Formato dominante esperado:** mechanism (chosen over concept map because the teaching job is state transition).
- **Sinais estruturais esperados:** left-to-right state machine; `git add`, `git commit`, `git push`, and `git fetch` arrows; concrete `git diff` / `git diff --cached` evidence; a visible remote boundary and a feedback path.
- **Pontos de revisão humana da rubrica:** state changes are distinct from inspection commands; the mechanism format is justified by causal transitions; remote boundary is clear; fetch feedback does not imply that local commits are overwritten automatically.
