from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Topic(Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    importance_level = Column(Integer)

    videos = relationship("Video", back_populates="topic")

class Video(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, unique=True)
    topic_id = Column(Integer, ForeignKey('topics.id'))
    watch_reminder = Column(Integer)  # Store reminder time in minutes

    topic = relationship("Topic", back_populates="videos")

class UserPreference(Base):
    __tablename__ = 'user_preferences'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    preferred_importance_level = Column(Integer)  # User's preferred importance level for videos
    daily_reminder_time = Column(String)  # Time for daily reminders (e.g., "09:00")