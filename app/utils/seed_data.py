# create data
from sqlalchemy.orm import Session
from app.models.note import Note
from faker import Faker

def seed_data(db: Session):
    fake = Faker()
    # delete old data
    db.query(Note).delete()
    # fake 20 data
    for _ in range(20):
        note = Note(
            title=fake.sentence(nb_words=6),
            content=fake.paragraph(nb_sentences=3),
            created_at=fake.date_time_this_year()
        )
        db.add(note)
    db.commit()