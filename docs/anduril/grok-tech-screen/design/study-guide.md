# Design Study Guide

This guide is for the full-loop design portion, not the HackerRank.

If you have done backend, internal tools, cloud systems, or workflow-heavy products, the main challenge is not "can I design systems?"

It is:

- can I translate those instincts into manufacturing software language?

If this domain feels foreign, read [Manufacturing Crash Course](./manufacturing-crash-course.md) first.

If the interview arc feels slippery, read [System Design Arc](./system-design-arc.md) too. That is the practical conversation flow.

## The Core Mental Shift

Most software domains let you treat the world as mostly digital.

Manufacturing software does not.

Here the software is attached to:

- physical parts
- stations
- operators
- tools
- test benches
- inventory
- quality gates
- shipping and deployment reality

That means the system has to care about:

- what was supposed to happen
- what actually happened
- what can no longer be undone
- what must be auditable later

In other words:

- this is not just CRUD
- this is operational state with physical side effects

## What Feels Different From Typical Backend Work

If you come from cloud or SaaS, the weirdest parts are usually:

### Physical Irreversibility

In many software systems, a bad write can be corrected later.

In manufacturing:

- a hole may already be drilled
- adhesive may already be cured
- a part may already be consumed
- a unit may already be shipped

So "rollback" often really means:

- stop further propagation
- quarantine affected work
- create compensating actions

### Human-In-The-Loop Reality

Your system is not just coordinating services.

It is coordinating:

- operators
- supervisors
- technicians
- inspectors
- machines

That means the workflow model matters as much as the database model.

### Local Correctness Beats Architectural Purity

Factories reward systems that keep the line safe and moving.

So a boring but resilient solution is often better than a fancy architecture that introduces uncertainty during live execution.

### Audit And Traceability Are Not "Enterprise Fluff"

They are operational necessities.

If something goes wrong, the system must explain:

- what happened
- when
- where
- to which units
- under which revision

## The Vocabulary You Should Be Comfortable With

### Product Definition

- `BOM`: the part structure for what should be built
- `routing`: the ordered steps required to build it
- `revision`: versioned definition of product, work instructions, tests, or process

### Execution

- `work order`: request to build units of a configuration
- `unit` / `serial`: the actual thing being built
- `WIP`: work in progress
- `station`: where a step is executed
- `traveler`: the execution record that moves with the unit

### Quality

- `nonconformance`: something failed spec
- `hold`: block a unit, lot, or process from moving forward
- `rework`: corrective path
- `scrap`: unrecoverable unit or component

### Inventory / Traceability

- `lot-tracked`: a batch of material
- `serial-tracked`: unique item-level identity
- `genealogy`: which exact components, lots, operators, and tests contributed to a unit

## The System Shapes That Matter

### 1. Definition-Time Versus Execution-Time Data

This distinction is extremely important.

Definition-time data is:

- the plan
- the product structure
- the routing
- the work instructions
- the approved test procedure

Execution-time data is:

- what the operator actually did
- what station the unit actually visited
- what part lot got consumed
- what test result was recorded
- what failed and when

A strong answer usually separates these clearly.

### 2. Append-Only History Plus Read Models

In this domain, mutable current state is not enough.

You almost always want:

- append-only execution history
- projections or read models for the current operator view

Why:

- auditability matters
- root-cause analysis matters
- quality investigations matter
- you need to know both current state and how it got there

### 3. Mixed Reality And Imperfect Rollouts

Factories do not change atomically.

You should assume:

- some lines are on old revision
- some units are already in progress
- some stations are temporarily down
- some tooling is not yet updated
- humans can and will make input mistakes

Design answers that assume perfect synchronized rollout will feel naive.

### 4. Operator Experience Matters

The users are often:

- technicians
- supervisors
- manufacturing engineers
- quality engineers

That means:

- the UI must be low-friction
- error messages must be actionable
- critical actions need confirmation and audit
- degraded mode matters

## The Questions You Should Ask In The Interview

When a design prompt lands, clarify:

1. What is the actual user workflow?
2. What is the unit of execution: part, lot, station, work order, or serialized unit?
3. What must be auditable later?
4. What are the highest-risk failure modes?
5. Is the priority throughput, traceability, flexibility, or low latency?
6. Does the factory need to keep running during rollout or outage?

These questions make you sound grounded instead of generic.

## A Practical Way To Drive The Conversation

The easiest mistake in system design is jumping too fast into tools.

A better rhythm is:

1. understand the workflow
2. define requirements
3. name the entities
4. sketch the high-level pieces
5. walk the main flows
6. then bring in concrete stack choices

That is where your actual experience should come in.

For example:

- use SQL if the system of record is relational and join-heavy
- use OpenSearch for fast search or operational querying, but not as the source of truth
- use Kinesis if the system is AWS-heavy and you want lower operational overhead
- use Kafka if ecosystem flexibility or existing org expertise matters more
- use ECS/Fargate if you want a straightforward service deployment story in AWS

Those choices sound strong when they are tied to requirements, not when they appear too early.

## The Default Design Moves That Usually Help

### Use Event History For Execution

Examples:

- station entered
- station completed
- material consumed
- test passed
- test failed
- hold placed
- hold released
- rework started

Then derive current state through read models.

### Version Definitions Explicitly

Examples:

- BOM revision
- routing revision
- instruction revision
- test revision

You want to be able to answer:

- what definition was active when this unit was built?

### Design For Reconciliation

Upstream systems will disagree.

Examples:

- ERP says material is available
- WMS says it is quarantined
- MES says it was already consumed

A senior answer includes reconciliation paths, not just happy-path writes.

### Prefer Idempotent Station Actions

Factory integrations are messy.

Retries happen.

So actions like:

- start step
- submit test result
- consume material
- complete station

should be idempotent or deduplicated by operation key.

### Prefer SQL By Default For Core Operational Truth

For most of these Anduril-shaped problems, I would default to:

- relational storage for core transactional state

Why:

- workflows are relational
- audit trails are relational
- joins across units, work orders, revisions, stations, and quality events are common
- correctness is usually more important than extreme scale

I would reach for DynamoDB or another key-value store only when:

- the access patterns are extremely simple and stable
- the object model is naturally document-shaped
- I need very high write throughput on append-only event or projection data

So if an interviewer asks "SQL or DynamoDB?", a strong default answer is:

- SQL for the system of record
- maybe key-value or stream-oriented storage for derived views, projections, or very high-volume event ingestion

## What Anduril Probably Cares About Most

My read from their role descriptions is that they want people who can connect:

- software design
- operational throughput
- real users on the floor
- live production constraints

So the highest-signal themes to emphasize are:

- throughput
- flexibility
- traceability
- uptime
- safe change rollout
- cross-system integration

## How To Sound Strong

Good phrases:

- "I’d separate the product definition model from execution records."
- "I want append-only operational history and read-optimized projections."
- "I’d design for mixed revisions because the plant will not flip atomically."
- "Quality and genealogy are first-class here, not side tables."
- "I’d keep the operator workflow simple and move complexity behind the scenes."
- "The control plane and the execution plane should be related but not conflated."

## How To Use The Mock Designs

For each design note:

1. Read the prompt only.
2. Spend `10-15` minutes sketching your own answer.
3. Compare your structure with the worked solution.
4. Practice saying the tradeoffs out loud.

The win condition is not to memorize my answer.

It is to make your own answer feel inevitable and grounded.
