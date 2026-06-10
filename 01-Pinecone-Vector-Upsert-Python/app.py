from openai import OpenAI
from pinecone import Pinecone

# Initialize clients using API keys
openai = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)
pc = Pinecone(
    api_key="YOUR_PINECONE_API_KEY"
)

# Connect to the created index
index = pc.Index("PINECONE INDEX_NAME")

# Structural product data fields
products = [
    {"pid": "P001", "pcat": "Mobiles", "pname": "Apple iPhone 15"},
    {"pid": "P002", "pcat": "Laptops", "pname": "Dell Inspiron 15"},
    {"pid": "P003", "pcat": "Shoes", "pname": "Nike Air Max"},
]

# Function to generate embeddings using text-embedding-3-small
def embed(text):
    response = openai.embeddings.create(
        model="text-embedding-3-small", 
        input=text
    )
    return response.data[0].embedding

vectors = []

# Map data fields and construct the vector payloads
for p in products:
    text = f"{p['pcat']} {p['pname']}"
    vectors.append(
        {
            "id": p["pid"],
            "values": embed(text),
            "metadata": {
                "pid": p["pid"], 
                "pcat": p["pcat"], 
                "pname": p["pname"]
            },
        }
    )

# Deploy programmatic upsert to ship embeddings to the cloud
index.upsert(vectors=vectors)
print("Data Inserted Successfully In PineCone Vector Database...")
