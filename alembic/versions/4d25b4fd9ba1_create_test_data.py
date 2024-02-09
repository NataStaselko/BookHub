"""Create test data

Revision ID: 4d25b4fd9ba1
Revises: 
Create Date: 2024-02-08 17:08:29.135427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d25b4fd9ba1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('login', sa.String, nullable=False),
                    )

    op.create_table('authors',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('first_name', sa.String, nullable=False),
                    sa.Column('last_name', sa.String, nullable=False),
                    sa.Column('avatar', sa.String),
                    )

    op.create_table('books',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('title', sa.String, nullable=False),
                    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
                    sa.Column('num_pages', sa.Integer, nullable=False),
                    sa.Column('author_id', sa.Integer, sa.ForeignKey('authors.id'), nullable=False),
                    sa.Column('is_available', sa.Boolean, nullable=False, default=True),
                    )

    op.create_table('genres',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('name', sa.String, nullable=False),
                    )

    op.create_table('book_genre_association',
                    sa.Column('book_id', sa.Integer, sa.ForeignKey('books.id'), primary_key=True),
                    sa.Column('genre_id', sa.Integer, sa.ForeignKey('genres.id'), primary_key=True),
                    )

    op.create_table('reservations',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('book_id', sa.Integer, sa.ForeignKey('books.id'), nullable=False),
                    sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
                    sa.Column('time_start', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
                    sa.Column('time_end', sa.DateTime(timezone=True),
                              server_default=sa.text('CURRENT_TIMESTAMP + INTERVAL \'10 days\'')),
                    sa.Column('is_active', sa.Boolean, default=True),
                    )

    op.execute("""            
            INSERT INTO users (login) 
            VALUES 
                 ('user1'), 
                 ('user2'), 
                 ('user3');
            
            INSERT INTO authors (first_name, last_name, avatar) 
            VALUES 
                 ('John', 'Doe','john_avatar.jpg'),
                 ('Jane', 'Fox', 'jane_avatar.jpg'),
                 ('Alice', 'Smith', 'alice_avatar.jpg');
            
            INSERT INTO books (title, price, num_pages, author_id, is_available)
            VALUES 
                ('The Great Book', 19.99, 320, 1, true),
                ('Fantastic Stories', 29.40, 300, 3, true),
                ('Programming 101', 14.20, 400, 2, true);
                
            INSERT INTO genres (name) 
            VALUES 
                 ('Fiction'), 
                 ('Non-Fiction'),
                 ('Science Fiction');
                 
            INSERT INTO book_genre_association (book_id, genre_id) 
            VALUES 
                 (1, 1), 
                 (2, 2),
                 (3, 3);
                 
            INSERT INTO reservations (book_id, user_id, is_active) 
            VALUES 
                 (1, 3, true), 
                 (2, 2, true),
                 (3, 1, true);
        """)


def downgrade():
    op.drop_table('reservations')
    op.drop_table('book_genre_association')
    op.drop_table('books')
    op.drop_table('genres')
    op.drop_table('authors')
    op.drop_table('users')
