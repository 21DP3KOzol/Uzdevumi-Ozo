#7 uzdevums
import gensim
from gensim.models import KeyedVectors

# Pirms tam lejupielādē vārdu iegulšanas modeli, piemēram, "fasttext-lv".
# fasttext_model = KeyedVectors.load("fasttext-lv.vec")
words = ["māja", "dzīvoklis", "jūra"]

for word in words:
    print(f'{word}: {fasttext_model[word]}')

similarity = fasttext_model.similarity("māja", "dzīvoklis")
print(f"Līdzība starp 'māja' un 'dzīvoklis': {similarity}")
