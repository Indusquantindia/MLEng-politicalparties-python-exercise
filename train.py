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

print(f"  Training data: {len(data)} tweets")