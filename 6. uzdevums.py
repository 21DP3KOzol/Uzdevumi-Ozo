#6 Uzdevums
import transformers

from transformers import pipeline

article = """Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."""
summarizer = pipeline("summarization", model="t5-small")
summary = summarizer(article, max_length=50, min_length=20, do_sample=False)

print(summary[0]['summary_text'])
