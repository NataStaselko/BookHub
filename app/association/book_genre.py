from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.database import Base

book_genre_association = Table(
    'book_genre_association',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)
