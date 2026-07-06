import pandas as pd
import string
import re

def normalize_answer(s: str) -> str:
    """Lower text and remove punctuation, articles and extra whitespace."""
    if pd.isna(s):
        return ""

    s = str(s)

    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))

def grade(submission: pd.DataFrame, answers: pd.DataFrame) -> float:
    """
    Score a submission against ground truth answers using Exact Match.
    """
    if 'id' not in submission.columns or 'answer' not in submission.columns:
        raise ValueError("Submission must have 'id' and 'answer' columns.")

    merged = answers.merge(submission, on='id', how='left', suffixes=('_truth', '_pred'))

    correct = 0
    total = len(answers)

    if total == 0:
        return 0.0

    for _, row in merged.iterrows():
        truth = row['answer_truth']
        pred = row['answer_pred']

        if pd.isna(pred):
            continue

        if normalize_answer(truth) == normalize_answer(pred):
            correct += 1

    return float(correct) / float(total)
