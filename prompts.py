"""
Dynamic prompt engine for the Agent Arena.
Provides task-type detection and a single strong composite prompt
that guides the agent to analyze, solve, and submit in one turn.
"""

from typing import Optional

# ── Task type detection ──────────────────────────────────────────────────────
TASK_PATTERNS = {
    "code": [
        "code", "function", "implement", "write a", "program", "script",
        "class", "algorithm", "api", "method", "library", "module", "package",
        "build", "create a", "develop", "application", "service", "endpoint",
    ],
    "debug": [
        "debug", "fix", "error", "bug", "issue", "broken", "fails",
        "exception", "traceback", "crash", "wrong", "incorrect", "not working",
        "repair", "resolve", "troubleshoot",
    ],
    "explain": [
        "explain", "describe", "what is", "how does", "why", "difference between",
        "concept", "theory", "overview", "introduction", "compare", "contrast",
        "elaborate", "clarify", "discuss",
    ],
    "optimize": [
        "optimize", "performance", "efficient", "slow", "bottleneck", "memory",
        "speed", "complexity", "scale", "improve", "faster", "latency",
        "throughput", "resource", "cache", "compress", "reduce",
    ],
    "design": [
        "design", "architecture", "system", "database schema", "pattern",
        "structure", "model", "diagram", "plan", "blueprint", "component",
        "microservice", "flow", "sequence", "entity relationship",
    ],
    "test": [
        "test", "unit test", "pytest", "assert", "coverage", "mock", "testing",
        "tdd", "spec", "validate", "verify", "bdd", "integration test",
        "regression", "benchmark",
    ],
    "data": [
        "data", "csv", "json", "sql", "query", "database", "etl", "pipeline",
        "transform", "clean", "analyze", "visualization", "chart", "pandas",
        "dataframe", "dataset",
    ],
    "security": [
        "security", "auth", "authentication", "authorization", "jwt", "oauth",
        "encrypt", "hash", "vulnerability", "sanitize", "xss", "csrf", "sql injection",
        "penetration", "secure",
    ],
}


def detect_task_type(title: str = "", description: str = "") -> str:
    text = f"{title} {description}".lower()

    scores = {}

    for task_type, keywords in TASK_PATTERNS.items():
        scores[task_type] = sum(1 for kw in keywords if kw in text)

    if not scores:
        return "general"

    top_score = max(scores.values())

    if top_score == 0:
        return "general"

    # Agar sirf ek keyword mila hai to bhi general hi treat karo
    if top_score <= 1:
        return "general"

    return max(scores, key=scores.get)


# ── Prompt templates ─────────────────────────────────────────────────────────

def _format_task(task: dict) -> str:
    lines = [
        f"Title: {task.get('title', 'N/A')}",
        f"Level: {task.get('level', 'N/A')}",
        f"Points: {task.get('points', 'N/A')}",
        f"Difficulty: {task.get('difficulty', 'N/A')}",
        f"Description:\n{task.get('description', 'N/A')}",
    ]
    return "\n".join(lines)


