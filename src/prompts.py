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

Generate 5 multiple-choice questions based on the SOP below.
You MUST follow this exact format for every question — no exceptions:

Question 1: [question text]
A) [option]
B) [option]
C) [option]
D) [option]
Answer: [letter only]

Question 2: [question text]
A) [option]
B) [option]
C) [option]
D) [option]
Answer: [letter only]

Rules:
- Each option (A, B, C, D) MUST be on its own separate line
- "Answer:" MUST be on its own line immediately after option D
- Do NOT put all options on one line
- Do NOT add any extra commentary or text outside this format

SOP:
{input_text}
"""