# ©2026 Brad Scheller

# The 7-Phase Product Lab

**MKT2700: Product Design & Development • Spring 2026**
**Northeastern University**
**Instructor:** Brad Scheller
**Team Size:** 5 students
**Deadline:** Sunday, February 15, 2026, 11:59 PM EST (extended deadline: Tuesday, February 17, 11:59 PM EST)
**Support:** Thursday Zoom Syncs, 7:00–8:00 PM EST (Zoom link on Canvas)

---

## Assignment Overview

Welcome to the Product Lab. For the next seven days, your team of five will operate as a venture-backed product development studio. Your mission: identify a high-potential product opportunity, validate it with market evidence, and deliver a production-ready Product Requirements Document (PRD) that could go straight to engineering.

You won't be doing this alone. You'll be using **ProdDevIQ**, an AI-augmented pipeline that guides you through seven systematic phases of product discovery and development. The pipeline leverages **Claude** as your primary strategic partner and **Gemini** as an independent evaluator through the **LLM Council**—a multi-model validation system that catches blind spots, challenges assumptions, and ensures your work meets professional standards.

By the end of this sprint, you'll deliver:
- A comprehensive PRD with market validation, KANO-classified features (a framework for categorizing features by customer impact—Must-Be, Performance, Excitement, Indifferent, Reverse), technical architecture, and a detailed implementation roadmap
- A narrated video slideshow that traces your team's journey and presents the winning concept
- Evidence of rigorous process execution across all seven phases
- LLM Council validation at four critical decision gates
- A portfolio-ready artifact that demonstrates your ability to systematically de-risk product ideas

**Required Tools:**
- Claude.ai Pro (or Claude Code with MCP)
- Google AI Studio (Gemini API - free tier)
- NotebookLM (free)
- Perplexity Pro

**Required Videos (watch before starting — available on Canvas under Files > ProdDevIQ > videos):**
1. **Pipeline Setup Guide** — How to set up your AI tools and accounts
2. **AI Pipeline Walkthrough** — Full walkthrough of the 7-phase process

---

## Before You Start

1. **Watch both required videos** on Canvas (Files > ProdDevIQ > videos). They'll save you hours of confusion.
2. **Download the ProdDevIQ package** from Canvas (Files > ProdDevIQ). Unzip it to a folder on your computer. This contains all pipeline skills, setup guides, and the LLM Council helper script.
3. **Follow the Getting Started Guide** (`guides/getting-started.md`) to set up all accounts and API keys (Claude Pro, Gemini API, NotebookLM, Perplexity Pro).
4. **Set up your working environment** — choose one:
   - **Claude.ai (Recommended):** Create a Project, paste `skills/orchestrator.md` as Custom Instructions, then upload the other 9 skill files to Project Knowledge. See the Getting Started Guide for details.
   - **Claude Code (Advanced):** Open a terminal, `cd` into your unzipped `ProdDevIQ` folder, and run `claude`. The `CLAUDE.md` file in the folder tells Claude about the pipeline automatically — no extra setup needed.
5. **Say "Start project"** to Claude to begin Phase 1.

**Important:** Make sure Claude has access to the pipeline skill files *before* you start. If you're using Claude.ai, that means the files are uploaded to your Project. If you're using Claude Code, that means you're running it from inside the ProdDevIQ folder where the `skills/` directory lives.

**Pro Tip:** The pipeline is designed to prevent common failure modes (confirmation bias, vague requirements, unsupported claims). Trust the process. If a phase feels tedious, it's probably because it's forcing you to do the hard thinking that most teams skip.

---

## The 7 Phases

### Phase 1: Strategic Foundation (Day 1)

**What you're doing:** Establishing the strategic context for your product exploration. You'll define your industry focus, analyze macro forces (PESTEL), map the competitive landscape, and articulate your team's unfair advantage.

**Why this matters:** Product ideas don't exist in a vacuum. The same concept can succeed or fail depending on timing, market readiness, and competitive dynamics. This phase forces you to think like investors: *Why this? Why now? Why you?*

