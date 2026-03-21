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
Generate 5 multiple-choice questions based on the SOP.

STRICT FORMAT:
Q1: Question text
A) Option
B) Option
C) Option
D) Option
Answer: B

(Repeat for all questions)

SOP:
{input_text}
"""


