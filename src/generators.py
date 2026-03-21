from .llm_engine import client
from .prompts import SUMMARY_PROMPT, TRAINING_PROMPT, QUIZ_PROMPT
import re


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


def format_quiz(text):
    # Put each option (A, B, C, D) on its own line
    text = re.sub(r'\s+([A-D])\)', r'\n\1)', text)
    # Put Answer: on its own line
    text = re.sub(r'\s+(Answer:)', r'\n\1', text)
    # Put each Question on its own line with a blank line before it
    text = re.sub(r'\s*(Question\s+\d+:)', r'\n\n\1', text)
    return text.strip()


def generate_quiz(text):
    prompt = QUIZ_PROMPT.format(input_text=text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    return format_quiz(raw)