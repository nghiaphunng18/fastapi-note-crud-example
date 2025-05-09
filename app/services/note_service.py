from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteRequest, NoteResponse
from typing import List

class NoteService:
    def get_notes(self, db: Session, skip: int, limit: int) -> List[Note]:
        return db.query(Note).offset(skip).limit(limit).all()

    def get_note(self, db: Session, note_id: int) -> Note:
        return db.query(Note).filter(Note.id == note_id).first()

    def create_note(self, db: Session, note: NoteRequest) -> Note:
        db_note = Note(**note.dict())
        db.add(db_note)
        db.commit()
        db.refresh(db_note)
        return db_note

    def update_note(self, db: Session, note_id: int, note: NoteRequest) -> Note:
        db_note = self.get_note(db, note_id)
        if not db_note:
            return None
        for key, value in note.dict().items():
            setattr(db_note, key, value)
        db.commit()
        db.refresh(db_note)
        return db_note

    def delete_note(self, db: Session, note_id: int) -> bool:
        db_note = self.get_note(db, note_id)
        if not db_note:
            return False
        db.delete(db_note)
        db.commit()
        return True