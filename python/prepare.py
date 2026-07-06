import hashlib
from pathlib import Path
import pandas as pd
import random
import re

def obfuscate_id(val: str, prefix: str = "eris_") -> str:
    """Generate a deterministic, anonymized hash ID to prevent web searching."""
    string_to_hash = f"{prefix}{val}".encode("utf-8")
    return hashlib.md5(string_to_hash).hexdigest()[:12]

def add_noise(text: str) -> str:
    """
    Applies trivial noise to the text to defeat basic web search scraping.
    It replaces generic finance terms with synonymous phrasing.
    """
    if not isinstance(text, str):
        return text

    replacements = {
        "portfolio manager": "investment manager",
        "private equity firm": "PE sponsor",
        "startup": "early-stage company",
        "value at risk": "Value-at-Risk",
        "European call": "vanilla European call",
        "Chapter 11": "court-supervised bankruptcy",
        "M&A analyst": "mergers and acquisitions analyst"
    }
    for k, v in replacements.items():
        text = re.sub(re.escape(k), v, text, flags=re.IGNORECASE)
    return text

def prepare(raw: Path, public: Path, private: Path) -> None:
    """Transform raw data into public/private splits with data secrecy enforcement."""
    (public / "train").mkdir(exist_ok=True, parents=True)
    (public / "test").mkdir(exist_ok=True, parents=True)

    seed = random.randint(1, 10000)

    # 1. Load and process the training data
    train_df = pd.read_json(raw / "train.jsonl", lines=True)
    train_df = train_df.sample(frac=1, random_state=seed).reset_index(drop=True)
    train_df["id"] = train_df["id"].astype(str).apply(lambda x: obfuscate_id(x, "train_"))

    if "question" in train_df.columns:
        train_df["question"] = train_df["question"].apply(add_noise)

    train_df.to_json(public / "train.jsonl", orient="records", lines=True)
    train_df.to_json(public / "train" / "train.jsonl", orient="records", lines=True)

    # 2. Load test and solution data
    test_df = pd.read_json(raw / "test.jsonl", lines=True)
    solution_df = pd.read_json(raw / "solution.jsonl", lines=True)

    test_df = test_df.sample(frac=1, random_state=seed).reset_index(drop=True)
    solution_df = solution_df.set_index("id").reindex(test_df["id"]).reset_index()

    old_test_ids = test_df["id"].astype(str)
    id_map = {old_id: obfuscate_id(old_id, "test_") for old_id in old_test_ids}

    test_df["id"] = test_df["id"].astype(str).map(id_map)
    solution_df["id"] = solution_df["id"].astype(str).map(id_map)

    # Apply noise to test questions as well!
    if "question" in test_df.columns:
        test_df["question"] = test_df["question"].apply(add_noise)
    if "question" in solution_df.columns:
        solution_df["question"] = solution_df["question"].apply(add_noise)

    test_df.to_json(public / "test.jsonl", orient="records", lines=True)
    test_df.to_json(public / "test" / "test.jsonl", orient="records", lines=True)

    # 3. Generate sample_submission.csv with realistic dummy values instead of empty strings
    answers = ["-0.30" if i % 2 == 0 else "private equity" for i in range(len(test_df))]
    sample_sub = pd.DataFrame({
        "id": test_df["id"],
        "answer": answers
    })
    sample_sub.to_csv(public / "sample_submission.csv", index=False)

    # 4. Populate the private directory for the Eris grading engine
    solution_df[["id", "answer"]].to_csv(private / "answers.csv", index=False)
    solution_df.to_json(private / "solution.jsonl", orient="records", lines=True)
