# MKT2700 — AI-Augmented Product Development Pipeline

## Project Overview

This is the ProdDevIQ pipeline for MKT2700 Product Design & Development at Northeastern University. It guides student teams through a 7-phase product development process from Strategic Foundation to PRD Generation.

**Read `skills/orchestrator.md` first** — it contains the full pipeline specification, phase sequence, decision gates, and startup instructions.

## How This Works

When a student says "Start project" or "Begin Phase N":
1. Read the orchestrator skill at `skills/orchestrator.md`
2. Read the corresponding phase skill at `skills/phase-N-*.md`
3. Follow the phase instructions exactly — ask questions one at a time, produce the required artifact
4. At LLM Council checkpoints, instruct the student to run `scripts/llm_council.py`

## Pipeline Phases

| Phase | Skill File | Output |
|-------|-----------|--------|
| 1 | `skills/phase-1-strategic-foundation.md` | `strategic-brief.md` |
| 2 | `skills/phase-2-rubric-creation.md` | `evaluation-rubric.md` |
| 3 | `skills/phase-3-concept-discovery.md` | `concept-candidates.md` |
| 4 | `skills/phase-4-deep-research.md` | `research-repository.md` |
| 5 | `skills/phase-5-concept-evaluation.md` | `evaluation-results.md` |
| 6 | `skills/phase-6-refinement-specification.md` | `refined-concept.md` |
| 7 | `skills/phase-7-prd-generation.md` | `product-requirements-document.md` |

## LLM Council

4 checkpoints use `scripts/llm_council.py` with Gemini API:
- Phase 2: `--checkpoint rubric`
- Phase 5: `--checkpoint scoring`
- Phase 6: `--checkpoint kano`
- Phase 7: `--checkpoint prd-review`

See `skills/llm-council-protocol.md` for the full reconciliation protocol.

## Key Rules

- Never let students score concepts before weighting rubric criteria
- Enforce decision thresholds: <90% kill, 90-95% revise, >95% continue
- Every phase must produce a saved artifact before the next phase begins
- Deadline: Sunday, February 15, 2026 (extended: Tuesday, February 17)
