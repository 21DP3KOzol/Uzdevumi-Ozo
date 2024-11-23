#10 uzdevums

import transformers
from transformers import pipeline

translator = pipeline("translation_lv_to_en", model="Helsinki-NLP/opus-mt-lv-en")
texts = ["Labdien! Kā jums klājas?", "Es šodien lasīju interesantu grāmatu."]

for text in texts:
    translation = translator(text)
    print(f'Latviski: "{text}" — Angliski: "{translation[0]["translation_text"]}"')

