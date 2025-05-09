from fastapi import FastAPI
from app.routes.note_routes import router
from app.utils.seed_data import seed_data
from app.config.database import engine, Base
from app.dependencies.db import get_db
import uvicorn

app = FastAPI(title="Notes FastAPI Tutorial")

Base.metadata.create_all(bind=engine)

# add routes
app.include_router(router)

# fake data
@app.on_event("startup")
def startup_event():
    db = next(get_db())
    seed_data(db)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)