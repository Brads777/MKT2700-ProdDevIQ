# ©2026 Brad Scheller

# NotebookLM Setup & Research Workflow Guide
## MKT2700 Product Design & Development • Northeastern University • Spring 2026

### What is NotebookLM?

NotebookLM is Google's AI-powered research assistant that helps you organize, analyze, and synthesize information from multiple sources. For MKT2700, you'll use it primarily in **Phase 3 (Concept Discovery)** and **Phase 4 (Deep Research)** to build a comprehensive research repository for each product concept.

**Key features:**
- Add sources: URLs, PDFs, YouTube videos, Google Drive files, pasted text
- AI-powered Q&A based on your sources
- Deep Research mode for thorough analysis
- Auto-generated summaries and study guides
- Audio overviews (AI-generated podcast-style summaries)

**Cost:** Free (as of Feb 2026)

---

## Step 1: Create Your First Notebook

### 1.1 Navigate to NotebookLM
Go to [https://notebooklm.google.com/](https://notebooklm.google.com/) and sign in with your Google account.

### 1.2 Create a New Notebook
1. Click the **"+ New Notebook"** button (top right or center of screen)
2. Give it a name related to your concept, for example:
   - "Concept A: Smart Water Bottle Research"
   - "Concept B: AI Study Planner Research"
   - "Concept C: Sustainable Packaging Research"

### 1.3 Understand the Interface
- **Left Sidebar:** List of all sources you've added
- **Center Panel:** Chat interface to ask questions
- **Right Panel:** Source viewer (shows the actual content when you click a source)

---

## Step 2: Add Sources

NotebookLM can ingest multiple types of content. Add at least 5-10 sources per concept.

### Source Types

#### 1. URLs (Web Pages, Articles, Blogs)
1. Click **"+ Add Source"** (or drag-and-drop a link)
2. Select **"Website"**
3. Paste the URL
4. Click **"Add"**
5. NotebookLM will scrape and index the content

**Pro tip:** Use Perplexity Pro to find high-quality sources first, then add those URLs to NotebookLM.

#### 2. PDFs (Research Papers, Reports, Whitepapers)
1. Click **"+ Add Source"**
2. Select **"Upload file"**
3. Choose your PDF file
4. Click **"Add"**

**Examples:**
- Academic papers from Google Scholar
- Industry reports (Nielsen, Gartner, McKinsey)
- Patent documents from USPTO

#### 3. YouTube Videos
1. Click **"+ Add Source"**
2. Select **"YouTube"**
3. Paste the video URL
4. NotebookLM will extract the transcript and index it

**Examples:**
- Product reviews
- Conference talks (TED, Web Summit, CES)
- Expert interviews

#### 4. Google Drive Files (Docs, Sheets, Slides)
1. Click **"+ Add Source"**
2. Select **"Google Drive"**
3. Navigate to your file and select it
4. Click **"Add"**

**Use case:** Your own notes from Phases 1-2 (strategic brief, evaluation rubric) can be added as context.

#### 5. Pasted Text
1. Click **"+ Add Source"**
2. Select **"Paste text"**
3. Copy-paste content (meeting notes, competitor analysis, survey results)
4. Give it a title
5. Click **"Add"**

---

## Step 3: Use Deep Research Mode

Deep Research is NotebookLM's most powerful feature for Phase 4. It generates comprehensive research reports based on your sources.

### 3.1 Activate Deep Research
1. In the chat panel, look for the **"Deep Research"** button (may be under a "Research" or "Generate" menu)
2. Enter your research question, for example:
   - "What are the key customer pain points for [target market]?"
   - "What are the competitive advantages and disadvantages of [product category]?"
   - "What are the emerging trends in [industry]?"

### 3.2 Review the Output
NotebookLM will:
- Analyze all your sources
- Generate a multi-section report
- Cite specific sources for each claim
- Identify gaps in your research

### 3.3 Follow Up with Questions
Don't stop at the first output. Ask follow-up questions to dig deeper:
- "What evidence supports [specific claim]?"
- "What are the counter-arguments to [trend]?"
- "Which sources discuss [specific feature]?"

**Pro tip:** Follow every follow-up question. The more you probe, the more you uncover blind spots.

---

## Step 4: Organize Notebooks by Concept

Create a separate notebook for each concept you're evaluating (typically 3-5 concepts in Phase 3).

### Recommended Notebook Structure

```
MKT2700 Semester Project/
├── Concept A: [Name]/
│   ├── Source 1: Perplexity Report - Market Size
│   ├── Source 2: YouTube - Competitor Product Review
│   ├── Source 3: PDF - Academic Paper on User Behavior
│   ├── Source 4: URL - TechCrunch Article
│   └── ...
├── Concept B: [Name]/
│   ├── Source 1: ...
│   └── ...
└── Concept C: [Name]/
    ├── Source 1: ...
    └── ...
```

### Naming Conventions
Use descriptive names so you can find them later:
- **Good:** "Concept A: Smart Water Bottle - Hydration Tracking for Athletes"
- **Bad:** "Notebook 1"

---

## Step 5: Export and Use Research in ProdDevIQ

### 5.1 Export Options
NotebookLM allows you to export:
- **Study Guide:** Auto-generated summary with key points
- **FAQ:** Common questions and answers based on sources
- **Timeline:** Chronological view (if sources have dates)
- **Audio Overview:** AI-generated podcast-style discussion (great for review)

### 5.2 Add to ProdDevIQ Pipeline
1. Export the Deep Research report or Study Guide
2. Save it as a markdown file in your ProdDevIQ project:
   ```
   research/concept-a-notebooklm-report.md
   ```
3. Reference it in Phase 4 when building your `research-repository.md`

### 5.3 Feed Back to Claude
When Claude asks for research summaries in Phase 4, you can:
- Copy-paste NotebookLM's Deep Research output directly
- Or say: "I've uploaded the NotebookLM report to Project Knowledge. Use it to populate the research repository."

---

## Pro Tips for MKT2700

### Tip 1: Load Perplexity Results as Sources
After running a Perplexity Pro deep research query:
1. Copy the full output (including sources)
2. In NotebookLM, click **"+ Add Source"** → **"Paste text"**
3. Paste the Perplexity output
4. Title it "Perplexity Research - [Topic]"
5. Now NotebookLM can cross-reference Perplexity's findings with your other sources

### Tip 2: Follow Every Follow-Up Question
The first answer is never enough. Keep asking:
- "What's the evidence for that?"
- "Are there any contradicting views?"
- "What are the implications for [your target market]?"

This iterative questioning uncovers insights you'd miss with a single query.

### Tip 3: Use Audio Overviews for Review
Before Phase 5 (Concept Evaluation), generate an Audio Overview for each concept:
1. Click the **"Generate"** menu in a notebook
2. Select **"Audio Overview"**
3. NotebookLM will create a 5-15 minute AI-generated discussion between two "hosts" summarizing your research
4. Listen to it while commuting or exercising to refresh your memory

### Tip 4: Tag Key Insights
As you chat with NotebookLM, use the **"Pin"** feature to save important insights:
- Click the pin icon next to any AI response
- Pinned items appear in a sidebar for quick reference
- Use these pins when writing your `research-repository.md` in Phase 4

### Tip 5: Add Your Strategic Brief and Rubric as Context
In Phase 4, add your `strategic-brief.md` and `evaluation-rubric.md` as sources to the concept notebooks. This ensures NotebookLM's research aligns with your evaluation criteria.

---

## Optional: NotebookLM MCP Server (Claude Code Users)

If you're using Claude Code instead of Claude.ai, you can integrate NotebookLM directly via an MCP (Model Context Protocol) server.

### What It Does
- Lets Claude Code read your NotebookLM notebooks
- Enables Claude to query your research without you copy-pasting
- Automates research workflow in Phase 4

### Setup
1. Install the NotebookLM MCP server:
   ```bash
   npm install -g @pleaseprompto/notebooklm-mcp
   ```

2. Add to your Claude Code config (`~/.config/claude/config.json`):
   ```json
   {
     "mcpServers": {
       "notebooklm": {
         "command": "notebooklm-mcp",
         "args": []
       }
     }
   }
   ```

3. Authenticate with your Google account (follow the CLI prompts)

4. In Claude Code, you can now say:
   - "List my NotebookLM notebooks"
   - "Read the Deep Research report from Concept A notebook"
   - "Query all notebooks for customer pain points"

**Source:** [PleasePrompto/notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)

---

## Troubleshooting

### Issue: "Unable to add source - URL blocked"
**Cause:** Some websites block scraping.

**Fix:**
- Download the page as a PDF (print → save as PDF) and upload it instead
- Or copy-paste the content as text

---

### Issue: "Source processing failed"
**Cause:** File is too large or in an unsupported format.

**Fix:**
- PDFs: Compress or split into smaller files
- Videos: Use shorter clips or extract transcript manually
- Max file size: 50 MB per source (as of Feb 2026)

---

### Issue: "Deep Research not generating comprehensive reports"
**Cause:** Not enough sources or sources lack depth.

**Fix:**
- Add at least 5-10 sources per concept
- Include diverse source types (academic, industry, news, video)
- Load Perplexity Pro research reports as sources for richer context

---

### Issue: "NotebookLM is citing outdated information"
**Cause:** Sources are old or not recent.

**Fix:**
- Filter Perplexity searches by date (last 6 months)
- Add recent sources (2024-2026)
- Cross-check with Google Trends or industry reports

---

## Need More Help?

- NotebookLM Official Guide: [https://notebooklm.google.com/help](https://notebooklm.google.com/help)
- NotebookLM YouTube Channel (tutorials): [https://www.youtube.com/@NotebookLM](https://www.youtube.com/@NotebookLM)
- Professor Scheller's Thursday Zoom Syncs
