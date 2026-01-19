import pandas as pd
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from utils.qdrant_client import get_qdrant_client
from config import TICKET_COLLECTION

df = pd.read_csv("data/itsm_historical_tickets.csv")

texts, metas = [], []
for _, r in df.iterrows():
    texts.append(
        f"Issue: {r.short_description}\n"
        f"Details: {r.detailed_description}\n"
        f"Root Cause: {r.root_cause}\n"
        f"Resolution: {r.resolution}"
    )
    metas.append(r.to_dict())

Qdrant.from_texts(
    texts,
    OpenAIEmbeddings(),
    metadatas=metas,
    client=get_qdrant_client(),
    collection_name=TICKET_COLLECTION
)

print("Tickets ingested")
