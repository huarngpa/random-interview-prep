# Modern Primer Shapes Worth Studying

This doc is the answer to:

- the `system-design-primer` is useful, but too generic and a bit dated
- which shapes are still worth studying for this Anduril loop?
- how should we modernize them?

The goal is not to relearn every classic internet-scale interview.

The goal is to extract the generic system-design patterns that still matter for:

- internal platforms
- workflow-heavy software
- operational tooling
- real-time visibility
- auditability
- safe rollout

## What To Keep From The Primer

Keep the fundamentals:

- requirement clarification
- API-first thinking
- read/write paths
- storage choice
- consistency and availability tradeoffs
- queues and asynchronous processing
- caching and projections
- retries, idempotency, and failure handling
- observability

## What To Mostly Ignore For This Loop

These are still educational, but not high-yield here:

- URL shortener
- social feed / Twitter clone
- chat app at global internet scale
- CDN-heavy media systems
- ride-sharing dispatch
- ad click / ad ranking systems

Those prompts optimize for consumer internet instincts.

Your likely loop wants:

- internal systems
- workflow execution
- operational state
- real users and messy constraints

## The Modern Set

These are the generic system shapes I would actually study.

1. Real-time operational dashboard
2. Workflow / task execution platform
3. Audit trail / lineage system
4. Versioned config / rollout system
5. Policy enforcement / exception workflow
6. Event pipeline / notifications
7. Search and query over operational data

## 1. Real-Time Operational Dashboard

### Classic Primer Version

- design a monitoring dashboard
- metrics come in, users look at charts

### Modern Version

- design a low-latency operational visibility product
- supports both current state and drill-down investigation
- serves different users with different levels of abstraction

### What Matters Now

- event-driven ingestion
- projection or materialized views for current state
- freshness indicators, not fake real-time
- role-specific views
- drill-down path from dashboard to raw evidence

### Default Modern Architecture

- sources emit operational events
- stream processor or projection builder updates read models
- APIs serve summary views and detail views separately
- websocket / SSE for live updates
- warehouse or lake path for historical analytics

### Good Tradeoffs To Mention

- freshness vs correctness
- projections vs direct queries on source tables
- polling vs push
- summary read path vs investigation read path

### Common Interview Mistake

Treating this like a charting problem instead of an operational state problem.

### Anduril Mapping

- factory visibility
- line health
- queue depth
- blockers
- station or workflow observability

### Worked Solution

Example prompt:

- design a real-time operational dashboard for supervisors tracking workflow health across many teams or lines

How I would work it:

1. Clarify whether the dashboard is only for current state or also for historical investigation.
2. Assume current state matters most, but drill-down is required.
3. Treat raw operational events as the source of truth.
4. Build projections for the live UI instead of querying raw events directly.

Concrete design:

- producers emit events like `task_started`, `task_failed`, `queue_depth_changed`, `station_heartbeat`
- events go into Kafka or Kinesis
- projection workers consume events and update:
  - `service_health_view`
  - `queue_depth_view`
  - `backlog_view`
  - `incident_view`
- the dashboard reads from those projection tables or documents
- websocket or SSE pushes updates to active clients
- a separate historical analytics path lands raw events in a warehouse or lake

Why these choices:

- projections make current state fast and predictable
- the event log preserves history and supports replay
- separating summary views from historical analytics keeps the UI responsive
- websocket/SSE fits a live dashboard better than polling every second

What I would not do:

- query raw transactional tables directly from the dashboard
- use the search index as the source of truth
- promise perfect real-time if freshness depends on projections

The answer I want to sound like:

- "I’d treat this as an observability product, not a charting page. I want durable operational events feeding low-latency read models, with freshness indicators and a clear path from high-level status down to raw evidence."

Concrete decisions I would make:

- source of truth: append-only operational event stream
- current-state storage: SQL projection tables for predictable relational queries
- live update path: SSE first, websockets only if bidirectional interactivity is needed
- history path: raw events copied into a warehouse or lake, not served from dashboard tables
- freshness model: every projection row stores `updated_at` so the UI can show staleness explicitly

Schema sketch:

```sql
create table operational_event (
  id uuid primary key,
  source text not null,
  entity_type text not null,
  entity_id text not null,
  event_type text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);

create table queue_depth_view (
  queue_name text primary key,
  depth int not null,
  blocked_count int not null default 0,
  updated_at timestamptz not null
);

create table service_health_view (
  service_name text primary key,
  status text not null,
  error_rate numeric not null,
  lag_ms int not null,
  updated_at timestamptz not null
);
```

