# Role And People Research

Last updated: April 14, 2026

This note pulls together the public signal around:

- the ArsenalOS / Forge role
- what the job likely looks like in practice
- what can be inferred about the interviewers from public sources

## What You Would Likely Be Doing

The clearest official description comes from Anduril's current and adjacent ArsenalOS / Forge postings.

The recurring pattern is:

- build internal software that powers manufacturing, supply chain, deployment, and sustainment
- spend time on the factory floor, then turn real physical bottlenecks into software solutions
- support high-rate manufacturing of products like Roadrunner and Fury
- build and maintain the digital backbone across systems like MES, ERP, WMS, PLM, and custom internal tools
- create software that helps factories run faster, more reliably, and with better visibility

The strongest direct statements are:

- Forge is "Anduril’s custom supply chain, manufacturing, and deployment mission execution software"
- ArsenalOS is the "system-of-systems" used across supply chain, manufacturing, field maintenance, and other internal business functions
- ProductionOS / ProdOS is the manufacturing and planning subset within ArsenalOS

So the practical translation is:

- not consumer product work
- not generic CRUD web work
- not pure enterprise IT either

It is more like:

- internal platform engineering for physical operations
- factory software
- manufacturing execution workflows
- digital thread and systems integration
- operational visibility and tooling for people building defense hardware

## What The Work Probably Feels Like Day To Day

My best inference from the postings is that the job sits at the intersection of:

- full-stack product engineering
- systems integration
- manufacturing operations
- internal platform leverage

In practice, that probably means a lot of:

- TypeScript / React / NextJS application development
- backend APIs and integrations
- modeling workflows across parts, stations, tools, builds, and deployments
- tying together enterprise systems and custom tools
- debugging production floor issues quickly
- building software that must be correct enough to support live operations, not just demos

The job also appears more operational than many "full stack" roles. Multiple postings emphasize:

- live production environments that cannot stop
- site readiness
- risk and dependency tracking
- first response to new technology integration
- on-call support for production software

So this role likely rewards people who are:

- comfortable near real operations
- fast at translating messy reality into software
- willing to own integration pain
- strong at simplifying workflows for other engineers and operators

## Why These Interview Problems Fit The Job

The coding screen problems are probably not random LeetCode trivia.

They are a cheap way to test whether you naturally think in the shapes this role uses:

### Number of Islands

- can you look at a grid and see hidden connectivity?
- relevant to layouts, zones, and disconnected regions on a factory floor

### Rotting Oranges

- can you model state spread over time?
- relevant to propagation, readiness, contamination, or status rollout across operational systems

### Spiral Matrix

- can you traverse structured state carefully and not get lost?
- relevant to deterministic workflows and ordered scanning of structured data

### Daily Temperatures

- can you maintain an efficient frontier of unresolved items?
- relevant to streaming signals, thresholds, or operational event processing

### Game of Life

- can you reason about synchronous state transitions?
- relevant to simulation, staged updates, and stateful operational tooling

### Group Anagrams

- can you normalize records into a canonical key and group them correctly?
- relevant to indexing, deduping, and operational data hygiene

So the deeper pattern is:

- grids and matrices test physical-layout reasoning
- BFS/DFS test propagation and reachability
- stack problems test ordered event resolution
- hash grouping tests normalization and classification

That is a pretty plausible proxy for software that sits close to manufacturing and deployment reality.

## People Research

### Michael Guberman

Public signal:

- the recruiter outreach you received identifies him as a Senior Technical Recruiter with Anduril

What that likely means:

- Mike is the recruiter and process owner, not a technical evaluator
- his job is likely matching strong full-stack / internal-tools candidates into ArsenalOS and adjacent manufacturing-software roles

### Ryan Chandler

Public signal:

- LinkedIn snippets show Ryan Chandler at Anduril Industries in Costa Mesa
- The Org lists him as `Sr. Manager, Internal Tools`
- The Org description says he has focused on next-generation ERP systems, custom tools, internal timekeeping, and manufacturing execution systems
- a public LinkedIn post snippet says he came from Tesla to Anduril and was hiring for a senior full-stack software engineer on the internal tools team

My inference:

- Ryan is very likely on the business-systems / internal-tools / manufacturing-software side of Anduril
- he is probably a hiring manager or close to that layer
- your hour with Ryan is likely to focus less on puzzle coding and more on:
  - how you think about operational software
  - systems and integration judgment
  - translating messy business reality into software
  - whether you can thrive in a fast, factory-adjacent environment

### Steven Chung

Public signal:

- I was not able to confidently verify the specific Steven Chung from public sources
- the schedule strongly suggests he is the engineer running the HackerRank coding round

My inference:

- treat Steven as a hands-on engineer who will care about:
  - pattern recognition
  - correctness
  - pace under pressure
  - how you explain tradeoffs while coding

I would not overfit a biography here since I could not confidently confirm a public profile.

## Interview Implications

My best read is:

- Ryan round:
  - role fit
  - internal-tools / factory-software judgment
  - systems thinking
  - how you operate with ambiguity and real operational customers

- Steven round:
  - two Medium-style coding problems
  - likely matrix, BFS/DFS, simulation, stack, or hash-map style
  - code quality and explanation matter because the time box is tight

## Sources

- Senior Software Engineer, Full Stack, Anduril: [Greenhouse](https://job-boards.greenhouse.io/andurilindustries/jobs/5036672007)
- Technical Program Manager, Digital Factory Systems: [Greenhouse](https://job-boards.greenhouse.io/andurilindustries/jobs/5088779007)
- Senior Product Manager, Manufacturing and Industrial Design Systems: [Greenhouse](https://job-boards.greenhouse.io/andurilindustries/jobs/5071911007)
- Ryan Chandler public org chart entry: [The Org](https://theorg.com/org/anduril-industries/org-chart/ryan-chandler)
- Ryan Chandler hiring post mention via Cy Sack: [LinkedIn post snippet](https://www.linkedin.com/posts/cyrilsack_senior-software-engineer-activity-7207423634800340992-981h)
- Recruiter title and role details: your outreach email
