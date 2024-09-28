from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import dbms

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",  # React app
    "http://127.0.0.1:3000",  # React app (alternative)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class Note(BaseModel):
    name: str
    createdAt: str

@app.get("/notes", response_model=List[Note])
async def get_notes():
    a = dbms.retrieve_data_as_json("notes")
    return a

@app.get("/notifications")
async def get_notifications():
    a = dbms.retrieve_data_as_json("notifications")
    return a

@app.get("/cases")
async def get_cases():
    a = dbms.retrieve_data_as_json("casess")
    return a[:30]

class Case(BaseModel):
    caseNumber: str
    caseID: str
    name: str
    court: str
    judge: str
    verdict: str
    date: str

@app.get("/cases/{case_id}", response_model=Case)
async def get_case(case_id: str):
    cases = dbms.retrieve_data_as_json("cases", {"caseID": case_id})

    if not cases:
        raise HTTPException(status_code=404, detail="Case not found")

    return cases[0]  # Return the first case found

# New endpoint for fetching case details by citation
@app.get("/cases/citation/{citation}")
async def get_case_by_citation(citation: str):
    # Normalize the citation format (if necessary)
    normalized_citation = citation.replace("%20", " ")  # Decode URL encoding

    # Retrieve the case from the database using the normalized citation
    cases = dbms.retrieve_data_as_json("casess", {"citation": normalized_citation})

    if not cases:
        raise HTTPException(status_code=404, detail="Case not found")

    return cases[0]  # Return the first case found

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
