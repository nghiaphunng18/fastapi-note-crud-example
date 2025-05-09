from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

# dto create/update note
class NoteRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Title of note")
    content: str = Field(..., min_length=1, description="Content of note")

# dto response note
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True  # Convert from SQLAlchemy object to Pydantic