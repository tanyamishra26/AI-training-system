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
Generate 5 MCQs.

STRICT RULES:
- Start each question with "Question 1:", "Question 2:"
- Each option must start with A), B), C), D)
- End with: Answer: <letter>

Example:
Question 1: ...
A) ...
B) ...
C) ...
D) ...
Answer: B

SOP:
{input_text}
"""


