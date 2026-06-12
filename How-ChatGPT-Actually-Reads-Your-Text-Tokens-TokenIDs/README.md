# 🧠 Mastering LLM Text Processing with OpenAI Tiktoken

## 📌(TL;DR)
Large Language Models (LLMs) like GPT-4o-mini cannot understand raw text directly.  
Instead, they convert text into **tokens** using a process called *tokenization*.

This project explains how OpenAI's `tiktoken` library works and how text is converted into **Token IDs** for model processing.

LLMs do NOT read sentences like humans.  
They:
- Break text into **tokens (sub-words)**
- Convert tokens into **numeric IDs** which are **Token IDs**
- Process these IDs inside neural networks

This improves:
- Context handling
- Memory efficiency
- API cost optimization

---

👉 Watch the full explanation here:  
https://youtu.be/LTPOg6kF_G4

[![Watch Video](https://img.youtube.com/vi/LTPOg6kF_G4/maxresdefault.jpg)](https://youtu.be/LTPOg6kF_G4)


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
