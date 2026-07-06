# Advanced Financial Reasoning Challenge

## Overview
This challenge evaluates an AI agent's ability to perform expert-level quantitative and strategic financial reasoning. Standard LLMs often struggle with multi-step mathematical operations, strict adherence to financial formulas (like Black-Scholes or Taylor series expansion), and navigating highly specialized domain lexicon (e.g., Venture Capital, Private Equity, and quantitative risk management).

Participants are tasked with building or fine-tuning a model that can ingest complex financial case studies and quantitative problems, generate the appropriate reasoning steps (Chain-of-Thought), and output the correct final answer. A labeled training dataset of 1,006 examples is provided, featuring both the step-by-step reasoning (enclosed in `<think>` tags) and the final expert answers. The hidden test set contains 100 new, unseen problems across diverse financial domains.

## Evaluation
Submissions are scored using **Exact Match (EM)** accuracy. Due to the diverse nature of the answers (some are precise monetary values, others are specific conceptual explanations), the grading script strips punctuation, normalizes whitespace, and checks if the predicted string matches the ground-truth string.

```python
import string
import re

def normalize_answer(s: str) -> str:
    """Lower text and remove punctuation, articles and extra whitespace."""
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

def evaluate(y_true: list[str], y_pred: list[str]) -> float:
    """Calculates Exact Match accuracy."""
    if len(y_true) != len(y_pred):
        raise ValueError("Mismatch in number of predictions and ground truths.")

    correct = 0
    for yt, yp in zip(y_true, y_pred):
        if normalize_answer(yt) == normalize_answer(yp):
            correct += 1

    return correct / len(y_true)
```

## Dataset
The dataset contains structured financial Q&A pairs. The files provided to participants are:

- `train/train.jsonl` (1,006 rows): Contains `id`, `question`, `cot` (reasoning chain), and `answer`.
- `test/test.jsonl` (100 rows): Contains `id` and `question`. (The `cot` and `answer` fields are hidden).

**Column Descriptions (train.jsonl):**
| Column   | Type   | Description |
|----------|--------|-------------|
| id       | string | Unique identifier for each question |
| question | string | The financial problem or case study |
| cot      | string | Expert reasoning steps enclosed in `<think>...</think>` tags |
| answer   | string | The final, concise answer |

## Submission
Submit a CSV file with the following format based on the `sample_submission.csv` template:

| Column | Type   | Description                               |
|--------|--------|-------------------------------------------|
| id     | string | Row identifier corresponding to test.jsonl|
| answer | string | The final predicted answer string         |

**Requirements:**
- Must contain exactly 100 rows (one per test sample, plus the header).
- Must include the header row `id,answer`.
- Ensure answers match the formatting implied by the training data.