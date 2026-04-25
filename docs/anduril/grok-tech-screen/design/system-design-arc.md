# System Design Arc

This is the simple, non-robotic arc to keep in your head during the interview.

It is not a script.

It is a way to keep the conversation moving in a strong direction without sounding like you memorized a framework.

## The Arc

### 1. Understand The Situation

Start by getting grounded in:

- who the users are
- what they are trying to do
- what the unit of work is
- what matters most in this system

Good questions:

- who is using this system day to day?
- what is the most important workflow?
- what hurts most if this system is wrong or slow?
- what matters more here: latency, throughput, correctness, auditability, or speed to ship?

This helps you sound like you care about reality, not just architecture.

What these questions are really doing:

- "who is using this system?" means "whose life gets easier or harder based on this design?"
- "what is the most important workflow?" means "what is the one path I absolutely cannot get wrong?"
- "what hurts most if this system is wrong or slow?" means "what failure should shape my design the most?"
- "what matters more?" means "what tradeoff should I optimize for instead of pretending everything matters equally?"

So clarifying questions are not there to look smart.

They are there to stop you from solving the wrong problem.

### 2. Turn The Prompt Into Clear Requirements

Once you understand the context, say it back in your own words.

Then split the problem into:

- functional requirements
- non-functional requirements

For example:

- what the system must do
- how fast it must be
- how reliable it must be
- what must be auditable
- what kind of rollout or failure constraints exist

### 3. Name The Core Entities Early

Before diving into infrastructure, define the nouns.

Examples:

- workflow
- execution instance
- event
- revision
- hold
- unit
- station

If the nouns are clean, the design usually gets easier fast.

### 4. Sketch The High-Level System

Now you can introduce the major pieces:

- client or UI
- API / service layer
- storage
- queue / stream / async path
- read models or cache
- integrations

This is where you should explain:

- the main write path
- the main read path

### 5. Walk One Or Two Important Flows

Do not stay too static.

Pick the core actions and walk them through:

- user submits an action
- API validates it
- data is written
- an event is emitted
- projections or downstream systems update

This is where the design starts feeling alive.

### 6. Use Your Real Experience

Now bring in practical choices.

Examples:

- if we want speed and we are already deep in AWS, I’d probably use CDK and ECS/Fargate rather than inventing a custom deployment story
- if the system of record is relational and the workflow is join-heavy, I’d default to SQL
- if we need streaming inside AWS with lower operational overhead, Kinesis might be a reasonable first choice
- if we need fast operational querying over denormalized documents, OpenSearch could help, but I would not make it the source of truth

The key is:

- choose tools because they fit the constraints
- not because they are your favorite stack

### 7. Talk About Failure And Tradeoffs

This is where seniority shows up.

Ask:

- what happens if writes are duplicated?
- what happens if a downstream system is slow or unavailable?
- what happens if data is stale?
- what if rollout is partial?
- what if users need degraded mode?

Then explain the choices you made and what you are trading off.

### 8. Close With Operations

If time allows, finish with:

- observability
- security / permissions
- rollout strategy
- migration path
- testing strategy

That makes the answer feel production-minded.

## A Good Default Speaking Style

Try to sound like:

- "Let me first make sure I understand the workflow and the most important constraints."
- "I think the core entities here are..."
- "At a high level I’d split this into..."
- "Let me walk the main write path first."
- "The main tradeoff I’m making is..."
- "If this were AWS-heavy and we wanted to move quickly, I’d probably start with..."

That sounds natural and practical.

## How To Ask Clarifying Questions Without Sounding Robotic

The goal is not to rattle off five canned questions.

The goal is to ask the minimum set of questions that changes the design.

A natural way to do it is:

- "Before I jump into architecture, I want to make sure I understand the workflow."
- "The main thing that would change the design for me is whether..."
- "One thing I want to clarify is..."

For example, instead of asking:

- "Are we designing for one site or many?"

you can think:

- if this is one site, I can keep the model simpler
- if this is many sites, I probably need site-aware configuration, permissions, rollout, and maybe replication concerns

So a more human way to say it is:

- "One thing that changes the design pretty quickly is whether this is for one location or multiple factories, because multi-site support usually introduces site-level config, rollout, and operational differences."

That is the real point of the question.

## A Good Default Order

If you want one compact version to memorize:

1. users and context
2. requirements
3. entities
4. high-level architecture
5. main flows
6. tech choices
7. tradeoffs and failures
8. operations and rollout

That is enough structure to keep you grounded without making you sound robotic.
