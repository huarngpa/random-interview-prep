# Manufacturing Crash Course For Software Engineers

This is the short version of the domain, written for someone who already knows systems but has not worked in manufacturing.

The goal is not to make you a manufacturing expert.

The goal is to make the design questions feel legible.

## The Simplest Mental Model

A factory is a distributed system with:

- physical state
- human operators
- machines and test benches
- inventory constraints
- irreversible side effects
- strict audit requirements

That means the software stack is not just managing data.

It is coordinating reality.

## Cloud Analogy

If you come from backend or infra, here is the rough translation:

- `work order` = a request to build a batch of real units
- `serialized unit` = a durable object moving through a workflow
- `routing` = a workflow or DAG of required steps
- `station` = a worker node with physical capabilities
- `traveler` = the execution record that follows the unit
- `genealogy` = distributed tracing plus hardware lineage
- `quality hold` = circuit breaker plus quarantine
- `engineering change` = schema and deploy migration with physical consequences
- `rework` = retry path, but not always idempotent or reversible

This is why normal software instincts transfer well, but only if you respect the physical side effects.

## The Three Truths That Matter

### 1. As-Designed Is Different From As-Built

Engineering defines:

- what should be built
- with what parts
- in what order
- under what instructions

The factory produces:

- what actually got built
- with which lots and serials
- at which station
- by which operator
- with what deviations

In manufacturing software, both truths matter.

### 2. History Matters More Than In Typical SaaS

If a customer record changes in SaaS, current state is often enough.

If a unit fails in the field, manufacturing needs to know:

- which components were used
- which lot was installed
- who touched it
- which test bench validated it
- what process revision was active

That is why append-only history and audit trails are so important.

### 3. The Plant Does Not Stop For Elegant Architecture

This is probably the biggest culture shift.

The system has to support:

- line downtime
- partial rollouts
- mixed revisions
- flaky machine integrations
- humans entering bad data
- local workarounds during operational pressure

So answers that assume perfect coordination will sound naive.

## Key Business Systems

### PLM

Product lifecycle management.

Where engineering definitions often live:

- product structures
- revisions
- released drawings or specifications

### ERP

Planning and business system of record.

Common responsibilities:

- purchasing
- accounting-ish flows
- inventory planning
- high-level production planning

### MES

Manufacturing execution system.

This is where the plant actually runs:

- work instructions
- station execution
- operator interaction
- completion tracking
- unit progression

### WMS

Warehouse management system.

Responsible for:

- where inventory physically sits
- picking, receiving, putaway
- movement in and out of storage

### QMS

Quality management system.

Responsible for:

- nonconformances
- investigations
- dispositions
- quality records

In a modern internal platform, these may not be cleanly separate products. Forge and ArsenalOS appear to stitch together or replace large pieces of this stack.

## Terms That Will Keep Coming Up

### BOM

Bill of materials.

The parts structure of a product.

### Routing

The ordered process steps needed to build a product.

### Traveler

The execution record that follows a unit through the line.

### WIP

Work in progress.

Anything partly built and not yet complete.

### Lot

A batch of material produced together.

### Serial

A unique identity for a specific unit or component.

### Nonconformance

Something did not meet spec.

### Rework

Extra work required to correct or disposition a problem.

### Scrap

The unit or material cannot proceed.

## Where The Software Gets Hard

### Mixed Revisions

Some units started on old instructions.

New ones should use new instructions.

Some stations are updated, some are not.

That means the software has to understand applicability, not just "latest version."

### Material Traceability

If a bad component lot is discovered later, you need to answer:

- which units used it?
- where are they now?
- what else must be held?

### Human Factors

Your users are not sitting calmly at a desk all day.

They may be:

- under time pressure
- wearing gloves
- scanning labels
- dealing with station downtime
- handling rework confusion

So the UX bar is different from a generic admin dashboard.

### Synchronous Versus Asynchronous Truth

Operator actions usually need:

- immediate authoritative acknowledgement

Analytics and reporting can often be:

- eventually consistent

That split is important in most of these designs.

## What A Good Design Answer Sounds Like

You do not need to sound like a manufacturing lifer.

You want to sound like a strong systems engineer who understands:

- this is a live operational system
- physical truth matters
- history matters
- rollout is messy
- quality and traceability are first-class
- operator simplicity matters

That is already a very strong posture for this interview.
