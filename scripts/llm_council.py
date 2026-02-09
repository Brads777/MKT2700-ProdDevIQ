"""
LLM Council Helper — MKT2700 Pipeline
Automates Gemini evaluation and comparison matrix generation.

Usage:
    python scripts/llm_council.py --checkpoint rubric --input evaluation-rubric.md --context strategic-brief.md
    python scripts/llm_council.py --checkpoint scoring --input research-repository.md --rubric evaluation-rubric.md --concept "Concept Name"
    python scripts/llm_council.py --checkpoint kano --input refined-concept.md --persona target-user-persona.md
    python scripts/llm_council.py --checkpoint prd-review --input product-requirements-document.md

Optional:
    --model MODEL    Override the default Gemini model (default: gemini-2.0-flash)
"""

import argparse
import os
import sys
from pathlib import Path

# --- Configuration ---
DEFAULT_GEMINI_MODEL = "gemini-2.0-flash"


def configure_api(model_name=None):
    """Configure Gemini API from environment variable. Returns (client, model_name)."""
    try:
        from google import genai
    except ImportError:
        print("ERROR: google-genai package not installed.")
        print("Install it with: pip install google-genai")
        sys.exit(1)
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY environment variable not set.")
        print("Get a free key at: https://aistudio.google.com/apikey")
        print("Then run: export GEMINI_API_KEY='your-key-here'")
        sys.exit(1)
    client = genai.Client(api_key=api_key)
    model = model_name or DEFAULT_GEMINI_MODEL
    print(f"Using model: {model}")
    return client, model


def read_file(path):
    """Read a file and return its contents."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"\nERROR: File not found: {path}")
        print("Make sure you're running this from the ProdDevIQ directory and the file exists.")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: Could not read file {path}: {e}")
        sys.exit(1)


def run_gemini_evaluation(client, model_name, prompt):
    """Send prompt to Gemini and return response text."""
    print(f"  Sending to {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        if not response.text:
            print("\nERROR: Gemini returned an empty response (content safety filter may have blocked it).")
            print("Try rephrasing your input or check the Gemini API documentation.")
            sys.exit(1)
        print(f"  Response received ({len(response.text)} chars)")
        return response.text
    except Exception as e:
        error_msg = str(e)
        print(f"\nERROR: Gemini API request failed: {error_msg}")
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            print("\nThis is a rate limit error. Your options:")
            print("  1. Wait a minute and try again")
            print("  2. Check your quota at: https://ai.dev/rate-limit")
            print("  3. Try a different model with: --model gemini-2.0-flash-lite")
        elif "404" in error_msg or "NOT_FOUND" in error_msg:
            print(f"\nModel '{model_name}' not found. Try:")
            print("  --model gemini-2.0-flash")
            print("  --model gemini-2.0-flash-lite")
            print("  --model gemini-1.5-pro")
        else:
            print("This might be due to:")
            print("  - Content safety filters blocking the request")
            print("  - Network connectivity issues")
            print("  - Invalid API key")
        sys.exit(1)


# --- Checkpoint: Rubric Vetting ---
def rubric_vetting(client, model_name, rubric_path, context_path):
    """Phase 2: Have Gemini independently review the draft rubric."""
    rubric = read_file(rubric_path)
    context = read_file(context_path)

    prompt = f"""TASK: Review this evaluation rubric for a product development project. Assess independently.

COMPANY CONTEXT:
{context}

DRAFT RUBRIC:
{rubric}

Evaluate the rubric on these dimensions:
1. COMPLETENESS: Are any critical criteria missing for this industry/market? List any gaps.
2. REDUNDANCY: Do any criteria overlap or measure the same thing? Identify pairs.
3. WEIGHT BALANCE: Are the category weights and individual weights reasonable? Flag over/under-weighted items.
4. LEVEL DEFINITIONS: Are the 0-4 level definitions specific, observable, and unambiguous? Flag vague ones.
5. BIAS CHECK: Do criteria or weights unfairly favor a particular type of solution? Identify any bias.
6. MUST-HAVE CONSTRAINTS: Are the pass/fail gates reasonable and sufficient?

For each dimension, provide:
- Rating: Strong / Adequate / Needs Improvement
- Specific findings with explanations
- Recommended changes (if any)

Format as a structured markdown report."""

    return run_gemini_evaluation(client, model_name, prompt)


# --- Checkpoint: Concept Scoring ---
def concept_scoring(client, model_name, rubric_path, dossier_path, concept_name):
    """Phase 5: Have Gemini independently score a concept."""
    rubric = read_file(rubric_path)
    dossier = read_file(dossier_path)

    prompt = f"""TASK: Score the following product concept against every criterion in this rubric.

RUBRIC:
{rubric}

CONCEPT: {concept_name}
RESEARCH EVIDENCE:
{dossier}

For EACH criterion:
1. Score (0-4) based on the level definitions
2. One-sentence justification citing specific evidence
3. Confidence (High/Medium/Low)

