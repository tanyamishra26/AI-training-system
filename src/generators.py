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