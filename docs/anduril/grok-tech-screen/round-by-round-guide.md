# Round-By-Round Guide

This doc turns the loop into a simple question:

- what does each interviewer most likely want to see?
- what would make me look strong?
- what would make me look weak?

Your schedule is:

- Thursday, April 30, 2026
  - Systems Design with Jackson Booth
  - Product / Customer Focus Behavioral with Cesar Cabrera
- Friday, May 1, 2026
  - Behavioral Project Deep Dive with Abel Jara
  - Full Stack Tech with Jacob Tobin

## Overall Through-Line

The loop does not look like a random collection of interviews.

It looks like Anduril is testing whether you can be a strong engineer in a domain where:

- the software is internal but mission-critical
- the users are operators, technicians, and manufacturing teams
- the systems are messy and operational
- coding ability still matters
- design has to cash out in reality

So across the whole loop, the strongest meta-signal is:

- calm, grounded, practical technical judgment

The main anti-signal is:

- sounding abstract, generic, or detached from real users and real constraints

## 1. Systems Design With Jackson Booth

## What They Probably Want To See

- you can structure an open-ended problem fast
- you ask good clarifying questions
- you identify the right entities and workflows
- you understand live operational constraints
- you can make reasonable tradeoffs without overcomplicating the system

Because the same HackerRank link is being used here, I would assume they want a typed, structured design discussion:

- assumptions
- entities
- APIs
- writes
- reads
- state transitions
- failure modes
- rollout and operational concerns

## What Strong Looks Like

- start by clarifying users and workflow
- separate definition-time and execution-time data
- preserve auditability and traceability
- explicitly mention mixed revisions, rework, and quality holds
- keep the operator path simple
- show awareness that factories do not stop for architectural purity

Good phrases:

- "I want to understand who is acting in the system and what the unit of work is."
- "I’d separate what should happen from what actually happened."
- "I’d use append-only execution history with read models for operator and supervisor views."
- "I’d design for mixed revisions and in-flight work rather than assuming atomic cutover."

## What Weak Looks Like

- jumping straight into services without defining workflow
- giving a generic SaaS architecture with no factory-specific nuance
- assuming current mutable state is enough
- forgetting quality, genealogy, or rollout safety
- talking only about scale, not operational correctness

## Likely Prompt Shapes

- design an MES for work orders, stations, and serialized units
- design genealogy / traceability
- design real-time factory visibility
- design engineering change rollout
- design quality hold and rework

## Best Prep Material

- [Manufacturing Crash Course](./design/manufacturing-crash-course.md)
- [MES For Mixed-Model Production](./design/mes-for-mixed-model-production.md)
- [Traceability And Genealogy](./design/traceability-and-genealogy.md)
- [Engineering Change Rollout](./design/engineering-change-rollout.md)

## 2. Product / Customer Focus Behavioral With Cesar Cabrera

## What They Probably Want To See

- you know how to build for internal customers
- you do not confuse "customer focus" with consumer product polish
- you can discover the real problem under noisy requests
- you can balance speed, correctness, usability, and operational pain

Given Cesar’s public background in quality/reliability-facing business systems, I would expect a strong focus on:

- internal users
- operator pain
- process friction
- ambiguous requirements
- feedback loops

## What Strong Looks Like

- stories where you translated messy stakeholder pain into software
- examples of changing your mind after learning from users
- examples of simplifying a workflow for non-experts
- examples of pushing back when a request was wrong or incomplete
- care for adoption, usability, and operational effect

Good framing:

- "I try to understand the workflow before I optimize the tool."
- "I look for where the user is paying the complexity tax."
- "I distinguish between the request I heard and the actual problem to solve."

## What Weak Looks Like

- talking like product work is just ticket intake
- telling stories where users are obstacles rather than signal
- overfocusing on features and underfocusing on outcomes
- sounding dismissive of non-technical users
- never changing course based on feedback

## Story Themes To Prepare

- ambiguous stakeholder request
- internal workflow simplification
- operational pain point you diagnosed
- conflicting stakeholder priorities
- fast shipping under real constraints

## 3. Behavioral Project Deep Dive With Abel Jara

## What They Probably Want To See

- you actually built meaningful things
- you know your architecture in detail
- you can explain tradeoffs and failure modes
- your ownership claims survive scrutiny

This round is likely where vagueness gets punished.

They will probably probe:

- what exactly did you own?
- what was hard technically?
- why did you make that design choice?
- what went wrong?
- what would you do differently now?

## What Strong Looks Like

- clear scope and personal ownership
- strong recall of architecture and decisions
- one or two real hard tradeoffs
- one failure or surprise handled honestly
- outcomes tied to your decisions

A strong project explanation usually covers:

1. context
2. problem
3. your role
4. architecture
5. major technical tradeoff
6. issue or incident
7. outcome
8. lessons learned

## What Weak Looks Like

- hiding behind team language the whole time
- describing a project only at the product layer
- inability to explain why the system was designed that way
- pretending nothing went wrong
- fuzzy ownership

## Best Way To Prep

Prepare two projects:

- one systems / backend / operational project
- one full-stack / user-facing / workflow-heavy project

For each, rehearse:

- 2-minute version
- 5-minute version
- 10-minute deep dive

## 4. Full Stack Tech With Jacob Tobin

## What They Probably Want To See

- you can still code cleanly under time pressure
- you can model state and workflow clearly
- you can reason across frontend and backend concerns
- you are not only a systems talker

Because this is labeled `Full Stack Tech` and not just `coding`, I would expect something more applied than pure LeetCode.

Possibilities:

- practical implementation problem
- data modeling or stateful object
- workflow or API-ish reasoning
- a problem with frontend or product flavor
- maybe one medium-style problem plus follow-ups

## What Strong Looks Like

- quick pattern recognition
- simple, readable implementation
- good variable naming
- clear explanation of state and invariants
- ability to extend the solution when asked

If it becomes more product-shaped, strong answers will also:

- think about inputs and outputs clearly
- clarify edge cases
- keep the design modular

## What Weak Looks Like

- treating every problem like abstract DSA theater
- overengineering
- getting lost in framework trivia
- not testing the code mentally
- unclear state transitions

## Best Prep Material

- [Solved Tech Screen Problems](./problems/README.md)
- [Likely Problem Pool](./likely-problem-pool.md)
- [45-Minute Screen Strategy](./screen-strategy.md)

## Round-Specific Failure Modes

### Systems Design

- overly generic architecture
- no operator/user model
- no audit/traceability story

### Product / Customer Focus

- no empathy for internal users
- no evidence of discovery or iteration

### Project Deep Dive

- shaky ownership
- shallow technical recall

### Full Stack Tech

- fancy but brittle code
- weak communication while coding

## What You Want The Whole Loop To Add Up To

By the end, the team should feel:

- Patrick can code
- Patrick can design systems that touch reality
- Patrick can learn a new domain quickly
- Patrick can work with internal customers and operators
- Patrick is senior enough to bring order to messy operational software

That is the real win condition.
