
from fastapi import FastAPI
from sumapi.api import SumAPI

api = SumAPI(username='kave', password='kave')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/kave/{user_input}")
def read_root(user_input: str):
    sentiment = get_sentiment(user_input)
    color = get_color(sentiment)
    return {"result": {"sentiment": sentiment, "color": color}}


def get_sentiment(text: str):
    result = api.sentiment_analysis(text, domain='general')
    return result['evaluation']['label']


def get_color(sentiment):
    # Duygu analizine göre renk döndür
    if sentiment == "Pozitif":
        return "#A8E6CF"  # Pastel Yeşil
    elif sentiment == "Negatif":
        return "#FF8A80"  # Pastel Kırmızı
    elif sentiment == "Nötr":
        return "#FFD3B6"  # Pastel Turuncu