Quick technical sketch:

```python
class ProjectionWorker:
    def handle(self, event: dict) -> None:
        match event["event_type"]:
            case "task_enqueued":
                self._increment_queue(event["payload"]["queue_name"])
            case "task_started":
                self._decrement_queue(event["payload"]["queue_name"])
            case "service_heartbeat":
                self._update_health(event["source"], event["payload"])

    def _increment_queue(self, queue_name: str) -> None:
        pass

    def _decrement_queue(self, queue_name: str) -> None:
        pass

    def _update_health(self, service_name: str, payload: dict) -> None:
        pass
```

## 2. Workflow / Task Execution Platform

### Classic Primer Version

- design a task scheduler
- design a job system

### Modern Version

- design a workflow execution platform with versioned definitions, assignment, retries, and exception paths

### What Matters Now

- state machines over ad hoc status fields
- versioned workflow definitions
- append-only execution history
- retries, timeouts, and reassignment
- human-in-the-loop steps

### Default Modern Architecture

- workflow definition service
- execution engine
- task assignment / queueing
- append-only event history
- read models for current task state

### Good Tradeoffs To Mention

- mutable status vs event history
- orchestration vs choreography
- synchronous user action vs async downstream effects
- generic engine vs domain-specific workflow logic

### Common Interview Mistake

Only describing queues and workers without modeling workflow state.

### Anduril Mapping

- MES
- station execution
- work orders
- operator workflows

### Worked Solution

Example prompt:

- design a workflow execution platform for internal teams handling multi-step operational tasks

How I would work it:

1. Clarify whether workflows are fixed or versioned.
2. Clarify whether humans, machines, or both perform tasks.
3. Assume versioned workflows with human-in-the-loop steps and exception paths.

Concrete design:

- `WorkflowDefinition` stores the approved template
- `WorkflowVersion` stores each released change
- `ExecutionInstance` represents one running workflow
- `TaskExecution` stores current task status
- `ExecutionEvent` stores append-only history
- an execution service handles:
  - create instance
  - assign task
  - complete task
  - fail task
  - retry / reroute task
- read models provide:
  - current status by workflow
  - backlog by queue
  - failed tasks needing attention

Storage choice:

- SQL for workflow definitions, assignments, and current execution state
- append-only event table for history
- optional queue or stream for async side effects

Why these choices:

- workflow systems are naturally relational
- event history is needed for auditability and debugging
- explicit versioning matters once definitions evolve
- current-state tables keep UI reads simple while event history keeps truth reconstructable

What I would not do:

- model everything with one mutable `status` field
- mix definition updates with in-flight execution history
- overcomplicate with microservices too early

The answer I want to sound like:

- "I’d separate the workflow definition from execution instances, keep append-only execution history, and make the core engine responsible for state transitions, retries, and exception handling."

Concrete decisions I would make:

- source of truth: SQL for workflow definitions, assignments, and execution instances
- history: append-only event table for audit and replay
- workflow control: explicit state machine rules, not free-form status mutations
- retries: store retry count and next-attempt time in task execution rows
- versioning: bind each execution instance to a workflow version at creation time

Schema sketch:

```sql
create table workflow_version (
  id uuid primary key,
  workflow_name text not null,
  version int not null,
  definition jsonb not null,
  status text not null
);

create table execution_instance (
  id uuid primary key,
  workflow_version_id uuid not null references workflow_version(id),
  status text not null,
  current_step text,
  created_at timestamptz not null default now()
);

create table task_execution (
  id uuid primary key,
  execution_instance_id uuid not null references execution_instance(id),
  task_name text not null,
  assignee text,
  status text not null,
  retry_count int not null default 0,
  next_attempt_at timestamptz
);
```

Quick technical sketch:

```python
class WorkflowEngine:
    def complete_task(self, execution_id: str, task_name: str, actor_id: str) -> None:
        current = self._load_execution(execution_id)
        next_state = self._transition(current, task_name, "complete")
        self._append_event(execution_id, "task_completed", {"task_name": task_name, "actor_id": actor_id})
        self._save_execution(next_state)

    def fail_task(self, execution_id: str, task_name: str, reason: str) -> None:
        current = self._load_execution(execution_id)
        next_state = self._transition(current, task_name, "failed")
        self._append_event(execution_id, "task_failed", {"task_name": task_name, "reason": reason})
        self._save_execution(next_state)
```