**Guidance questions:**
- What industry are you passionate about? What gives your team an unfair advantage (domain expertise, network, technical capability)?
- Where are the biggest unmet needs in this space? What are customers complaining about or building workarounds for?
- What are the macro forces (PESTEL) that create opportunity *right now*? Why is this the perfect moment for disruption?
- Run parallel research in Perplexity and Gemini—cover trends, competitors, regulatory changes, technological enablers, and market positioning.

**Artifact produced:** `strategic-brief.md`

**Decision gate:** None (this is foundational work for all subsequent phases)

---

### Phase 2: Rubric Creation (Day 1-2)

**What you're doing:** Building a custom evaluation framework that defines what "success" means for your specific market and company context. This isn't a generic template—it's a tailored rubric with weighted criteria and specific scoring level definitions.

**Why this matters:** Most teams choose product ideas based on gut feel or whoever argues loudest. A rigorous rubric forces you to articulate success criteria upfront, weight them by importance, and apply them consistently. It's the difference between "I like this idea" and "This idea scores 8.4/10 on our validated framework."

**Guidance questions:**
- What makes a product successful in YOUR specific market? (Don't copy generic rubrics—think about your industry's unique dynamics.)
- What criteria should carry the most weight for your company's situation? (Early-stage startups might prioritize speed-to-market; established companies might prioritize strategic fit.)
- Are your scoring level definitions specific enough that two people would assign the same score? (Vague definitions like "moderate potential" lead to inconsistent scoring.)
- **LLM Council checkpoint:** Have Gemini vet your rubric before you lock it. Look for ambiguous definitions, missing criteria, or unrealistic weightings.

**Artifact produced:** `evaluation-rubric.md`

**Decision gate:** LLM Council rubric validation (Claude + Gemini must both approve before Phase 3)

---

### Phase 3: Concept Discovery (Day 2-3)

**What you're doing:** Generating 30-40 product concept candidates through systematic exploration of customer pain points, competitive gaps, adjacent market transfers, and emerging technology enablers. You're deliberately casting a wide net before narrowing down.

**Why this matters:** The quality of your final product is constrained by the quality of your initial candidate pool. If you only consider 3-4 obvious ideas, you'll never discover the high-potential outliers. This phase forces quantity before quality—because creativity requires exploration.

**Guidance questions:**
- What are people complaining about on Reddit, YouTube, and X? What workarounds are they building themselves?
- What solutions from adjacent industries could transfer to your space? (E.g., Uber for X, Airbnb for Y, Stripe for Z.)
- What new technologies or platforms enable solutions that weren't possible two years ago? (AI, blockchain, edge computing, AR/VR, etc.)
- What jobs are customers "hiring" existing products to do—and what jobs are they struggling to accomplish?

**Artifact produced:** `concept-candidates.md` (30-40 concepts, each with a brief description and initial assessment)

**Decision gate:** None (but you must have at least 30 concepts to proceed)

**Pro Tip:** Create a **Discovery Notebook** in NotebookLM and feed it all your research sources. Use it to surface patterns and connections you'd miss manually.

---

### Phase 4: Deep Research (Day 3-4)

**What you're doing:** Taking your top 10-15 concepts from Phase 3 and conducting deep research on each: TAM/SAM/SOM sizing, competitive analysis, customer evidence, technical feasibility, and go-to-market dynamics.

**Why this matters:** Surface-level research leads to surface-level decisions. This phase forces you to dig into the uncomfortable questions: *Who are the real competitors? What's the actual market size? Why would customers switch from their current solution? What's the realistic path to $10M ARR (Annual Recurring Revenue)?*

