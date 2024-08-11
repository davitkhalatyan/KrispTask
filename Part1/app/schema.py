from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from database import Base


class Metrics(Base):
    __tablename__ = 'user_metrics'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    session_id = Column(String)
    device_id = Column(String)
    talked_time = Column(Float, nullable=True)
    microphone_used = Column(Boolean, nullable=True)
    speaker_used = Column(Boolean, nullable=True)
    voice_sentiment = Column(Float, nullable=True)
    timestamp = Column(DateTime)
