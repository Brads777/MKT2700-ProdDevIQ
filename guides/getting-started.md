# ©2026 Brad Scheller

# ProdDevIQ — Getting Started Guide
## MKT2700 Product Design & Development • Northeastern University • Spring 2026

### Before You Begin

Watch these two required videos (available on Canvas under Files > ProdDevIQ > videos):
1. **Pipeline Setup Guide** (`MKT2700_Pipeline_Setup_Guide`) — Technical setup walkthrough
2. **AI Pipeline Walkthrough** (`MKT2700_Week5_AI_Pipeline_Walkthrough2`) — Overview of the 7-phase process

### Required Accounts (Set Up Before Phase 1)

| Tool | What It Does | Setup Link | Cost |
|------|-------------|-----------|------|
| **Claude.ai** (Pro) | Primary AI — runs the pipeline | [claude.ai](https://claude.ai) | $20/mo (Pro) |
| **Google AI Studio** | Gemini API for LLM Council | [aistudio.google.com](https://aistudio.google.com) | Free |
| **NotebookLM** | Research notebooks | [notebooklm.google.com](https://notebooklm.google.com) | Free |
| **Perplexity Pro** | Deep research | [perplexity.ai](https://perplexity.ai) | $20/mo (Pro) |

### Step 1: Get Your Gemini API Key (Required)

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key" in the left sidebar
4. Click "Create API Key" → select any Google Cloud project (or create one)
5. Copy the key and save it somewhere safe
6. Set it as an environment variable:
   - **Mac/Linux:** Add to your ~/.bashrc or ~/.zshrc: `export GEMINI_API_KEY="your-key-here"`
   - **Windows:** In PowerShell: `$env:GEMINI_API_KEY="your-key-here"` (this is temporary — closes when you close the terminal. See `guides/gemini-api-setup.md` for permanent setup)

See the [Gemini API Setup Guide](./gemini-api-setup.md) for detailed instructions with screenshots.

### Step 2: Install Python Dependencies

**Prerequisite:** Verify Python is installed by running `python --version` in your terminal. If not installed, download from [python.org](https://www.python.org/downloads/). You need Python 3.10 or later.

```bash
pip install google-genai
```

### Step 3: Verify Your Setup

```python
from google import genai
import os
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello! Confirm you are Gemini."
)
print(response.text)
```

### Step 4: Start the Pipeline

#### Claude.ai (Recommended)
1. Create a new Claude.ai Project called **"MKT2700 Semester Project"**
2. **Custom Instructions** — open `skills/orchestrator.md` in a text editor, select all, copy, and paste it into the Project's Custom Instructions box
3. **Project Knowledge** — click the upload button (or drag-and-drop) and add these 9 files from the `skills/` folder on your computer:
   - `phase-1-strategic-foundation.md`
   - `phase-2-rubric-creation.md`
   - `phase-3-concept-discovery.md`
   - `phase-4-deep-research.md`
   - `phase-5-concept-evaluation.md`
   - `phase-6-refinement-specification.md`
   - `phase-7-prd-generation.md`
   - `llm-council-protocol.md`
   - `prd-presentation-SKILL.md`

   Do **not** upload `orchestrator.md` (already pasted above) or `DEPLOYMENT.md` (instructor-only).
4. Start a new chat within the Project and say: **"Start project"**
5. Follow the orchestrator's guidance through each phase

#### Claude Code (Advanced)

**Important:** You must run Claude Code from inside the ProdDevIQ directory. The `CLAUDE.md` file in this directory tells Claude about the 7-phase pipeline and where to find the skill files.

```bash
cd ProdDevIQ
claude
# Then say: "Start project"
```

Claude Code will read the CLAUDE.md, find the orchestrator skill, and begin Phase 1 automatically. All phase artifacts will be saved in this directory.

**NotebookLM Integration (auto-configured):** The package includes a `.claude/mcp.json` file that connects Claude Code to NotebookLM via an MCP server. The first time it runs, it will:
1. Download the NotebookLM MCP server automatically (requires Node.js/npm)
2. Open Chrome for a one-time Google login
3. After that, Claude can create and query NotebookLM notebooks directly during Phase 4 research

If you don't have Node.js installed or prefer to use NotebookLM manually in the browser, you can safely ignore this — the pipeline works without it.

### How the Pipeline Works

```
Phase 1: Strategic Foundation     → strategic-brief.md
Phase 2: Rubric Creation          → evaluation-rubric.md (LOCKED)
    ↓ [Council: Rubric Vetting]
Phase 3: Concept Discovery        → concept-candidates.md
Phase 4: Deep Research             → research-repository.md
Phase 5: Concept Evaluation        → evaluation-results.md
    ↓ [Council: Scoring]
Phase 6: Refinement & Spec         → refined-concept.md
    ↓ [Council: KANO Validation]
Phase 7: PRD Generation            → product-requirements-document.md + .docx
    ↓ [Council: PRD Review]
```

### Using the LLM Council

At 4 points in the pipeline, you'll run the LLM Council — a multi-model check using both Claude and Gemini to catch blind spots.

```bash
# Example: Phase 2 rubric vetting
python scripts/llm_council.py --checkpoint rubric --input evaluation-rubric.md --context strategic-brief.md
```

Then paste the output back into Claude and say: "Here is Gemini's independent assessment. Run the LLM Council reconciliation protocol."

### Need Help?
- Thursday Zoom Syncs with Professor Scheller
- Review the walkthrough videos
- Check the phase skill files in `skills/` for detailed instructions
- See [Gemini API Setup Guide](./gemini-api-setup.md) for API troubleshooting
- See [NotebookLM Setup Guide](./notebooklm-setup.md) for research workflow tips
