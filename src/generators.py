from .llm_engine import client
from .prompts import SUMMARY_PROMPT, TRAINING_PROMPT, QUIZ_PROMPT


def generate_summary(text):
    prompt = SUMMARY_PROMPT.format(input_text=text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def generate_training(text):
    prompt = TRAINING_PROMPT.format(input_text=text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def generate_quiz(text):
    prompt = QUIZ_PROMPT.format(input_text=text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def parse_quiz(quiz_text):
    questions = []
    blocks = quiz_text.split("\n\n")

    for block in blocks:
        lines = block.strip().split("\n")

        if len(lines) < 6:
            continue

        question = lines[0]
        options = lines[1:5]
        answer_line = lines[5]

        answer = answer_line.split(":")[-1].strip()

        questions.append({
            "question": question,
            "options": options,
            "answer": answer
        })

    return questions