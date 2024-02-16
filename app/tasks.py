import os
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv
from datetime import datetime
from app.db.database import SessionLocal
from app.reservations.model import Reservation
from app.books.model import Book
from app.genres.model import Genre
from app.association.book_genre import book_genre_association

load_dotenv('.env')

celery = Celery('tasks')
celery.conf.broker_url = os.environ.get('CELERY_BROKER_URL')
celery.conf.result_backend = os.environ.get('CELERY_RESULT_BACKEND')
celery.autodiscover_tasks(['app.tasks'])

celery.conf.beat_schedule = {
    'check_expired_reservations': {
        'task': 'app.tasks.check_expired_reservations',
        'schedule': crontab(minute='*'),
    },
}


@celery.task(name='app.tasks.check_expired_reservations')
def check_expired_reservations():
    session = SessionLocal()
    try:
        with session.begin():
            reservations = session.query(Reservation).filter(Reservation.time_end <= datetime.now()).all()
            if reservations:
                for reservation in reservations:
                    reservation.is_active = False
                    book = session.query(Book).filter(Book.id == reservation.book_id).first()
                    book.is_available = True
                    session.commit()
    except Exception as e:
        print(f"Error in task: {e}")
    finally:
        session.close()