def build_task_prompt(task: dict, agent_id: str, task_id: str) -> str:
    """
    Single composite prompt that instructs the agent to:
      1. Analyze the task deeply
      2. Produce a complete, high-quality solution
      3. Call submit_task with the full solution
    """
    task_type = detect_task_type(task.get("title", ""), task.get("description", ""))

    type_guidance = {
        "code": (
            "Write clean, well-commented code with docstrings, type hints, error handling, "
            "and a brief usage example. Explain key design decisions."
        ),
        "debug": (
            "Identify the root cause, provide the fixed code/config, explain why the fix works, "
            "and suggest prevention strategies."
        ),
        "explain": (
            "Use clear analogies, step-by-step breakdowns, concrete examples, and address "
            "common misconceptions. Structure from simple to complex."
        ),
        "optimize": (
            "Show before/after reasoning, provide the optimized solution, explain performance gains, "
            "and note any trade-offs."
        ),
        "design": (
            "Provide architecture overview, component breakdown, data flow, technology choices "
            "with justification, and scalability/failure considerations."
        ),
        "test": (
            "Provide a complete test suite with setup, positive/negative cases, edge cases, "
            "and mocking strategy where applicable."
        ),
        "data": (
            "Provide the data pipeline/transformation logic, schema, validation checks, "
            "and sample outputs."
        ),
        "security": (
            "Summarize threat model, provide secure code/config, explain defense mechanisms, "
            "and include verification steps."
        ),
        "general": (
            "Provide a complete, well-structured, and thorough solution with examples and reasoning."
        ),
    }

    reasoning_modes = {
    "code": "Think like a senior software engineer. Consider correctness, readability, maintainability, and edge cases.",
    "debug": "Find the root cause first. Never patch symptoms. Verify the fix.",
    "design": "Think about scalability, trade-offs, bottlenecks, reliability, and future extensibility.",
    "security": "Think like an attacker first, then design the defense.",
    "optimize": "Compare before vs after. Justify every optimization with measurable benefits.",
    "test": "Think of happy paths, edge cases, failure cases, and boundary conditions.",
    "data": "Validate assumptions, data quality, schema consistency, and transformation correctness.",
    "general": "Use structured reasoning and provide the most complete answer possible."
   }

    guidance = type_guidance.get(task_type, type_guidance["general"])
    reasoning = reasoning_modes.get(task_type, reasoning_modes["general"])

    return f"""
ROLE:
You are ThirdSight Prime, an autonomous reasoning agent.

MISSION:
Produce the highest quality answer possible.

══════════════════════════════════════

PHASE 1 — PLANNER

- Understand the task.
- Identify explicit requirements.
- Infer hidden requirements.
- List assumptions.
- List edge cases.
- Decide best strategy.

══════════════════════════════════════

PHASE 2 — SOLVER

Produce a complete solution.

Think carefully.

Don't optimize for speed.

Optimize for correctness.

══════════════════════════════════════

PHASE 3 — REVIEWER

Review your own solution.

Ask yourself:

Did I miss anything?

Any edge case?

Any ambiguity?

Can I improve readability?

Can I improve correctness?

If yes,

improve it before submitting.

══════════════════════════════════════

FINAL

Call submit_task()

Never stop before submission.

TASK ({task_type.upper()}):
{_format_task(task)}

REASONING & SOLVING INSTRUCTIONS:
1. ANALYZE — Restate the problem, extract all explicit and implicit requirements, list edge cases and risks, and outline your chosen approach with justification.
2. SOLVE — Produce a complete, production-ready answer. {guidance}
3. REVIEW — Before submitting, mentally verify: correctness, completeness, edge cases, clarity, best practices, and efficiency.
4. REFLECT — Do not submit your first draft. Improve it after reviewing your own work.
5. CONFIDENCE — Estimate whether your answer is complete. If you find weaknesses, fix them before submission.

REASONING & SOLVING INSTRUCTIONS:
REASONING MODE:
{reasoning}
1. ANALYZE ...
2. SOLVE ...
3. REVIEW ...
4. REFLECT ...
5. CONFIDENCE ...

IMPORTANT BEHAVIOR:
- Do not produce the first solution...
- Spend additional reasoning effort...
...
QUALITY CHECKLIST:
✓ Technical correctness
✓ Completeness
✓ Edge cases covered
✓ Clear explanation
✓ Professional formatting
✓ Best practices followed

SELF-REFLECTION:

Before calling submit_task, silently evaluate your own solution.

Ask yourself:

• Did I miss any requirement?
• Are all edge cases handled?
• Is there a simpler or better approach?
• Is every claim technically correct?
• Is the response well structured?

If any answer is "No",

improve the solution before submission.

Only then call submit_task.

Never submit your first draft.

Always improve your answer after reviewing it.

SUBMISSION INSTRUCTIONS:
After your analysis and solution, you MUST call submit_task with:
  agent_id = "{agent_id}"
  task_id  = "{task_id}"
  content  = <your complete final answer (analysis + solution)>

The evaluator rewards:
- Technical correctness
- Depth of reasoning
- Robustness
- Professional structure
- Edge-case handling
- Clarity

Optimize your answer for the highest possible evaluation score.

Do NOT stop after analysis. Do NOT ask for confirmation. Call submit_task in this same turn.
""".strip()
