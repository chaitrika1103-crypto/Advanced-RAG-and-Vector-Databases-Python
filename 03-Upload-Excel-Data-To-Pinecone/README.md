# 🚀 Upload Excel Data to Pinecone Vector Database Using Python

## 📌 TL;DR

Learn how to read Excel files using Pandas, generate embeddings with llama-text-embed-v2, create vector records with metadata, and upsert them into Pinecone Vector Database using Python.

This workflow is commonly used for:

- RAG Applications
- Semantic Search
- AI Search Engines
- Product Search
- Recommendation Systems
- Knowledge Base Assistants

---

👉 Watch the full explanation here:

https://youtu.be/9JD32S_DJd8

[![Watch Video](https://img.youtube.com/vi/9JD32S_DJd8/maxresdefault.jpg)](https://youtu.be/9JD32S_DJd8)

---

## 🚀 Introduction

Most business data starts in spreadsheets.

Product catalogs, inventory records, customer databases, and knowledge bases are often stored in Excel files.

Before AI systems can perform semantic search, this data must be converted into vector embeddings and stored inside a vector database.

This tutorial demonstrates the complete Excel-to-Pinecone workflow using Python.

---

## 🧠 What You'll Learn

✅ Read Excel files using Pandas

✅ Process DataFrame rows using iterrows()

✅ Generate embeddings using llama-text-embed-v2

✅ Create vector IDs

✅ Add metadata

✅ Upsert vectors into Pinecone

✅ Verify stored vectors

✅ Understand RAG ingestion pipelines

---

## ⚡ Workflow

```text
Excel File
    ↓
Pandas DataFrame
    ↓
Text Construction
    ↓
llama-text-embed-v2
    ↓
Vector Embeddings
    ↓
Metadata
    ↓
Pinecone Upsert
    ↓
Semantic Search
