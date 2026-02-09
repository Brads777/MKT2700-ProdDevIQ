# ProdDevIQ — AI-Augmented Product Development Pipeline

**MKT2700 Product Design & Development • Northeastern University • Spring 2026**

## What's in this package

```
ProdDevIQ/
├── README.md               ← You are here
├── CLAUDE.md               ← Claude Code project config (auto-detected)
├── assignment.md            ← The 7-Phase Product Lab assignment
├── skills/                  ← Pipeline skill files (upload to Claude.ai Project)
│   ├── orchestrator.md      ← Master orchestrator (set as Project Instructions)
│   ├── phase-1-strategic-foundation.md
│   ├── phase-2-rubric-creation.md
│   ├── phase-3-concept-discovery.md
│   ├── phase-4-deep-research.md
│   ├── phase-5-concept-evaluation.md
│   ├── phase-6-refinement-specification.md
│   ├── phase-7-prd-generation.md
│   ├── llm-council-protocol.md
│   ├── prd-presentation-SKILL.md
│   └── DEPLOYMENT.md
├── scripts/
│   └── llm_council.py       ← LLM Council helper (Gemini API automation)
├── guides/
│   ├── getting-started.md    ← START HERE — setup walkthrough
│   ├── gemini-api-setup.md   ← Detailed Gemini API key setup
│   └── notebooklm-setup.md   ← NotebookLM research workflow
├── .claude/
│   └── mcp.json              ← NotebookLM MCP config (Claude Code auto-detects)
└── requirements.txt           ← Python dependencies (pip install -r requirements.txt)
```

**Videos** are on Canvas (Files > ProdDevIQ > videos) — too large for GitHub.

## Quick Start

### Option A: Clone with Git (recommended)
```bash
git clone https://github.com/Brads777/MKT2700-ProdDevIQ.git
cd MKT2700-ProdDevIQ
pip install -r requirements.txt
```

### Option B: Download ZIP
Click the green **"Code"** button above → **"Download ZIP"** → unzip to a folder on your computer.

### Then:
1. Watch both required videos on Canvas (Files > ProdDevIQ > videos)
2. Read `guides/getting-started.md`
3. Set up your accounts (Claude Pro, Gemini API, NotebookLM, Perplexity Pro)
4. **Claude.ai:** Create a Project → paste `skills/orchestrator.md` as Custom Instructions → upload all other skill files to Project Knowledge
5. **Claude Code:** Run `claude` from this directory — it auto-detects the pipeline
6. Say **"Start project"** to begin

## Questions?

Post in the Canvas discussion forum or attend Thursday Zoom Syncs (7:00-8:00 PM EST).
