import pytz
from sqlalchemy import Column, Integer, String, DateTime
from app.config.database import Base
from datetime import datetime

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(pytz.UTC))