from models import Book
from sqlalchemy.orm import Session
from Schemas import BookCreate


def create_book(db: Session, data:BookCreate):
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance



def get_books(db: Session):
    return db.query(Book).all()


