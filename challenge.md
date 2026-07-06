# Advanced Financial Reasoning Challenge

## Overview
This challenge evaluates an AI agent's ability to perform expert-level quantitative and strategic financial reasoning. Standard LLMs often struggle with multi-step mathematical operations, strict adherence to financial formulas (like Black-Scholes or Taylor series expansion), and navigating highly specialized domain lexicon (e.g., Venture Capital, Private Equity, and quantitative risk management).

Participants are tasked with building or fine-tuning a model that can ingest complex financial case studies and quantitative problems, generate the appropriate reasoning steps (Chain-of-Thought), and output the correct final answer. A labeled training dataset of 1,006 examples is provided, featuring both the step-by-step reasoning (enclosed in `<think>` tags) and the final expert answers. The hidden test set contains 100 new, unseen problems across diverse financial domains.

## Related Work & Differentiation
While existing financial datasets like Sanscritic/finance-pro-bench rely on subjective, LLM-as-a-judge point rubrics over fictional multi-page narratives, this challenge introduces a strictly deterministic Exact Match (EM) evaluation protocol. By pairing deep, multi-step `<think>` reasoning traces with automated string-normalization, this benchmark eliminates evaluator drift and partial-credit loopholes, testing true quantitative derivation accuracy.

## Evaluation
Submissions are scored using **Exact Match (EM)** accuracy. Due to the diverse nature of the answers (some are precise monetary values, others are specific conceptual explanations), the grading script strips punctuation, normalizes whitespace, and checks if the predicted string matches the ground-truth string. The platform grader strictly checks for exact text matching; participants must ensure number formats (e.g. `10.5` vs `10.50`) perfectly match those seen in the training data.

```python
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

**Example of a correctly formatted submission file (`sample_submission.csv`):**
```csv
id,answer
test_8a3b1c2d9f4e,-0.30
test_4b2c9a1d3f8e,private equity
test_7f3e1b8c2d9a,-0.30
test_1d9a8c3b2e4f,private equity
```