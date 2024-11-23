#1.Uzdevums

from collections import Counter
import re

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
words = re.findall(r'\w+', text.lower())
word_frequency = Counter(words)

print(word_frequency)