## 3. Audit Trail / Lineage System

### Classic Primer Version

- design an audit log

### Modern Version

- design a system that can reconstruct history, support compliance, and answer forward/backward lineage queries

### What Matters Now

- immutable history
- explicit relationships between objects
- version and actor attribution
- correction without destructive overwrite
- investigation-oriented query support

### Default Modern Architecture

- append-only audit events
- lineage edges between related objects
- read models for common ancestry / where-used / history queries
- strong identity and idempotency on writes

### Good Tradeoffs To Mention

- relational edge tables vs graph database
- exact source-of-truth writes vs async projections
- current state lookup vs historical reconstruction

### Common Interview Mistake

Saying “just store logs” without designing how investigators actually query them.

### Anduril Mapping

- genealogy
- traceability
- compliance
- blast-radius analysis

### Worked Solution

Example prompt:

- design an audit trail and lineage system for high-stakes internal operations

How I would work it:

1. Clarify whether the key queries are:
   - history of one object
   - blast radius from one bad input
   - actor and version attribution
2. Assume all three matter.

Concrete design:

- every important write emits an `AuditEvent`
- related objects are connected with `LineageEdge`
- the source-of-truth store is relational:
  - `audit_event`
  - `lineage_edge`
  - `object_identity`
- projections support:
  - full history for object X
  - all downstream objects touched by input Y
  - all actions by actor Z
- a search layer can index serials, IDs, and key metadata for investigation UX

Why these choices:

- relational storage is operationally simpler and good enough for known query patterns
- append-only history preserves compliance and debugging value
- lineage edges make forward and backward traceability explicit
- projections and search make investigator workflows usable

What I would not do:

- treat logs alone as the design
- overwrite old history for convenience
- jump straight to a graph database without evidence it is necessary

The answer I want to sound like:

- "I’d model this as immutable audit history plus explicit lineage relationships, so I can answer both ‘how did this object get here?’ and ‘what else was affected by this input?’"

Concrete decisions I would make:

- source of truth: relational edge tables plus append-only audit events
- correction model: superseding records instead of destructive updates
- query model: precomputed ancestry / where-used projections for common investigations
- search layer: OpenSearch for investigator UX, but not authoritative truth
- identity: every write carries a stable operation key to prevent duplicate lineage edges

Schema sketch:

```sql
create table object_identity (
  id uuid primary key,
  object_type text not null,
  external_ref text not null,
  created_at timestamptz not null default now()
);

create table lineage_edge (
  id uuid primary key,
  parent_id uuid not null references object_identity(id),
  child_id uuid not null references object_identity(id),
  edge_type text not null,
  source_event_id uuid not null,
  created_at timestamptz not null default now()
);

create table audit_event (
  id uuid primary key,
  object_id uuid not null references object_identity(id),
  event_type text not null,
  actor_id text,
  payload jsonb not null,
  created_at timestamptz not null default now()
);
```

Quick technical sketch:

```python
class LineageService:
    def record_relationship(self, parent_id: str, child_id: str, edge_type: str, source_event_id: str) -> None:
        # Upsert by operation key / source_event_id to keep writes idempotent.
        pass

    def get_full_history(self, object_id: str) -> dict:
        return {
            "audit_events": [],
            "upstream_objects": [],
            "downstream_objects": [],
        }
```

## 4. Versioned Config / Rollout System

### Classic Primer Version

- design a feature flag system
- design a config service

### Modern Version

- design a versioned control plane that supports staged rollout, compatibility checks, and in-flight work

### What Matters Now

- explicit versioning
- staged rollout
- applicability rules
- compatibility checks
- rollback that is sometimes asymmetric

### Default Modern Architecture

- config / definition version store
- rollout planner
- validation layer
- runtime resolution service
- audit trail of effective versions actually used

### Good Tradeoffs To Mention

- latest config vs bound version
- hard cutover vs mixed-version support
- dynamic lookup vs pre-binding to execution instances

### Common Interview Mistake

Treating rollout as “push the newest config everywhere.”

### Anduril Mapping

- engineering change rollout
- routing revision activation
- instruction/test/BOM version control