**Guidance questions:**
- For each top concept: what's the TAM/SAM/SOM? (Use bottom-up calculations, not just top-down market reports.)
- Who are the direct and indirect competitors, and what are their specific weaknesses? (Not "they have bad UX"—what exactly is broken?)
- What evidence exists that customers would actually *pay* for this? (Not "I think people would want it"—where's the proof?)
- What technical risks or dependencies could derail this concept? (Third-party APIs, regulatory approval, hardware supply chains, etc.)

**Artifact produced:** `research-repository.md` (detailed research notes for each top concept, with citations)

**Decision gate:** None (but you must have deep research on at least 10 concepts to proceed)

**Pro Tip:** Follow EVERY follow-up question in NotebookLM and Perplexity. The AI's suggested questions often reveal blind spots you didn't know you had.

---

### Phase 5: Concept Evaluation (Day 4-5)

**What you're doing:** Applying your rubric from Phase 2 to score each concept from Phase 4. Claude scores first, then Gemini scores independently, then you reconcile disagreements and select your winning concept.

**Why this matters:** This is where your strategic discipline pays off. By forcing AI models to score independently, you avoid confirmation bias and groupthink. Disagreements between Claude and Gemini reveal genuine uncertainty—which is exactly where you need to dig deeper.

**Guidance questions:**
- Does your scoring feel honest, or are you gaming the rubric to favor a concept you already like? (If you find yourself adjusting definitions mid-scoring, stop and recalibrate.)
- Where do Claude and Gemini disagree? Those disagreements reveal genuine uncertainty—investigate the root cause before proceeding.
- Is the winning concept *clearly* the best, or are there close alternatives worth considering? (If scores are within 0.5 points, you may need more research.)
- What would change your mind about the winning concept? (If the answer is "nothing," you're not being intellectually honest.)

**Artifact produced:** `evaluation-results.md` (scored concepts with justifications and LLM Council reconciliation)

**Decision gate:** LLM Council scoring validation (Claude and Gemini must both approve the winning concept before Phase 6)

---

### Phase 6: Refinement & Specification (Day 5-6)

**What you're doing:** Taking your winning concept and refining it through SCAMPER ideation, KANO feature classification, and Jobs-to-be-Done mapping. You're transforming a high-level concept into a detailed product specification.

**Why this matters:** A concept is not a product. This phase forces you to make hard decisions about what to build, what to cut, and what to prioritize. KANO classification reveals which features are must-haves (customers expect them) vs. delighters (customers love them but don't expect them). This prevents feature bloat and ensures you're building the *right* product, not just more features.

**Guidance questions:**
- What would happen if you 10x'd the core value proposition? (SCAMPER: Magnify—forces you to think bigger.)
- What features do competitors include that customers don't actually need? (SCAMPER: Eliminate—removes complexity.)
- Would your target user be FURIOUS if a feature were missing (Must-Be) or just prefer more of it (Performance)? (This is KANO classification—critical for prioritization.)
- What job is the customer hiring your product to do? (Not features—outcomes. E.g., "I need to close deals faster," not "I need a CRM.")

**Artifact produced:** `refined-concept.md` (detailed product specification with KANO-classified features and JTBD mapping)

**Decision gate:** LLM Council KANO validation (Gemini must approve your feature classification before Phase 7)

---

### Phase 7: PRD Generation (Day 6-7)

**What you're doing:** Synthesizing all prior work into a professional Product Requirements Document with 10 core sections: Executive Summary, Problem Statement, Strategic Context, Target Users, Product Vision, Feature Specifications (KANO-Classified), Architecture Overview, Risks & Mitigations, Success Metrics, and Implementation Roadmap.

**Why this matters:** This is your final deliverable—the artifact that proves you can systematically de-risk a product idea and communicate it to stakeholders. A strong PRD is portfolio-ready and could go straight to engineering, fundraising, or executive review.

**Guidance questions:**
- Does every market claim in your PRD have a cited source? (Minimum 25 citations across the document.)
- Could a development team actually build from your Implementation Roadmap? (Not "build the MVP"—specific sprints, dependencies, and deliverables.)
- Are your success metrics specific, measurable numbers—not vague goals? (Not "increase engagement"—"increase DAU/MAU (Daily Active Users / Monthly Active Users) from 0.20 to 0.35 within 90 days.")
- Would an investor or executive read this PRD and immediately understand why this product will succeed? (If not, your Executive Summary needs work.)

**Artifact produced:** `product-requirements-document.md` AND `.docx`/`.pdf` (MKT2700 branded)

**Decision gate:** LLM Council PRD review (full document validation before submission)

---

### Video Slideshow (Day 7)

**What you're doing:** Creating a narrated video slideshow (5–10 minutes) that traces your team's journey through the 7 phases and presents your winning concept to an audience of investors and executives.

**Why this matters:** The ability to synthesize complex work into a compelling narrative is a core product management skill. Your PRD proves you can do the analytical work; the video proves you can communicate it persuasively.

**What to include:**
1. **Team introduction** — who you are and your domain expertise
2. **Problem & opportunity** — the market gap you identified and why now
3. **Journey highlights** — key decisions, pivots, and LLM Council insights that shaped your direction (not a phase-by-phase recap—focus on turning points)
4. **Winning concept overview** — what it does, who it's for, and why it wins
5. **Key evidence** — 3-5 strongest data points that validate the concept (TAM, customer evidence, competitive advantage)
6. **Roadmap snapshot** — high-level implementation plan and success metrics

**Guidance questions:**
- Would a first-time viewer understand your concept within the first two minutes?
- Are you showing *evidence* (data, citations, evaluation scores) or just making assertions?
- Does the video tell a story—or just walk through slides?
- Could an investor watch this and want to learn more?

**Format requirements:**
- 5–10 minutes in length (under 5 loses depth; over 10 loses attention)
- All team members should contribute (on-screen or narrating)
- Use screen recordings, slides, or any tool your team prefers (PowerPoint, Canva, Loom, etc.)
- Export as `.mp4` or provide a shareable link (YouTube, Loom, Google Drive)

**Artifact produced:** Video file (`.mp4`) or shareable video link

---

## Timeline

| Day | Target | Phases |
|-----|--------|--------|
| **Tuesday, Feb 10** | Team formed, industry chosen, pipeline started | Phase 1 |
| **Wednesday, Feb 11** | Strategic brief + rubric complete | Phase 1-2 |
| **Thursday, Feb 12** (Zoom Sync) | Concepts discovered, progress check | Phase 3-4 |
| **Friday, Feb 13** | Deep research complete, concepts evaluated | Phase 4-5 |
| **Saturday, Feb 14** | Concept refined, PRD started | Phase 5-6 |
| **Sunday, Feb 15** | PRD complete, council review done, video recorded | Phase 7 + Video |
| **Sunday, Feb 15, 11:59 PM EST** | **TARGET SUBMISSION** | **All artifacts** |

**Deadline:** Aim to submit by **Sunday, February 15 at midnight**. If you need more time, you may submit through **Tuesday, February 17 at 11:59 PM EST** — no penalty, no questions asked. After Tuesday, submissions will not be accepted.

---

## What You Submit

Submit all files via Canvas as a single ZIP archive. Your submission must include:

1. **Product Requirements Document**
   - `product-requirements-document.md` (primary artifact)
   - `product-requirements-document.docx` OR `.pdf` (MKT2700 branded)

2. **Phase Artifacts**
   - `strategic-brief.md` (Phase 1)
   - `evaluation-rubric.md` (Phase 2)
   - `concept-candidates.md` (Phase 3)
   - `research-repository.md` (Phase 4)
   - `evaluation-results.md` (Phase 5)
   - `refined-concept.md` (Phase 6)

3. **Progress Tracker**
   - `progress-tracker.md` (showing all phases complete with timestamps)
   - **Note:** The progress tracker is generated when you start the pipeline. Save it as a separate file before submission.

4. **LLM Council Outputs**
   - `council-rubric.md` (Phase 2 validation)
   - `council-scoring.md` (Phase 5 validation)
   - `council-kano.md` (Phase 6 validation)
   - `council-prd-review.md` (Phase 7 validation)

5. **Video Slideshow**
   - `.mp4` file included in the ZIP **or** a shareable link (YouTube, Loom, Google Drive) included in a `video-link.md` file
   - 5–10 minutes, narrated, all team members contributing

**File naming convention:** `TeamName_MKT2700_ProductLab_Spring2026.zip`

---

## Grading Criteria

This deliverable is worth **5% of your final grade** (5.0 points). Your work will be evaluated across six dimensions:

| Dimension | Weight | Points |
|-----------|--------|--------|
| Evidence Quality | 20% | 1.00 |
| Process Rigor | 20% | 1.00 |
| Concept Selection Quality | 20% | 1.00 |
| PRD Completeness | 15% | 0.75 |
| Video Slideshow | 15% | 0.75 |
| Team Collaboration | 10% | 0.50 |
| **Total** | **100%** | **5.00** |

### 1. Evidence Quality (1.00 pt)
- Are all market claims supported by cited sources? (Minimum 25 citations across the PRD)
- Do you distinguish between primary research (customer interviews, usage data) and secondary research (analyst reports, articles)?
- Are your TAM/SAM/SOM calculations defensible, with clear assumptions and bottom-up math?

### 2. Process Rigor (1.00 pt)
- Did you complete all 7 phases in order, with all required artifacts?
- Did you use the LLM Council at all 4 checkpoints (rubric, scoring, KANO, PRD)?
- Is there evidence of systematic exploration (30+ concepts in Phase 3, deep research on 10+ concepts in Phase 4)?

### 3. Concept Selection Quality (1.00 pt)
- Is the winning concept clearly justified by the evaluation results?
- Did you identify and resolve disagreements between Claude and Gemini?
- Does the concept align with your strategic brief and rubric criteria?

### 4. PRD Completeness (0.75 pt)
- Are all 10 PRD sections present and fully developed?
- Are features KANO-classified with clear justifications?
- Is the Implementation Roadmap specific enough for a dev team to execute?

### 5. Video Slideshow (0.75 pt)
- Does the video clearly present the winning concept and its value proposition?
- Is there evidence of the team's journey—key decisions, pivots, and insights from the LLM Council?
- Are claims backed by data (TAM, customer evidence, evaluation scores), not just assertions?
- Is the production quality professional (clear audio, readable visuals, 5–10 min length)?
- Did all team members contribute?

### 6. Team Collaboration (0.50 pt)
- Is there evidence of distributed work across the team? (All members contributing to research, evaluation, and writing)
- Did the team leverage Thursday Zoom Syncs for feedback and course correction?

**Detailed rubric:** See Canvas for the full grading rubric with scoring level definitions.

---

## Tips for Success

1. **Set up your tools on Day 1.** Follow the Getting Started Guide (`guides/getting-started.md`) before doing anything else. Tool setup issues are the #1 time-waster.

2. **Start early.** The pipeline takes 6-7 days if you maintain momentum. Starting late means rushing phases—and rushing leads to weak research and poor decisions.

3. **Trust the LLM Council.** When Claude and Gemini disagree, it's not a bug—it's a feature. Disagreements reveal blind spots. Investigate them.

4. **Cite everything.** Every market claim, every competitive insight, every TAM calculation should have a source. Unsupported claims = weak PRD.

5. **Use NotebookLM aggressively.** Feed it all your research, then ask it follow-up questions. It'll surface connections you'd never find manually.

6. **Attend the Thursday Zoom Sync (7:00–8:00 PM EST).** Professor Scheller will be live to answer questions, troubleshoot tool issues, and review your progress. If you're stuck, confused, or behind schedule — this is your best chance to get unblocked. Don't skip it.

7. **Don't fall in love with your first idea.** The best teams score 30+ concepts and let the data decide. The worst teams pick a favorite on Day 1 and reverse-engineer justifications.

8. **Read the rubric before you submit.** If your PRD is missing citations, KANO classifications, or a detailed roadmap, you'll lose points. Check twice, submit once.

---

## Support & Resources

- **Thursday Zoom Sync (7:00–8:00 PM EST):** Live Q&A with Professor Scheller — bring questions, get unstuck (Zoom link on Canvas)
- **Required Videos:** Pipeline Setup Guide + AI Pipeline Walkthrough (Canvas > Files > ProdDevIQ > videos)
- **ProdDevIQ Package:** All skills, guides, and scripts (Canvas > Files > ProdDevIQ)
- **Getting Started Guide:** `guides/getting-started.md` in the ProdDevIQ package
- **Gemini API Setup:** `guides/gemini-api-setup.md` in the ProdDevIQ package
- **NotebookLM Guide:** `guides/notebooklm-setup.md` in the ProdDevIQ package
- **Office Hours:** By appointment (email Brad)

**Questions?** Post in the Canvas discussion forum or ask during the Thursday Zoom Sync (7:00–8:00 PM EST).

---

© 2026 Northeastern University | MKT2700 Product Design & Development
*"The best way to predict the future is to architect it."*
