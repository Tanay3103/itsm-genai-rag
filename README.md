# AI ITSM Copilot – Complete GenAI RAG Demo

This repository is a **fully working demo** of an AI-powered ITSM copilot using:
- OpenAI (LLM + embeddings)
- LangChain
- Local Qdrant
- Streamlit UI

## Features
- Ticket similarity search
- Knowledge PDF fallback
- Intent detection
- Confidence scoring
- Auto ticket creation
- Continuous learning (auto-ingestion)

## Run Instructions

docker run -p 6333:6333 qdrant/qdrant

pip install -r requirements.txt

export OPENAI_API_KEY=your_key

python ingestion/load_csv_tickets.py
python ingestion/load_pdf_knowledge.py

streamlit run app.py
