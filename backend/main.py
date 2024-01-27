from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated, List

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class DiapersBase(BaseModel):
    time: str
    date: str
    content: str


class FeedingBase(BaseModel):
    time: str
    type: str
    amount: int
    date: str


class TaskBase(BaseModel):
    name: str
    is_done: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/api/v1/tasks/")
def get_tasks(db: db_dependency):
    result = db.query(models.Tasks).filter(models.Tasks.is_finished == False).all()
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="no info found")
    return result


@app.get("/api/v1/feeding/")
def get_feedings(db: db_dependency):
    result = db.query(models.Feeding).all()
    if not result:
        raise HTTPException(status_code=404, detail="no info found")
    return result


@app.get("/api/v1/diapers/")
async def get_diaper_changes(db: db_dependency):
    result = db.query(models.Diapers).all()
    if not result:
        raise HTTPException(status_code=404, detail="no info found")
    return result


@app.post("/api/v1/diapers/")
async def add_diaper_change(details: dict, db: db_dependency):
    change_diaper = models.Diapers(date=details["date"], time=details["time"], content=details["content"])
    db.add(change_diaper)
    db.commit()


@app.post("/api/v1/feeding/")
def add_feeding_time(details: dict, db: db_dependency):
    feeding_time = models.Feeding(date=details["date"], time=details["time"], amount=details["amount"],
                                  type=details["type"])
    db.add(feeding_time)
    db.commit()


@app.post("/api/v1/tasks/")
def add_task(details: dict, db: db_dependency):
    task = models.Tasks(name=details["name"], is_finished=False)
    db.add(task)
    db.commit()


@app.post("/api/v1/complete_task/{task_id}")
def remove_completed_task(task_id: int, db: db_dependency):
    result = db.query(models.Tasks).filter(models.Tasks.id == task_id).update({models.Tasks.is_finished: True})
    db.commit()
