Mastering LLM Text Processing: How OpenAI Tiktoken Tokenizer Encodes Text for Models like GPT-4o-mini
TL;DR : > LLMs cannot read raw characters directly; instead, they rely on a tokenizer to break down strings into sub-word pieces called tokens and map them to unique numerical IDs. 
By using OpenAI's fast tiktoken library in Python, developers can programmatically encode text inputs into discrete numerical arrays required by embeddings and vector databases. 
This precise processing optimization improves context window budgeting, tracks strict semantic splits, and lowers overall API computing costs.

Video Timestamps 
[00:01] - Introduction to tokens and token IDs output
[00:29] - How to install and import OpenAI tiktoken library in Python
[00:44] - Setting up tokenizer encoding for GPT-4o-mini model
[01:09] - Handling dynamic text input for text tokenization
[01:17] - Using tokenizer encode method to generate token IDs
[01:55] - Parsing through token IDs list using Python loops
[02:26] - Fixing syntax errors in Python text tokenization script
[02:54] - Final text to token IDs code verification and output

This repository contains a lightweight, production-ready Python script demonstrating how Large Language Models (LLMs) like ChatGPT convert raw human text strings into machine-readable tokens and numerical token IDs using OpenAI’s highly optimized tiktoken library.

Installation
Ensure you have Python installed, then install the official tokenization engine:
pip install tiktoken
