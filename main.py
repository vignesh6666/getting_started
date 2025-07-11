from fastapi import FastAPI, Depends,HTTPException
import services,models, Schemas
from db import get_db,engine
from sqlalchemy.orm import Session

app =FastAPI()
@app.get("/books/", response_model= list[Schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
    return services.get_books(db)


@app.post("/books/",response_model=Schemas.Book)
def create_new_book(book:Schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db,book)