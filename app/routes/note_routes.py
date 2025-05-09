from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.note import NoteRequest, NoteResponse
from app.services.note_service import NoteService
from app.dependencies.db import get_db

router = APIRouter(prefix="/notes", tags=["notes"])

# get list note
@router.get("/", response_model=List[NoteResponse])
def get_notes(
    skip: int = Query(0, ge=0, description="Number of records skipped"),
    limit: int = Query(10, ge=1, le=100, description="Number of records skipped"),
    db: Session = Depends(get_db)
):
    service = NoteService()
    notes = service.get_notes(db, skip, limit)
    return notes

# get note by id
@router.get("/{id}", response_model=NoteResponse)
def get_note(id: int, db: Session = Depends(get_db)):
    service = NoteService()
    note = service.get_note(db, id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

# create note
@router.post("/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteRequest, db: Session = Depends(get_db)):
    service = NoteService()
    db_note = service.create_note(db, note)
    return db_note

# update note
@router.put("/{id}", response_model=NoteResponse)
def update_note(id: int, note: NoteRequest, db: Session = Depends(get_db)):
    service = NoteService()
    db_note = service.update_note(db, id, note)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# delete note
@router.delete("/{id}", status_code=204)
def delete_note(id: int, db: Session = Depends(get_db)):
    service = NoteService()
    success = service.delete_note(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return None