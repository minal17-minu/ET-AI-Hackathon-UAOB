from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
import uvicorn
from typing import List

# Mocking the RAG pipeline for the hackathon prototype
# In a production environment, this connects to FAISS/ChromaDB and an LLM

app = FastAPI(title="Industrial Knowledge API", version="1.0")

class Query(BaseModel):
    question: str

class ResponseData(BaseModel):
    answer: str
    sources: List[str]

# In-memory mock database representing the Vector Store
MOCK_KNOWLEDGE_BASE = {
    "pump failure": "Check the impeller clearance and bearing lubrication. Source: Maintenance Manual P-204.",
    "pressure valve": "Standard operating pressure is 450 PSI. Do not exceed 500 PSI. Source: Safety Guideline V-12.",
    "o-ring replacement": "Ensure system is depressurized before replacing O-rings. Use Viton for high temp. Source: SOP-99."
}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Simulates document ingestion, chunking, and vector embedding
    return {"filename": file.filename, "status": "Successfully ingested and indexed."}

@app.post("/ask", response_model=ResponseData)
async def ask_copilot(query: Query):
    question = query.question.lower()
    
    # Simulating similarity search O(1) for prototype speed
    for key, data in MOCK_KNOWLEDGE_BASE.items():
        if key in question:
            return ResponseData(
                answer=data.split("Source:")[0].strip(),
                sources=[data.split("Source:")[1].strip()]
            )
            
    return ResponseData(
        answer="I could not find specific maintenance parameters for that query in the current document corpus.",
        sources=[]
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
