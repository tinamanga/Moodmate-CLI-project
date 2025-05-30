from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class MoodEntry(Base):
    __tablename__ = 'mood_entries'

    id = Column(Integer, primary_key=True)
    mood = Column(String)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="entries")
    activities = relationship("Activity", back_populates="entry")

    def __repr__(self):
        return f"<MoodEntry(id={self.id}, mood='{self.mood}', date={self.date})>"
