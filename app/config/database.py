from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3307/notes_fastapi_tutorial"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# model SQLAlchemy
Base = declarative_base()