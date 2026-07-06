# Dataset Description

## Overview
This dataset is designed for training models on advanced financial reasoning and represents high-quality Q&A pairs with deep reasoning chains. The data was synthetically generated using Gemini AI guided by a human financial expert with experience in quantitative finance. It covers a wide array of specialized financial domains, providing complex quantitative questions along with step-by-step reasoning (Chain-of-Thought) and final expert answers.

## File Structure
- `train/train.jsonl` — Labeled training data (1,006 entries) containing questions, reasoning chains, and answers.
- `test/test.jsonl` — The test set (100 entries) provided to competitors, containing only `id` and `question`.
- `test/solution.jsonl` — The hidden solution set (100 entries) containing the full ground-truth answers and reasoning for the test set.
- `sample_submission.csv` — A template file demonstrating the expected submission format for the competition.
*(This is the complete file listing for the dataset.)*

## Features
| Column   | Type   | Description |
|----------|--------|-------------|
| id       | string | Unique identifier for each question (e.g., `train_0001` or `test_0001`). |
| question | string | The financial problem or question presented to the model. |
| cot      | string | The Chain-of-Thought reasoning enclosed in `<think>...</think>` tags to solve the problem step-by-step. |
| answer   | string | The final, professional answer or explanation derived from the reasoning process. |

## Notes
**Domain-Specific Context:**
This highly specialized dataset covers advanced topics such as stochastic calculus, machine learning in finance, options pricing, quantitative risk management, and portfolio optimization. Authentic industry lexicon is used throughout to ensure high-quality, realistic case studies and expert dialogues.

**Synthetic Data Generation Process:**
The data was synthetically generated through structured templates and iterative human-AI collaboration to simulate expert-level, deep-reasoning quantitative scenarios. The generation process prioritized deep, accurate, and educational content, introducing controlled complexity through randomized variables to ensure realistic distributions. The dataset was formatted to prevent duplication and ensure appropriate string lengths for both the reasoning (`cot`) and the final `answer`.