### Worked Solution

Example prompt:

- design a versioned config rollout system for a live platform with in-flight work

How I would work it:

1. Clarify whether old and new versions must coexist.
2. Clarify whether rollout is by environment, tenant, cohort, or execution instance.
3. Assume mixed-version support is required.

Concrete design:

- `DefinitionVersion` stores the new config or workflow version
- `ApplicabilityRule` decides where it applies
- `CompatibilityCheck` validates dependencies before activation
- `ExecutionBinding` records which version each running instance actually used
- a rollout service:
  - validates readiness
  - activates the new version in stages
  - binds new executions to the right version
  - stops future assignment if rollback is required

Storage choice:

- SQL for versions, rollout plans, bindings, and readiness checks
- event stream for notifying downstream systems and rebuilding caches

Why these choices:

- explicit versioning avoids “whatever was current at the time” ambiguity
- applicability rules allow staged rollout
- bindings preserve historical truth for in-flight work
- SQL is a good fit because the control-plane objects are relational and low volume

What I would not do:

- have a single mutable “latest config”
- assume rollback means everything returns to the old state
- activate changes everywhere at once without readiness checks

The answer I want to sound like:

- "I’d treat rollout as a control-plane problem with versioning, applicability rules, staged activation, and explicit execution bindings so that in-flight work remains explainable."

Concrete decisions I would make:

- source of truth: SQL for definition versions, rollout plans, and execution bindings
- activation model: staged rollout by environment / tenant / cohort
- compatibility model: explicit readiness checks before activation
- in-flight work: bind running instances to a concrete version; do not resolve “latest” on every read forever
- rollback: stop future assignment first, then decide what to do about already-bound executions

Schema sketch:

```sql
create table definition_version (
  id uuid primary key,
  definition_name text not null,
  version int not null,
  payload jsonb not null,
  status text not null
);

create table rollout_plan (
  id uuid primary key,
  definition_version_id uuid not null references definition_version(id),
  target_scope jsonb not null,
  status text not null,
  created_at timestamptz not null default now()
);

create table execution_binding (
  execution_id uuid primary key,
  definition_version_id uuid not null references definition_version(id),
  bound_at timestamptz not null default now()
);
```

Quick technical sketch:

```python
class RolloutService:
    def activate(self, version_id: str, target_scope: dict) -> None:
        self._run_compatibility_checks(version_id, target_scope)
        self._mark_rollout_active(version_id, target_scope)

    def resolve_version(self, execution_context: dict) -> str:
        existing = self._load_binding(execution_context["execution_id"])
        if existing:
            return existing
        chosen = self._match_applicability_rule(execution_context)
        self._bind(execution_context["execution_id"], chosen)
        return chosen
```

## 5. Policy Enforcement / Exception Workflow

### Classic Primer Version

- design approval workflow
- design fraud detection review flow

### Modern Version

- design a system that blocks risky actions, routes exceptions for review, and supports explicit release or remediation

### What Matters Now

- enforcement in APIs, not just the UI
- clear blocked states
- conservative containment
- review and disposition workflow
- blast radius when the root issue is shared

### Default Modern Architecture

- policy engine
- exception state store
- review workflow
- enforcement hooks in write APIs
- audit trail of every decision

### Good Tradeoffs To Mention

- auto-block vs review-first
- strict enforcement vs user productivity
- centralized policy engine vs embedded domain rules

### Common Interview Mistake

Designing only notification and review, without actual enforcement.

### Anduril Mapping

- quality hold
- rework
- release / scrap / use-as-is

### Worked Solution

Example prompt:

- design a policy enforcement and exception workflow for blocking risky actions and routing review

How I would work it:

1. Clarify whether enforcement must happen in the API or only in the UI.
2. Clarify whether one bad input can affect many downstream objects.
3. Assume API-level enforcement and possible blast radius.

Concrete design:

- a policy engine evaluates risky conditions
- when violated, it creates an `ExceptionRecord`
- an `ActiveBlock` table or projection is consulted by write APIs
- a review workflow handles:
  - pending investigation
  - approved override
  - remediation required
  - permanently rejected
- if the root cause is shared, lineage lookups compute impacted entities

Why these choices:

- blocking only in the UI is not safe enough
- explicit exception states make review and release auditable
- API-level enforcement prevents accidental forward progress
- lineage integration supports blast-radius containment

