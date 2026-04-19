# Generic Design Translations

This doc exists for one reason:

- the current design prep is strong, but it is very manufacturing-shaped

That is useful for Anduril, but you do not want to sound overfit if the interviewer asks a more generic internal-platform or full-stack systems question.

So the right move is:

- keep the manufacturing designs
- also understand the generic system shape underneath them

This lets you do both:

- answer a role-shaped prompt well
- pivot if the prompt is broader or more abstract

## The Core Translation

- `MES` -> workflow engine / task execution platform
- `genealogy` -> audit trail / lineage system
- `engineering change rollout` -> versioned config rollout system
- `quality hold / rework` -> policy enforcement + exception workflow
- `factory visibility` -> real-time operational dashboard / observability product

## 1. MES -> Workflow Engine / Task Execution Platform

### Manufacturing Version

- units move through stations
- operators complete steps
- materials are consumed
- work instructions apply by revision

### Generic Version

- entities move through a multi-step workflow
- users or services execute tasks
- prerequisites must be satisfied
- actions create durable execution state

### Generic Prompt It Maps To

- design a workflow engine
- design a task execution system
- design an internal operations platform for multi-step processes

### What To Say Generically

"I’d model the system around versioned workflow definitions and execution instances. Definitions describe what should happen, while execution records capture what actually happened. I’d keep append-only execution history for auditability and derive current task state through projections or current-state tables. The core engine would handle assignment, completion, failures, retries, and exception paths."

### Generic Entities

- `WorkflowDefinition`
- `WorkflowVersion`
- `TaskDefinition`
- `ExecutionInstance`
- `TaskExecution`
- `Assignment`
- `ExecutionEvent`
- `ExceptionState`

### Key Design Points

- state machine over ad hoc status fields
- append-only history
- user/task assignment
- retries and exception paths
- versioned definitions

## 2. Genealogy -> Audit Trail / Lineage System

### Manufacturing Version

- which components, lots, operators, and tests contributed to a unit

### Generic Version

- how did this object come to be in its current state?
- what upstream inputs, actors, transformations, and approvals contributed to it?

### Generic Prompt It Maps To

- design an audit trail system
- design a lineage system
- design a system to trace changes and dependencies across objects

### What To Say Generically

"I’d model lineage as append-only events plus explicit relationships between upstream and downstream objects. The important capability is reconstructing history and answering both forward and backward queries: how did object X get here, and what else was affected by input Y. I’d likely start with relational storage and indexed edge tables, then build read models for common investigation and compliance queries."

### Generic Entities

- `Object`
- `LineageEdge`
- `TransformationEvent`
- `Actor`
- `Approval`
- `ArtifactVersion`
- `AuditEvent`

### Key Design Points

- immutable history
- forward and backward traceability
- correction without destructive overwrite
- investigation-oriented queries

## 3. Engineering Change Rollout -> Versioned Config Rollout System

### Manufacturing Version

- new BOM / instructions / routing revision rolls into a live factory

### Generic Version

- new configuration or definition version rolls into a live system with in-flight work

### Generic Prompt It Maps To

- design a config rollout system
- design a safe change management platform
- design staged rollout for workflow definitions or policies

### What To Say Generically

"I’d treat this as a control-plane rollout problem. The core challenge is not storing the new version, but deciding where and when it applies, validating dependencies, and safely handling in-flight work. I’d use explicit versioning, applicability rules, staged rollout, compatibility checks, and durable recording of which version each execution instance actually used."

### Generic Entities

- `DefinitionVersion`
- `ApplicabilityRule`
- `RolloutPlan`
- `CompatibilityCheck`
- `ExecutionBinding`
- `RollbackState`

### Key Design Points

- explicit versioning
- staged rollout
- mixed old/new support
- applicability by tenant, region, cohort, or instance
- rollback is not always symmetric

## 4. Quality Hold / Rework -> Policy Enforcement + Exception Workflow

### Manufacturing Version

- failed units or suspect lots are blocked, investigated, reworked, or scrapped

### Generic Version

- risky or invalid entities are blocked, reviewed, corrected, retried, or permanently rejected

### Generic Prompt It Maps To

- design an exception workflow
- design a policy enforcement system
- design hold / review / release flows for sensitive operations

### What To Say Generically

"I’d design this as a policy enforcement system integrated with the execution platform. When an object violates a rule or is associated with a risky upstream input, the system should create a durable exception state, enforce restrictions at the API level, and route the object into an investigation and disposition workflow. The main requirements are safe containment, explicit disposition states, and full auditability."

### Generic Entities

- `PolicyViolation`
- `BlockedEntity`
- `Disposition`
- `ReviewTask`
- `ExceptionWorkflow`
- `ReleaseDecision`

### Key Design Points

- enforcement in core APIs, not just the UI
- conservative initial containment
- explicit review and release states
- blast radius if the issue comes from shared upstream input

## 5. Factory Visibility -> Real-Time Operational Dashboard / Observability Product

### Manufacturing Version

- stations, queue depth, yield, downtime, blockers

### Generic Version

- system health, workflow throughput, backlog, error states, and bottlenecks

### Generic Prompt It Maps To

- design a real-time dashboard
- design operational visibility for a workflow system
- design an observability product for internal operations

### What To Say Generically

"I’d design this as a read-optimized observability layer on top of operational events and telemetry. The write path remains in the source systems, while a projection layer materializes current status, throughput, backlog, failures, and recent changes for users who need fast situational awareness. I’d separate low-latency dashboards from slower investigation paths and make freshness explicit."

### Generic Entities

- `OperationalEvent`
- `HealthSignal`
- `ProjectionView`
- `ThroughputMetric`
- `BacklogView`
- `IncidentState`

### Key Design Points

- read/write separation
- projections for low-latency views
- role-specific dashboards
- freshness and staleness indicators

## How To Use This In Interviews

The best pattern is:

1. Start generic.
2. Show clear system-design structure.
3. If relevant, add domain nuance.

That means instead of opening with:

- "I’d build an MES with station-level execution and traveler state..."

you might start with:

- "I’d model this as a workflow execution system with versioned definitions and append-only execution history..."

and then, if the role or interviewer seems to want domain depth, add:

- "In a manufacturing context, those execution instances would map to serialized units moving through stations."

That sequence is safer because it shows:

- systems fluency first
- domain sensitivity second

## Final Rule

The role-specific language is a strength.

Just do not make it your only language.

You want to be able to answer both:

- the Anduril-shaped question
- the generic system-design question underneath it
