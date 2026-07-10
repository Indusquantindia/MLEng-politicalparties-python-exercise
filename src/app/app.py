import os
import requests
import streamlit as st

DEFAULT_API_URLS = [
    os.getenv("PREDICTION_API_URL"),
    "http://localhost:8000/get-prediction/",
    "http://model_inference_endpoint:8000/get-prediction/",
]


def get_prediction(input_text):
    # TODO - task 3
    # -----------------------------------
    # Goal: our goal is to complete the implementation of this function, 
    #       which takes input text and returns a prediction result from a pre-trained model.
    # Old placeholder code:
    # pass

    if not input_text or not input_text.strip():
        return "No tweet text provided."

    payload = {"input_texts": input_text}

    for api_url in [url for url in DEFAULT_API_URLS if url]:
        try:
            response = requests.post(api_url, json=payload, timeout=5)
            response.raise_for_status()
            prediction_data = response.json()
            return prediction_data.get("prediction", "No prediction returned")
        except requests.RequestException:
            continue

    return (
        "Unable to reach the prediction service. "
        "Set PREDICTION_API_URL or run the model inference endpoint first."
    )

# Streamlit page configuration
st.set_page_config(page_title="Tweet Classifier", layout="wide")

# Streamlit UI components
st.title("Classify your tweet")

# User inputs the tweet
tweet_input = st.text_input("Enter your tweet", "")

# Button to trigger prediction
if st.button("Classify Tweet"):
    # Get prediction
    prediction = get_prediction(tweet_input)
    
    # Display the prediction
    st.write("Prediction:", prediction)

