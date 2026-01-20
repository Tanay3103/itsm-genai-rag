import pandas as pd
from langchain_qdrant import QdrantVectorStore

from config.config import QDRANT_URL, TICKET_COLLECTION
from embeddings.embeddings import get_embeddings

embeddings = get_embeddings()


def load_ticket_history():
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

    QdrantVectorStore.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metas,
        url=QDRANT_URL,
        collection_name=TICKET_COLLECTION,
    )
