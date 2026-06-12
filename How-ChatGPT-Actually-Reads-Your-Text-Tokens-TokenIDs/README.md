Mastering LLM Text Processing: How OpenAI Tiktoken Tokenizer Encodes Text for Models like GPT-4o-mini
TL;DR : > LLMs cannot read raw characters directly; instead, they rely on a tokenizer to break down strings into sub-word pieces called tokens and map them to unique numerical IDs. 
By using OpenAI's fast tiktoken library in Python, developers can programmatically encode text inputs into discrete numerical arrays required by embeddings and vector databases. 
This precise processing optimization improves context window budgeting, tracks strict semantic splits, and lowers overall API computing costs.

# 🧠 Mastering LLM Text Processing with OpenAI Tiktoken

## 📌 Overview
Large Language Models (LLMs) like GPT-4o-mini cannot understand raw text directly.  
Instead, they convert text into **tokens** using a process called *tokenization*.

This project explains how OpenAI's `tiktoken` library works and how text is converted into **Token IDs** for model processing.

---

## 🎯 Key Idea (TL;DR)

LLMs do NOT read sentences like humans.  
They:
- Break text into **tokens (sub-words)**
- Convert tokens into **numeric IDs**
- Process these IDs inside neural networks

This improves:
- Context handling
- Memory efficiency
- API cost optimization

---

## 🚀 Introduction

Ever wondered how ChatGPT understands language?

It doesn’t read characters or words directly.  
Instead, it uses **tokenization**, which converts text into machine-readable numbers.

In this guide, we explore how to use OpenAI’s `tiktoken` library to visualize this process in Python.

---

## 🛠️ Installation

Install the required library:

```bash
pip install tiktoken
