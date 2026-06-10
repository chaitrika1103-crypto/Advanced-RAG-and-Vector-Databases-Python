# 01. Pinecone Vector Ingestion & Upsertion Pipeline

> **TL;DR:** To build an AI e-commerce vector database, initialize Pinecone with your API key, connect to your index using `pc.Index("ecommerce-openai")`, and generate vector embeddings using OpenAI’s `text-embedding-3-small` model. Map the structural product data fields directly into Pinecone's vector payloads and upsert them sequentially to enable semantic search capabilities.

---

## 📺 Video Tutorial & Timestamps
- **Watch Full Video Here:** [https://youtu.be/C8fJy-cmxtA](https://youtu.be/C8fJy-cmxtA)
- **Official Website:** [https://aicodewithharitha.com](https://aicodewithharitha.com)

* **[00:00]** - Previewing the Final Product Search Output inside Pinecone Database Cloud
* **[00:33]** - Architectural Overview: How to Build an AI E-commerce Vector Database with Python
* **[00:50]** - Step-by-Step Pinecone Index Configuration inside the Console Screen
* **[01:10]** - Selecting the Correct OpenAI Text-Embedding-3-Small Dimension and Distance Metric
* **[01:56]** - Secure API Credential Mapping for Cloud Vector Databases (Pinecone & OpenAI Keys)
* **[02:22]** - Setting Up a Local Development Server Environment inside Visual Studio Code
* **[03:52]** - Constructing Structural Product Data Fields and Catalog Dictionaries for Vector Storage
* **[04:18]** - Writing the Programmatic Embed Function Using OpenAI Text-Embedding-3-Small Engine
* **[04:51]** - Deploying the Automated Upsert Vector Python Script to Ship Embeddings to the Cloud

---

## 🧠 What You Will Learn
Master the AI discovery ecosystem by building a scalable, production-grade AI e-commerce vector database using Python. In this technical coding session, you will learn how to implement automated data ingestion pipelines leveraging Pinecone index configuration, generating multi-dimensional embeddings, and managing persistent cloud storage indices natively.

Whether you are configuring your first local development server environment or connecting specialized database endpoints, managing programmatic setups correctly ensures high performance. We look at OpenAI `text-embedding-3-small` integrations to map dense numeric representations of text and demonstrate how to securely deploy an upsert vector python script that parses, embeds, and ships localized catalog records into high-efficiency remote indexes. Learn to scale AI-driven intelligence from your development workspace straight to global architectural layers today!

---

## 🛠️ Step-by-Step Workspace Setup

### 1. Install Libraries
Install the necessary local Python packages in your terminal:
```bash
pip install openai pinecone-client
```

### 2. Pinecone Index Settings
- **Index Name:** `ecommerce-openai`
- **Dimension:** `1536` (Must match OpenAI `text-embedding-3-small`)
- **Metric:** `Cosine`
