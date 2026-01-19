from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from utils.qdrant_client import get_qdrant_client
from config import KNOWLEDGE_COLLECTION

docs = PyPDFLoader("data/itsm_context_knowledge.pdf").load()

Qdrant.from_documents(
    docs,
    OpenAIEmbeddings(),
    client=get_qdrant_client(),
    collection_name=KNOWLEDGE_COLLECTION
)

print("Knowledge PDF ingested")
