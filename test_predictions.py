import re
import sys
from collections import Counter
import pandas as pd

data = pd.read_csv("data/Tweets.csv")

def clean_text(text: str) -> str:
    if text is None:
        return ""
    text = str(text)
    text = re.sub(r'https?://\S+', " ", text)
    text = re.sub(r'[^A-Za-z]+', " ", text)
    return " ".join(text.split()).strip().lower()

counters = {"Republican": Counter(), "Democrat": Counter()}
party_counts = {"Republican": 0, "Democrat": 0}

for _, row in data.iterrows():
    party = str(row.get("Party", "")).strip()
    if party not in counters:
        continue
    clean_tweet = clean_text(row.get("Tweet", ""))
    tokens = [token for token in clean_tweet.split() if len(token) > 1]
    if not tokens:
        continue
    party_counts[party] += 1
    counters[party].update(tokens)

scores = {}
for token in set(counters["Republican"]) | set(counters["Democrat"]):
    rep_freq = counters["Republican"][token] / max(1, party_counts["Republican"])
    dem_freq = counters["Democrat"][token] / max(1, party_counts["Democrat"])
    scores[token] = rep_freq - dem_freq

def predict(text: str) -> str:
    clean = clean_text(text)
    tokens = [t for t in clean.split() if len(t) > 1]
    score = sum(scores.get(t, 0.0) for t in tokens)
    return "Republican" if score >= 0 else "Democrat"

print("=" * 70)
print("PREDICTION TEST RESULTS")
print("=" * 70)

test_cases = [
    "Thank you for supporting our military and veterans",
    "Climate change is a real threat we must address",
    "Defending our Second Amendment rights",
    "Healthcare is a right for all Americans",
    "Lower taxes for businesses and workers",
    "We need to strengthen our borders"
]

for tweet in test_cases:
    pred = predict(tweet)
    print(f"\nInput: {tweet}")
    print(f"Predicted: {pred}")


print("\n" + "=" * 70)
print(f"Model Stats:")
print(f"  Training data: {len(data)} tweets")
print(f"  Republicans: {party_counts['Republican']}")
print(f"  Democrats: {party_counts['Democrat']}")
print(f"  Vocabulary: {len(scores)} tokens")
