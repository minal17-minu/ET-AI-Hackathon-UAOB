# ET-AI-Hackathon-UAOB
 Unified Asset & Operations Brain (UAOB)
Team Solo Submission by MINAL NATHA WAGHMODE
Target Problem: Problem 8 - AI for Industrial Knowledge Intelligence
Tech Stack:** Python, FastAPI, Streamlit, LangChain, FAISS

---

## 1. Executive Summary
The Unified Asset & Operations Brain (UAOB) is an AI-powered intelligence platform designed to eliminate the fragmentation of industrial knowledge. Currently, professionals in asset-intensive industries waste 35% of their working hours searching for critical information across disconnected document systems. This fragmentation is a direct contributor to 18-22% of unplanned downtime in Indian heavy industry. 

UAOB solves this by ingesting heterogeneous industrial documents (P&IDs, maintenance records, safety procedures) and creating a centralized, queryable Retrieval-Augmented Generation (RAG) system. It serves as a continuous, accessible expert copilot at the point of need.

## 2. Business Impact
* **Reduced Unplanned Downtime:** Instantly connects work order history and OEM manuals to generate predictive maintenance recommendations.
* **Knowledge Preservation:** Captures the implicit knowledge of the retiring workforce and makes it available to new engineers.
* **Improved Compliance:** Automatically maps regulatory requirements (e.g., Factory Act, OISD) against current procedures to flag compliance gaps.

## 3. Technical Architecture
The UAOB platform is built on a modern, scalable microservices architecture optimized for speed and semantic accuracy:
* **Frontend UI (Streamlit):** Provides a mobile-responsive, conversational interface for field technicians.
* **Backend API (FastAPI):** Orchestrates high-speed routing between the user query, the vector database, and the LLM.
* **Data Ingestion & Vector Storage:** Simulates unstructured PDF processing and semantic search using vector embeddings to understand the *meaning* of a maintenance query, not just keyword matching.

## 4. How to Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Start the Backend API: `uvicorn main:app --reload`
3. Start the Frontend UI: `streamlit run app.py`
1. Install dependencies: `pip install -r requirements.txt`
2. Start the Backend API: `uvicorn main:app --reload`
3. Start the Frontend UI: `streamlit run app.py`
