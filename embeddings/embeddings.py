# --- Embedding factory with fallback ---
import logging

import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings

from config.config import OPENAI_MODEL as EMBEDDING_MODEL

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@st.cache_resource
def get_embeddings():
    """
    Try OpenAI embeddings first, fallback to local HF embeddings if unavailable.
    """
    try:
        logger.info("Trying OpenAI embeddings...")

        embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL, chunk_size=100)

        # Smoke test to force API call
        embeddings.embed_query("health check")

        logger.info("Using OpenAI embeddings")
        return embeddings

    except Exception as e:
        logger.warning("OpenAI embeddings unavailable, falling back to local model")
        logger.warning(f"Reason: {e}")

        logger.info("Loading HuggingFace embeddings (all-MiniLM-L6-v2)")
        return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
