from fastapi import FastAPI, Request
from pydantic import BaseModel
import spacy

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

class OCRRequest(BaseModel):
    text: str

@app.post("/parse")
async def parse_text(payload: OCRRequest):
    doc = nlp(payload.text)
    entities = {ent.label_: ent.text for ent in doc.ents}
    return entities
