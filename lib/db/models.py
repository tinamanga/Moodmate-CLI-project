from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.base import Base

# user model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    entries = relationship("MoodEntry", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

# mood entry model

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
