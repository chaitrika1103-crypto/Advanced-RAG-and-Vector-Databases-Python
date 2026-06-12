# How ChatGPT Actually Reads Your Text (Tokens Explained in Python)

import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-4o-mini")

text = input("Enter Text  :")

token_ids = tokenizer.encode(text)
tokens = [tokenizer.decode([tid]) for tid in token_ids]

print("Tokens :", tokens)
print("Token IDs:  ", token_ids)
