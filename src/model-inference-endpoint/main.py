from collections import Counter
from pathlib import Path
import re

from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd

mlflow.set_tracking_uri('data')

DATA_FILE = Path(__file__).resolve().parent / "data" / "Tweets.csv"
if not DATA_FILE.exists():
    DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "Tweets.csv"

_keyword_scores = None


class InputText(BaseModel):
    input_texts: str


app = FastAPI()


@app.get("/health")
def get_health():
    return {"status": "OK"}


def _clean_text(text: str) -> str:
    if text is None:
        return ""

    text = str(text)
    text = re.sub(r'https?://\S+', " ", text)
    text = re.sub(r'[^A-Za-z]+', " ", text)
    return " ".join(text.split()).strip().lower()


def _load_training_data() -> pd.DataFrame:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Training data file not found at {DATA_FILE}")
    return pd.read_csv(DATA_FILE)


def _build_keyword_scores(data_frame: pd.DataFrame) -> dict[str, float]:
    counters = {"Republican": Counter(), "Democrat": Counter()}
    party_counts = {"Republican": 0, "Democrat": 0}

    for _, row in data_frame.iterrows():
        party = str(row.get("Party", "")).strip()
        if party not in counters:
            continue

        clean_tweet = _clean_text(row.get("Tweet", ""))
        tokens = [token for token in clean_tweet.split() if len(token) > 1]
        if not tokens:
            continue

        party_counts[party] += 1
        counters[party].update(tokens)

    scores: dict[str, float] = {}
    for token in set(counters["Republican"]) | set(counters["Democrat"]):
        rep_freq = counters["Republican"][token] / max(1, party_counts["Republican"])
        dem_freq = counters["Democrat"][token] / max(1, party_counts["Democrat"])
        scores[token] = rep_freq - dem_freq

    return scores


def _get_keyword_scores() -> dict[str, float]:
    global _keyword_scores
    if _keyword_scores is None:
        data_frame = _load_training_data()
        _keyword_scores = _build_keyword_scores(data_frame)
    return _keyword_scores


def _predict_party_from_text(input_text: str) -> str:
    clean_tweet = _clean_text(input_text)
    if not clean_tweet:
        return "No valid text to classify."

    tokens = [token for token in clean_tweet.split() if len(token) > 1]
    weights = _get_keyword_scores()
    score = sum(weights.get(token, 0.0) for token in tokens)
    return "Republican" if score >= 0 else "Democrat"


def _load_mlflow_model():
    try:
        model_path = Path(__file__).resolve().parent / "data" / "model"
        if model_path.exists():
            return mlflow.pyfunc.load_model(str(model_path))
    except Exception:
        pass
    return None


@app.post("/get-prediction/")
def get_prediction(input_data: InputText):
    # TODO - task 2 
    # -----------------------------------
    # Goal: our goal is to complete the implementation of this function, 
    #       which takes input data and returns a prediction result from a pre-trained model.
    # Old placeholder code:
    # pass

    if not input_data.input_texts or not input_data.input_texts.strip():
        return {"prediction": "No tweet text provided."}

    model = _load_mlflow_model()
    if model is not None:
        try:
            output = model.predict([input_data.input_texts])
            if isinstance(output, str):
                prediction = output
            else:
                prediction = output[0] if len(output) else output
            return {"prediction": str(prediction)}
        except Exception:
            pass

    fallback_prediction = _predict_party_from_text(input_data.input_texts)
    return {"prediction": fallback_prediction}
