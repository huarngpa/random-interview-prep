# Anduril Full-Loop Prep Plan

This doc is the practical answer to:

- how do I prepare for this exact loop?

Your schedule is:

- Thursday, April 30, 2026
  - Systems Design with Jackson Booth
  - Product / Customer Focus Behavioral with Cesar Cabrera
- Friday, May 1, 2026
  - Behavioral Project Deep Dive with Abel Jara
  - Full Stack Tech Interview with Jacob Tobin

The best way to prepare is not to treat these as four unrelated interviews.

They are four different angles on the same question:

- can Patrick build and explain software for messy, real operational environments?

## What Each Round Is Probably Testing

### Systems Design

Primary test:

- can you design operational software for a live factory environment?

Prepare for:

- entity modeling
- workflow/state transitions
- traceability and auditability
- mixed revisions and rollout safety
- operational failure modes

Most relevant docs:

- [Manufacturing Crash Course](./design/manufacturing-crash-course.md)
- [Design Study Guide](./design/study-guide.md)
- [MES For Mixed-Model Production](./design/mes-for-mixed-model-production.md)
- [Traceability And Genealogy](./design/traceability-and-genealogy.md)
- [Engineering Change Rollout](./design/engineering-change-rollout.md)

### Product / Customer Focus Behavioral

Primary test:

- can you build for internal customers with real operational pain?

Prepare for:

- discovering the actual user problem
- handling ambiguous requirements
- balancing speed and correctness
- working with non-engineering stakeholders
- changing direction after learning from users

### Behavioral Project Deep Dive

Primary test:

- did you actually build hard things, and do you understand them deeply?

Prepare for:

- architecture details
- exact role and ownership
- tradeoffs
- incidents or failures
- how you influenced decisions
- what you would change now

### Full Stack Tech

Primary test:

- can you still code clearly and model state well?

Prepare for:

- practical coding
- workflow/state modeling
- data transformations
- API-ish thinking
- possibly some React / TypeScript / backend-flavored reasoning

Keep the existing coding set fresh:

- [Solved Tech Screen Problems](./problems/README.md)

## The Right Prep Strategy

There are four workstreams.

### 1. Design Fluency

Goal:

- be able to answer one Forge / ArsenalOS design prompt clearly in both `5` and `15` minutes

How:

- rehearse one design doc per day
- explain it out loud without notes
- force yourself to name:
  - users
  - entities
  - writes
  - reads
  - state transitions
  - failure modes
  - tradeoffs

### 2. Project Story Depth

Goal:

- have two projects that can survive aggressive drilling

Pick:

- one systems / backend / operational project
- one product / full-stack / user-facing project

For each, prepare:

- context
- problem
- your exact role
- architecture
- hardest technical decision
- hardest people / alignment problem
- incident or failure
- outcome
- what you learned

### 3. Customer / Product Stories

Goal:

- sound like someone who can build for real users, not just code in isolation

Prepare at least six stories:

- ambiguous user need
- stakeholder conflict
- discovered the real problem
- simplified a workflow
- balanced speed vs quality
- handled operational pain or production issues

Best source docs now:

- [Behavioral Focus](../current-loop/behavioral/README.md)

### 4. Coding Sharpness

Goal:

- stay fast enough that the full-stack round feels controlled

Focus on:

- stateful problems
- data transformation
- one or two grid/BFS/simulation problems per week
- one JavaScript / TypeScript implementation session every day or two

## Day-By-Day Prep Template

Use this template for the days leading up to the loop.

### Day A: Systems Heavy

1. Read one design doc.
2. Explain the `5-minute` answer from memory.
3. Explain the `15-minute` answer from memory.
4. Write a one-page skeleton:
   - prompt
   - users
   - entities
   - architecture
   - tradeoffs

### Day B: Behavioral Heavy

1. Practice one project deep dive for `10` minutes.
2. Practice two behavioral stories for `5` minutes each.
3. Tighten any vague parts:
   - what did I personally do?
   - what was hard?
   - what changed because of me?

### Day C: Coding Heavy

1. Solve one medium problem in JavaScript or TypeScript.
2. Solve one Anduril-style grid / simulation / stack problem.
3. Explain the complexity and invariant out loud.

Then rotate.

## The Last 3 Days

Do not keep expanding scope.

Just tighten the highest-value material.

### Must Feel Ready

- one strong systems design answer
- one backup systems design answer
- two project deep dives
- six behavioral stories
- a handful of practical coding patterns

### Should Not Spend Time On

- random hard LeetCode problems
- obscure manufacturing edge cases
- trying to become a domain expert overnight

## Manufacturing-Specific Things To Keep In Mind

You do not need to pretend to be from this world.

You do need to show that you understand the important differences:

- physical side effects matter
- auditability matters
- mixed revisions are normal
- operator UX matters
- factories do not stop for elegant architecture

That is enough to sound serious and grounded.

## How To Sound Good In The Loop

Use language like:

- "I’d separate definition-time data from execution-time data."
- "I’d preserve append-only operational history."
- "I’d design for mixed revisions and in-flight work."
- "I’d optimize the operator path and hide complexity behind the scenes."
- "I’d make quality and genealogy first-class, not afterthoughts."

## Night Before Checklist

- confirm schedule and room setup
- confirm HackerRank environment works
- review `5-minute` design answers
- review project bullets
- review behavioral stories
- stop cramming

## Final Framing

The bar is probably not:

- be a manufacturing veteran

It is more like:

- be a strong engineer who can learn a new domain fast
- reason clearly about live operational systems
- build for real users
- communicate with calm and structure

That is a very winnable bar.
