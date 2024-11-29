from typing import List, Type, Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from repositories.schemas.booksSchema import Books


def get_books_from_dataBased(db:Session):
    return db.query(Books).all()

def creat_book_into_dataBased(db:Session,book:Books):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books_db_by_filter(db:Session,author:Optional[str]=None,year:Optional[int]=None,tilte:Optional[str]=None):
    query = db.query(Books)
    if author:
        query = query.filter(Books.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Books.ano_de_publicacion == str(year))
    if tilte:
        query = query.filter(Books.title.ilike(f"%{tilte}%"))

    return query.all()

def patch_book_by_id(db: Session, id: int, updated_data: dict):
    book = db.query(Books).filter(Books.id == id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in updated_data.items():
        if value is not None:
            setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book

def delete_book_by_id(db:Session,id:int)->int:
    result = db.query(Books).filter(Books.id == id).delete(synchronize_session=False)
    db.commit()
    return result
