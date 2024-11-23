#4.Uzdevums

from transformers import pipeline

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
for sentence in sentences:
    result = sentiment_model(sentence)
    print(f'Teikums: "{sentence}" — Noskaņojums: {result[0]["label"]}')

