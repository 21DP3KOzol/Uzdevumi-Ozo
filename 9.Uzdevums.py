#9 Uzdevums
import transformers
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "Reiz kādā tālā zemē..."
story = generator(prompt, max_length=50, num_return_sequences=1)

print(story[0]['generated_text'])

