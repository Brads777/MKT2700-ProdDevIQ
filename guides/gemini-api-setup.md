# ©2026 Brad Scheller

# Gemini API Setup Guide
## MKT2700 Product Design & Development • Northeastern University • Spring 2026

### Why You Need This

The LLM Council feature uses Google's Gemini model to provide independent verification of Claude's work at key checkpoints. This catches blind spots and reduces model bias in your product development pipeline.

---

## Step 1: Get Your Google AI Studio API Key

### 1.1 Navigate to Google AI Studio
Go to [https://aistudio.google.com/](https://aistudio.google.com/) and sign in with your Google account (Northeastern or personal).

### 1.2 Access the API Key Section
- Look for the left sidebar navigation
- Click on **"Get API Key"** (it may be under a settings or developer menu)
- You should see a screen titled "API Keys"

### 1.3 Create a New API Key
1. Click the blue **"Create API Key"** button
2. A modal will appear asking you to select a Google Cloud project
3. Options:
   - **If you have an existing project:** Select it from the dropdown
   - **If this is your first time:** Click "Create new project" and give it a name like "MKT2700 Semester Project"
4. Click **"Create API Key in existing/new project"**

### 1.4 Copy and Save Your Key
- A new API key will be generated (starts with `AIza...`)
- Click the **copy icon** to copy the full key
- Save it somewhere secure (password manager, secure note, etc.)
- **Do NOT share this key publicly** (GitHub, Discord, etc.)

---

## Step 2: Set the Environment Variable

Your Python script needs to access this key via an environment variable called `GEMINI_API_KEY`.

### Mac / Linux / Git Bash (Windows)

#### Temporary (Current Session Only)
```bash
export GEMINI_API_KEY="AIzaSyC_your_actual_key_here"
```

#### Permanent (Recommended)
Add the export command to your shell configuration file:

**Bash:**
```bash
echo 'export GEMINI_API_KEY="AIzaSyC_your_actual_key_here"' >> ~/.bashrc
source ~/.bashrc
```

**Zsh (Mac default):**
```bash
echo 'export GEMINI_API_KEY="AIzaSyC_your_actual_key_here"' >> ~/.zshrc
source ~/.zshrc
```

**Git Bash (Windows):**
```bash
echo 'export GEMINI_API_KEY="AIzaSyC_your_actual_key_here"' >> ~/.bash_profile
source ~/.bash_profile
```

### Windows PowerShell

#### Temporary (Current Session Only)
```powershell
$env:GEMINI_API_KEY="AIzaSyC_your_actual_key_here"
```

#### Permanent (Recommended)
1. Open PowerShell as Administrator
2. Run:
```powershell
[System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'AIzaSyC_your_actual_key_here', 'User')
```
3. Close and reopen PowerShell to apply

### Windows Command Prompt

#### Temporary (Current Session Only)
```cmd
set GEMINI_API_KEY=AIzaSyC_your_actual_key_here
```

#### Permanent (Recommended)
1. Search for "Environment Variables" in Windows Start Menu
2. Click "Edit the system environment variables"
3. Click **"Environment Variables"** button
4. Under "User variables", click **"New"**
5. Variable name: `GEMINI_API_KEY`
6. Variable value: `AIzaSyC_your_actual_key_here`
7. Click OK, OK, OK
8. Restart your terminal

---

## Step 3: Install Python SDK

Install the Google GenAI library:

```bash
pip install google-genai
```

---

## Step 4: Verify Your Setup

Create a test script called `test_gemini.py`:

```python
from google import genai
import os

# Check if the environment variable is set
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("ERROR: GEMINI_API_KEY environment variable not set!")
    print("Please follow the setup instructions above.")
    exit(1)

print(f"API Key found: {api_key[:10]}... (truncated for security)")

# Configure the client
client = genai.Client(api_key=api_key)

# Test the connection
try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Hello! Confirm you are Gemini and ready to assist with MKT2700."
    )
    print("\n✓ Connection successful!")
    print(f"\nGemini's response:\n{response.text}")
except Exception as e:
    print(f"\n✗ Connection failed: {e}")
    print("Check the troubleshooting section below.")
```

Run it:
```bash
python test_gemini.py
```

Expected output:
```
API Key found: AIzaSyC_yo... (truncated for security)

✓ Connection successful!

Gemini's response:
Hello! I am Gemini, and I am ready to assist you with MKT2700...
```

---

## Troubleshooting

### Error: "GEMINI_API_KEY environment variable not set"
**Cause:** The environment variable isn't configured or not loaded.

**Fix:**
- Make sure you closed and reopened your terminal after setting the variable
- Check if it's set: `echo $GEMINI_API_KEY` (Mac/Linux) or `echo $env:GEMINI_API_KEY` (PowerShell)
- If empty, repeat Step 2 above

---

### Error: "Invalid API key"
**Cause:** The API key is incorrect or malformed.

**Fix:**
- Go back to [Google AI Studio](https://aistudio.google.com/) and verify your key
- Copy it again (make sure no extra spaces or characters)
- Update the environment variable with the correct key

---

### Error: "Quota exceeded" or "Rate limit exceeded"
**Cause:** You've hit the free tier usage limits.

**Free Tier Limits (as of Feb 2026):**
- 15 requests per minute
- 1,500 requests per day
- 1 million tokens per minute

**Fix:**
- Wait a few minutes and try again
- If you need higher limits, enable billing in Google Cloud Console (usually not needed for this course)
- The LLM Council only runs 4 times per semester, so free tier is sufficient

---

### Error: "Model not found"
**Cause:** The model name is outdated or misspelled.

**Fix:**
- The pipeline defaults to `gemini-2.0-flash`. If Google renames this model, update line 21 in `scripts/llm_council.py` where `DEFAULT_GEMINI_MODEL` is defined, or use the `--model` flag to override:
  ```bash
  python scripts/llm_council.py --checkpoint rubric --model gemini-2.0-flash-lite ...
  ```

---

### Error: "Module 'google.genai' not found"
**Cause:** The Python SDK isn't installed.

**Fix:**
```bash
pip install google-genai
```

If you're using a virtual environment, make sure it's activated first.

---

## Using the LLM Council in ProdDevIQ

Once your Gemini API is set up, you'll use it at 4 checkpoints:

### Checkpoint 1: Rubric Vetting (After Phase 2)
```bash
python scripts/llm_council.py --checkpoint rubric \
  --input evaluation-rubric.md \
  --context strategic-brief.md
```

### Checkpoint 2: Concept Scoring (After Phase 5)
```bash
python scripts/llm_council.py --checkpoint scoring \
  --input research-repository.md \
  --rubric evaluation-rubric.md \
  --concept "Your Concept Name"
```

### Checkpoint 3: KANO Validation (After Phase 6)
```bash
python scripts/llm_council.py --checkpoint kano \
  --input refined-concept.md \
  --persona target-user-persona.md
```
**Note:** Before running, extract your target user persona into `target-user-persona.md` from your refined concept (the "Target Users" section). The `--input` is your full refined concept with KANO-classified features.

### Checkpoint 4: PRD Review (After Phase 7)
```bash
python scripts/llm_council.py --checkpoint prd-review \
  --input product-requirements-document.md
```

Each time, paste Gemini's output back into Claude and say:
> "Here is Gemini's independent assessment. Run the LLM Council reconciliation protocol."

---

## Security Best Practices

1. **Never commit your API key to GitHub**
   - Add `.env` files to `.gitignore`
   - Use environment variables, not hardcoded keys

2. **Restrict your API key** (Optional but recommended)
   - In Google Cloud Console, go to "APIs & Services" > "Credentials"
   - Click on your API key
   - Under "API restrictions", select "Restrict key" and choose "Generative Language API"

3. **Regenerate if compromised**
   - If you accidentally share your key, delete it in Google AI Studio
   - Create a new one and update your environment variable

---

## Need More Help?

- Google AI Studio Docs: [https://ai.google.dev/docs](https://ai.google.dev/docs)
- Gemini API Python SDK: [https://github.com/googleapis/python-genai](https://github.com/googleapis/python-genai)
- Professor Scheller's Thursday Zoom Syncs
