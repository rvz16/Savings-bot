from pydantic import BaseModel
from typing import List, Optional

class TopicBase(BaseModel):
    title: str
    description: Optional[str] = None
    importance_level: int

class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    id: int

    class Config:
        orm_mode = True

class VideoBase(BaseModel):
    title: str
    url: str
    topic_id: int
    importance_level: int

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True

class UserPreferenceBase(BaseModel):
    user_id: int
    video_id: int
    reminder_time: str

class UserPreferenceCreate(UserPreferenceBase):
    pass

class UserPreference(UserPreferenceBase):
    id: int

    class Config:
        orm_mode = True

class Reminder(BaseModel):
    video_id: int
    reminder_time: str

class ReminderResponse(BaseModel):
    message: str
    reminders: List[Reminder]