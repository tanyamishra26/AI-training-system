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
    
    blocks = quiz_text.split("Question")

    for block in blocks:
        lines = block.strip().split("\n")

        if len(lines) < 5:
            continue

        question = lines[0]
        options = []
        answer = None

        for line in lines[1:]:
            if line.strip().startswith(("A)", "B)", "C)", "D)")):
                options.append(line.strip())

            if "Answer" in line or "Correct" in line:
                answer = line.split(":")[-1].strip()

        if question and options and answer:
            questions.append({
                "question": question,
                "options": options,
                "answer": answer
            })

    return questions