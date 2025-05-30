from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    entry_id = Column(Integer, ForeignKey("mood_entries.id"))

    entry = relationship("MoodEntry", back_populates="activities")

    def __repr__(self):
        return f"<Activity(id={self.id}, name='{self.name}')>"
