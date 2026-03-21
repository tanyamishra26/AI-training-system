SUMMARY_PROMPT = """
You are an AI training assistant.

Summarize the following SOP into 5-7 clear bullet points.
Keep it concise and easy to understand.

SOP:
{input_text}
"""

TRAINING_PROMPT = """
You are an expert trainer.

Convert the following SOP into step-by-step training instructions
for a new employee. Make it simple, structured, and actionable.

SOP:
{input_text}
"""

QUIZ_PROMPT = """
You are an assessment generator.

Generate 5 multiple-choice questions based on the SOP.
Each question should have:
- 4 options
- Correct answer clearly marked

SOP:
{input_text}
"""