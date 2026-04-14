# 45-Minute Screen Strategy

If the format really is:

- `45` minutes
- `2` Medium problems

then this is not just an algorithms test.

It is also a pacing and composure test.

## The Main Rule

Do not try to look clever.

Try to look:

- fast to orient
- calm
- correct
- easy to trust

That is the profile that usually wins short screening rounds.

## Target Pacing

### Problem 1

Goal:

- finish in `12-18` minutes

That means:

- identify the pattern fast
- say the brute force briefly
- move quickly to the standard solution
- code without over-talking

### Problem 2

Goal:

- finish or mostly finish in `20-25` minutes

This is where the stronger Medium usually lands.

The winning behavior is:

- classify the shape quickly
- name the invariant
- keep the implementation organized
- narrate edge cases before the interviewer asks

### Final Buffer

Leave `3-5` minutes for:

- one dry run
- complexity statement
- any follow-up or cleanup question

## How To Start Each Problem

Use the same structure every time:

1. Restate the problem in your own words.
2. Name the likely pattern family.
3. Mention the brute force.
4. Say the optimized approach and why it fits.
5. Code.

This keeps you from thrashing and also makes you sound senior and composed.

## Category-Specific Reminders

### If It Is A Grid Problem

Ask yourself:

- is this connected components?
- is this shortest path?
- is this spread over time?
- do I need DFS, BFS, or multi-source BFS?

### If It Is A Matrix Traversal Problem

Ask yourself:

- what state defines where I am?
- what invariant keeps the traversal correct?
- can I write the boundary updates before coding?

### If It Is A Stack Problem

Ask yourself:

- what unresolved items am I storing?
- why do I need indices instead of values?
- what monotonic property am I maintaining?

### If It Is A String / Hash Problem

Ask yourself:

- what is the canonical key?
- what am I grouping or counting?
- can I explain the mapping cleanly in one sentence?

## Interview Behavior That Helps

- Say the pattern name early.
- Name time and space complexity after coding.
- Use one small example out loud before finalizing.
- If you get stuck, re-classify the problem instead of blindly patching.

## Interview Behavior That Hurts

- silent thrashing
- over-abstracting
- trying to invent something new under time pressure
- spending five minutes on variable naming before the core logic exists

The best screen answers usually look more like disciplined Medium execution than brilliance.
