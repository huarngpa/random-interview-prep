# QuickSight Vs Bedrock Agents

This note covers a modern architecture choice that comes up in operational software:

- when should the answer be BI?
- when should the answer be an agentic app?

The confusion usually comes from people collapsing two different products into one mental bucket.

## Two Different Things

### 1. QuickSight / Amazon Q In QuickSight

Use this when the product is basically:

```text
natural language -> BI chart / dashboard / business analysis
```

Example:

- "Show defect rate by station over the last 7 days."

This is a BI problem.

The user wants:

- a chart
- a table
- a dashboard summary
- maybe a generated calculation

QuickSight is a good fit when the answer should come from:

- curated datasets
- trusted metrics
- governed business logic

### 2. Bedrock Agent Or Custom App Agent

Use this when the product is more like:

```text
natural language -> reason -> call tools / APIs -> answer or action
```

Example:

- "Why is Line 3 behind schedule, and open an incident if station 7 is the bottleneck."

That is not just BI.

That is an operational assistant.

It needs:

- tool calling
- retrieval
- permissions
- evidence
- maybe actions

## The Practical AWS Shape

For an operational assistant, the architecture often looks like:

```text
User
  ↓
Web app / chat UI
  ↓
Bedrock Agent or your own orchestrator
  ↓
Tools:
  - Athena query over S3 / Iceberg
  - OpenSearch search
  - internal APIs
  - ERP / MES APIs
  - ticket / incident API
  ↓
Answer with citations / evidence / action summary
```

## A Good Mental Model

Think in layers.

### Context Layer

Examples:

- SOPs
- runbooks
- work instructions
- incident playbooks
- quality procedures

Good fit:

- Bedrock Knowledge Bases or your own RAG layer

### Structured Query Layer

Examples:

- historical metrics
- line throughput
- defect counts
- cycle time by station

Good fit:

- Athena over S3 / Iceberg
- warehouse queries
- governed SQL views

### Search Layer

Examples:

- logs
- incidents
- indexed workflow projections
- event history

Good fit:

- OpenSearch

### Action Layer

Examples:

- open incident
- create work order
- fetch line health
- fetch blocked units
- escalate quality hold

Good fit:

- Lambda-backed tools
- internal APIs
- action groups

## The Important Distinction

The agent is not the LLM itself.

The agent is the orchestration boundary around the model:

- system prompt
- tool definitions
- retrieval
- permissions
- planning loop
- guardrails
- audit logs
- human approval rules

That distinction matters a lot in interviews.

It shows you are thinking in systems, not vibes.

## Quick Decision Rule

```text
BI-only analytics
-> QuickSight / Amazon Q in QuickSight

Operational assistant inside your app
-> Bedrock Agent + action groups + knowledge base

Strict permissions, custom UX, complex tool routing
-> custom orchestrator using Bedrock models + your own tool router
```

## Worked Example

Example prompt:

- design an AI assistant for factory operations

How I would work it:

1. Clarify whether the user wants dashboards or an operational assistant.
2. Clarify whether the assistant needs to take actions or only answer questions.
3. Assume:
   - users want explanations and evidence
   - some workflows require actions
   - destructive actions need human approval

Concrete design:

- use a normal web app or internal operations console as the front end
- use a Bedrock-powered orchestration layer
- give it tools like:
  - `getLineHealth(factoryId, lineId)`
  - `searchIncidents(query)`
  - `queryAthena(sqlTemplate, params)`
  - `searchEvents(filters)`
  - `openIncident(payload)`
- use a knowledge base or RAG layer for:
  - SOPs
  - work instructions
  - known issue playbooks
- require approval for actions like:
  - opening incidents
  - changing workflow state
  - creating or modifying operational records

Why these choices:

- BI tools are great for charts and summary analysis, but weak at operational tool use
- agents are useful when the system must reason across multiple tools and possibly act
- permissions and approvals must live outside the model
- evidence-based output is critical for trust in operational settings

What I would not do:

- let the model directly mutate core system state with no approval path
- use QuickSight as a substitute for a tool-calling operational assistant
- let the model invent answers when structured evidence is available

## Practical Design Choices

### When I Would Choose QuickSight

- the user mostly wants:
  - dashboards
  - slicing and filtering
  - natural-language questions over metrics
- the data model is curated and business-oriented
- the output is mostly visual or tabular

### When I Would Choose Bedrock Agents

- the user wants:
  - root cause analysis
  - evidence gathering
  - summarization across multiple systems
  - tool-calling
  - actions or escalations

### When I Would Choose A Custom Orchestrator

- permissions are strict and complex
- tool routing is specialized
- the UX is embedded in an app, not a generic assistant shell
- you need deep control over retries, planning, and audit

In practice, this is often the strongest answer for a serious internal platform:

- use Bedrock models
- but keep the orchestration logic under your control

## What This Sounds Like In An Interview

A strong answer:

> I’d use QuickSight if the problem is natural-language BI over curated datasets. But for a factory operations assistant, I’d build an agentic layer with Bedrock or a custom orchestrator: knowledge retrieval for runbooks and SOPs, structured query tools like Athena, search over indexed operational data with OpenSearch, and internal APIs for operational actions. I’d keep permissions, approvals, and auditability outside the model, and require human approval for destructive actions.

That sounds grounded, modern, and operationally responsible.

## Why This Matters For Our Prep

This note is really about:

- separating analytics from action
- separating model capability from system responsibility
- showing good judgment around AI in operations

That is exactly the kind of distinction strong interviewers like.
