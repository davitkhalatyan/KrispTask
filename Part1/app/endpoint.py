from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schema import SessionLocal, engine, Metrics, Base
from UserMetrics import UserMetrics

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/metrics/")
async def create_metrics(metric: UserMetrics, db: Session = Depends(get_db)):
    db_metric = Metrics(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric
