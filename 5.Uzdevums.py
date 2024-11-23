#5 Uzdevums

import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
clean_text = re.sub(r'http\S+|@\S+|[^\w\s]', '', raw_text).lower()

print(clean_text)

