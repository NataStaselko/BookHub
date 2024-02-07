from sqlalchemy import Column, DateTime, Integer, ForeignKey, Boolean
from sqlalchemy.sql import func
from datetime import timedelta
from app.db.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    time_start = Column(DateTime(timezone=True), server_default=func.now())
    time_end = Column(DateTime(timezone=True), server_default=func.now() + timedelta(days=10))
    isActive = Column(Boolean, default=True)