What I would not do:

- rely only on notifications
- let reviewers mutate history without a decision record
- mix enforcement logic ad hoc inside every service without a shared policy concept

The answer I want to sound like:

- "I’d design for fast containment first, then explicit review and release, with API-level enforcement so blocked entities cannot move forward accidentally."

Concrete decisions I would make:

- source of truth: SQL for exceptions, blocks, and decisions
- enforcement: write APIs consult an `active_block` projection before allowing progression
- severity model: some violations warn, others block immediately
- review model: every release or override requires an auditable decision record
- blast radius: optional integration with lineage if the violation comes from a shared input

Schema sketch:

```sql
create table exception_record (
  id uuid primary key,
  entity_type text not null,
  entity_id text not null,
  policy_name text not null,
  severity text not null,
  status text not null,
  payload jsonb not null,
  created_at timestamptz not null default now()
);

create table active_block (
  entity_type text not null,
  entity_id text not null,
  exception_id uuid not null references exception_record(id),
  primary key (entity_type, entity_id)
);

create table disposition_decision (
  id uuid primary key,
  exception_id uuid not null references exception_record(id),
  decision text not null,
  decided_by text not null,
  notes text,
  created_at timestamptz not null default now()
);
```

Quick technical sketch:

```python
class PolicyEnforcer:
    def can_write(self, entity_type: str, entity_id: str) -> bool:
        return not self._has_active_block(entity_type, entity_id)

    def handle_violation(self, entity_type: str, entity_id: str, policy_name: str, severity: str) -> str:
        exception_id = self._create_exception(entity_type, entity_id, policy_name, severity)
        if severity in {"high", "critical"}:
            self._activate_block(entity_type, entity_id, exception_id)
        return exception_id
```

## 6. Event Pipeline / Notifications

### Classic Primer Version

- design a notification system
- design pub/sub

### Modern Version

- design a resilient event distribution pipeline for operational changes, alerts, and downstream consumers

### What Matters Now

- durable eventing
- consumer isolation
- retries and dead-letter handling
- subscriber-specific delivery semantics
- deduplication and idempotent consumers

### Default Modern Architecture

- source systems emit canonical events
- message bus or log backbone
- consumer groups for independent downstream workflows
- notification service for user-visible alerts
- delivery tracking and retry logic

### Good Tradeoffs To Mention

- at-least-once vs exactly-once semantics
- push vs pull delivery
- low-latency fanout vs durability

### Common Interview Mistake

Ignoring retries, duplicates, and downstream failures.

### Anduril Mapping

- station alerts
- supervisor notifications
- downstream sync to quality, analytics, deployment, or support systems

### Worked Solution

Example prompt:

- design an event pipeline that distributes operational updates and user-visible notifications

How I would work it:

1. Clarify whether events are only for internal systems or also for users.
2. Clarify delivery guarantees and acceptable delay.
3. Assume internal consumers plus user-facing alerts.

Concrete design:

- source systems emit canonical events into Kafka or Kinesis
- consumer groups handle:
  - analytics updates
  - search indexing
  - policy checks
  - notification fanout
- notification service applies routing rules by user, role, and channel
- failed deliveries go through retry and dead-letter handling
- consumers are idempotent using event IDs or operation keys

Why these choices:

- one durable event backbone decouples producers from consumers
- consumer isolation prevents one bad downstream service from blocking others
- retries and DLQs are mandatory for real operational systems
- notification fanout is different from system-of-record eventing, so it deserves its own service

What I would not do:

- send direct synchronous webhooks from every producer
- assume exactly-once everywhere
- mix user notification formatting into the core event producers

The answer I want to sound like:

- "I’d use a durable event backbone with isolated consumers, then treat user notifications as a downstream delivery problem with retries, routing, and idempotency."

Concrete decisions I would make:

- event backbone: Kafka if the org already runs it well, Kinesis if we are all-in on AWS and want less operational burden
- delivery model: at-least-once, with idempotent consumers
- retries: exponential backoff and dead-letter queue for poison events
- user notifications: separate service from the core event bus consumers
- event shape: canonical envelope with stable event ID and versioned payload

Event envelope sketch:

