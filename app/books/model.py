from sqlalchemy import Column, String, Integer, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.association.book_genre import book_genre_association


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    num_pages = Column(Integer, nullable=False)
    is_available = Column(Boolean, nullable=False, default=True)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    reservations = relationship('Reservation')
    genres = relationship('Genre', secondary=book_genre_association, back_populates='books')
