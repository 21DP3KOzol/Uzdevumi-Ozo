#3.Uzdevums

import re

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

words1 = set(re.findall(r'\w+', text1.lower()))
words2 = set(re.findall(r'\w+', text2.lower()))

common_words = words1 & words2
similarity = len(common_words) / len(words1 | words2) * 100

print(f'Kopējie vārdi: {common_words}')
print(f'Sakritības procents: {similarity:.2f}%')