```json
{
  "event_id": "uuid",
  "event_type": "unit_blocked",
  "source": "quality-service",
  "entity_type": "unit",
  "entity_id": "unit-123",
  "occurred_at": "2026-04-25T12:00:00Z",
  "payload_version": 1,
  "payload": {
    "reason": "failed_test"
  }
}
```

Quick technical sketch:

```python
class NotificationConsumer:
    def handle(self, event: dict) -> None:
        dedupe_key = event["event_id"]
        if self._already_processed(dedupe_key):
            return

        recipients = self._resolve_recipients(event)
        for recipient in recipients:
            self._send(recipient, event)

        self._mark_processed(dedupe_key)
```

## 7. Search And Query Over Operational Data

### Classic Primer Version

- design search

### Modern Version

- design search for entities with rich filtering, recent state, and history-aware queries

### What Matters Now

- transactional source of truth
- read-optimized search index
- eventual consistency between source and index
- faceting, filtering, and permission-aware results

### Default Modern Architecture

- operational DB as source of truth
- CDC or event-driven indexing path
- search index for query-heavy use cases
- detail API that falls back to source-of-truth records

### Good Tradeoffs To Mention

- SQL filtering vs dedicated search index
- sync indexing vs async indexing
- search relevance vs exact operational querying

### Common Interview Mistake

Moving too much truth into the search engine.

### Anduril Mapping

- find a unit
- find affected work orders
- search quality issues
- query by revision, operator, station, or serial

### Worked Solution

Example prompt:

- design search over operational data with filters, recent state, and history-aware queries

How I would work it:

1. Clarify whether this is keyword search, exact lookup, faceted filtering, or all three.
2. Clarify whether search is a convenience layer or a source of operational truth.
3. Assume search is for fast lookup and filtering, not authoritative truth.

Concrete design:

- SQL remains the transactional source of truth
- CDC or event-driven indexing updates an OpenSearch index
- the index stores:
  - key identifiers
  - denormalized metadata
  - current summary state
- search APIs support:
  - keyword search
  - faceted filtering
  - sorting by recency, severity, status
- detail views fetch authoritative records from SQL when precision matters

Why these choices:

- operational search wants flexible filtering and fast response
- OpenSearch is strong for faceted operational queries
- SQL is still better for exact truth and transactional joins
- async indexing is a reasonable tradeoff for this kind of UX

What I would not do:

- make the search index the only place current truth lives
- block writes on indexing
- pretend search results are always perfectly fresh

The answer I want to sound like:

- "I’d keep SQL as the source of truth, build an async search index for fast operational queries, and use detail APIs to pull exact records when correctness matters more than search speed."

Concrete decisions I would make:

- source of truth: Postgres or Aurora Postgres
- index: OpenSearch for faceted filtering and keyword search
- indexing path: CDC or event-driven async indexing
- consistency model: eventual consistency is acceptable for search, but detail APIs fall back to SQL
- permissions: enforce user scope in the search query layer, not only in the UI

Schema sketch:

```sql
create table operational_entity (
  id uuid primary key,
  entity_type text not null,
  status text not null,
  owner_id text,
  metadata jsonb not null,
  updated_at timestamptz not null
);
```

Index document sketch:

```json
{
  "id": "unit-123",
  "entity_type": "unit",
  "status": "blocked",
  "serial_number": "SN-00123",
  "operator_id": "op-17",
  "revision": "rev-4",
  "updated_at": "2026-04-25T12:00:00Z"
}
```

Quick technical sketch:

```python
class Indexer:
    def handle_entity_updated(self, entity: dict) -> None:
        document = {
            "id": entity["id"],
            "entity_type": entity["entity_type"],
            "status": entity["status"],
            "updated_at": entity["updated_at"],
            **entity["metadata"],
        }
        self._index_document(document)
```

## A Good Default Answer Shape

If you get a generic systems prompt, use this sequence:

1. Clarify users and workflow.
2. Define the core entities.
3. Define the write path.
4. Define the read path.
5. Choose storage.
6. Explain async boundaries.
7. Call out failure modes.
8. Add rollout / observability / permissions if relevant.

That is more useful for your loop than trying to remember every old-school internet-scale pattern.

## Best Study Order

If you only have time for a few:

1. Workflow / task execution platform
2. Real-time operational dashboard
3. Versioned config / rollout system
4. Audit trail / lineage system
5. Policy enforcement / exception workflow

That set gives you the most coverage for both:

- generic system design
- Anduril-shaped operational software design
