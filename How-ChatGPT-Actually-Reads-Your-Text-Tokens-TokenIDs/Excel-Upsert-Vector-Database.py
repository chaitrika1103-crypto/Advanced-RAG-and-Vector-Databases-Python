import pandas as pd
from pinecone import Pinecone
from openai import OpenAI

openai = OpenAI(
    api_key="YOUR-OPENAI-KEY"
)
pc = Pinecone(
    api_key="YOUR-PINECONE-KEY"
)


index = pc.Index("INDEX NAME")

df = pd.read_excel("Excelfilename.xlsx")

records = []

for _, row in df.iterrows():
    pid = str(row["pid"])

    text = f"""
    Product ID:{row['pid']}
    Category:{row['pcat']}
    Product Name:{row['pname']}
    Description:{row['desc']}
    """

    embedding = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[text],
        parameters={"input_type": "passage", "truncate": "END"},
    )

    vector = embedding[0]["values"]
    records.append(
        {
            "id": pid,
            "values": vector,
            "metadata": {
                "pid": row["pid"],
                "pcat": row["pcat"],
                "pname": row["pname"],
                "desc": row["desc"],
            },
        }
    )

    index.upsert(vectors=records)
    print(f"successfully Inserted excel sheet into pinecone.. embeddings")