Calculate final weighted score: Σ(score × weight) ÷ Σ(4 × weight) × 100%

Format as a markdown scorecard table."""

    return run_gemini_evaluation(client, model_name, prompt)


# --- Checkpoint: KANO Validation ---
def kano_validation(client, model_name, features_path, persona_path):
    """Phase 6: Have Gemini independently classify features via KANO."""
    features = read_file(features_path)
    persona = read_file(persona_path)

    prompt = f"""TASK: Independently classify the following product features using the KANO model.

TARGET USER:
{persona}

FEATURES TO CLASSIFY:
{features}

For EACH feature, classify into exactly one KANO category:
- Must-Be: Absence causes dissatisfaction, presence doesn't increase satisfaction
- Performance: More is better, linearly proportional to satisfaction
- Excitement: Unexpected, creates disproportionate delight
- Indifferent: Users don't care either way
- Reverse: Would hurt satisfaction if included

For each classification, provide:
1. Category assignment
2. One-sentence justification based on user needs
3. Confidence (High/Medium/Low)

Format as a markdown table."""

    return run_gemini_evaluation(client, model_name, prompt)


# --- Checkpoint: PRD Review ---
def prd_review(client, model_name, prd_path):
    """Phase 7: Have Gemini review the complete PRD."""
    prd = read_file(prd_path)

    prompt = f"""TASK: Review this Product Requirements Document for quality, consistency, and completeness.

PRD:
{prd}

Review each section and assess:
1. EVIDENCE SUFFICIENCY: Are claims supported by cited sources? Flag unsupported assertions.
2. INTERNAL CONSISTENCY: Do sections contradict each other?
3. LOGICAL FLOW: Does the narrative make sense from problem to solution to implementation?
4. COMPLETENESS: Are any required subsections missing or thin?
5. ACTIONABILITY: Could a development team build from this PRD? Are specs specific enough?

For each of the 10 sections, provide:
- Pass / Needs Revision
- Specific issues found (if any)
- Severity: Critical (blocks submission) / Minor (improve if time allows)

Format as a structured markdown review."""

    return run_gemini_evaluation(client, model_name, prompt)


# --- Comparison Matrix Generator ---
def generate_comparison_header(checkpoint_name):
    """Generate the header for a comparison output file."""
    return f"""# LLM Council Comparison — {checkpoint_name}
## Generated by llm_council.py

**Evaluator A:** Claude (current session)
**Evaluator B:** Gemini (API)

---

## Gemini's Independent Assessment

"""


# --- Main ---
def main():
    parser = argparse.ArgumentParser(description="LLM Council Helper — MKT2700 Pipeline")
    parser.add_argument("--checkpoint", required=True,
                        choices=["rubric", "scoring", "kano", "prd-review"],
                        help="Which council checkpoint to run")
    parser.add_argument("--input", required=True, help="Primary input file path")
    parser.add_argument("--context", help="Context file (strategic-brief.md for rubric)")
    parser.add_argument("--rubric", help="Rubric file (for scoring checkpoint)")
    parser.add_argument("--concept", help="Concept name (for scoring checkpoint)")
    parser.add_argument("--persona", help="Persona file (for KANO checkpoint)")
    parser.add_argument("--output", help="Output file path (default: council-{checkpoint}.md)")
    parser.add_argument("--model", default=DEFAULT_GEMINI_MODEL,
                        help=f"Gemini model to use (default: {DEFAULT_GEMINI_MODEL})")

    args = parser.parse_args()
    client, model_name = configure_api(args.model)

    print(f"\n=== LLM Council: {args.checkpoint.upper()} ===\n")

    if args.checkpoint == "rubric":
        if not args.context:
            print("ERROR: --context (strategic-brief.md) required for rubric checkpoint")
            sys.exit(1)
        result = rubric_vetting(client, model_name, args.input, args.context)

    elif args.checkpoint == "scoring":
        if not args.rubric or not args.concept:
            print("ERROR: --rubric and --concept required for scoring checkpoint")
            sys.exit(1)
        result = concept_scoring(client, model_name, args.rubric, args.input, args.concept)

    elif args.checkpoint == "kano":
        if not args.persona:
            print("ERROR: --persona required for KANO checkpoint")
            sys.exit(1)
        result = kano_validation(client, model_name, args.input, args.persona)

    elif args.checkpoint == "prd-review":
        result = prd_review(client, model_name, args.input)

    # Write output
    output_path = args.output or f"council-{args.checkpoint}.md"
    header = generate_comparison_header(args.checkpoint)
    Path(output_path).write_text(header + result, encoding="utf-8")
    print(f"\n  Output saved to: {output_path}")
    print(f"\n  Next step: Paste this into Claude for reconciliation.")
    print(f"  Say: 'Here is Gemini's independent {args.checkpoint} assessment. Compare with yours and run the LLM Council reconciliation protocol.'")


if __name__ == "__main__":
    main()
