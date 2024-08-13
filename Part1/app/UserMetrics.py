from pydantic import BaseModel
from typing import Optional


class UserMetrics(BaseModel):
    user_id: int
    device_id: Optional[str]
    talked_time: Optional[float]
    microphone_used: Optional[bool]
    speaker_used: Optional[bool]
    voice_sentiment: Optional[float]
    time_recorded: str
