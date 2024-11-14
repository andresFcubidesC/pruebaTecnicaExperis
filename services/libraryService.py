from typing import List, Type, Optional

from sqlalchemy import delete
from sqlalchemy.orm import Session

from Repositorys.libraryRepository import get_books_from_dataBased, creat_book_into_dataBased, get_books_db_by_filter, \
    patch_book_by_id, delete_book_by_id
from Repositorys.schemas.booksSchema import Books
from controllers.models.booksResponse import BookRequest


def get_all_books(db:Session):
    books=get_books_from_dataBased(db)
    return books

def create_book_service(db:Session,book:BookRequest):
    db_book=Books(title=book.title,
                  author=book.author,
                  ano_de_publicacion=book.ano_de_publicacion,
                  isbn=book.isbn)
    book=creat_book_into_dataBased(db=db,book=db_book)
    return book

def get_books_by_filters(db:Session,author:Optional[str]=None,year:Optional[int]=None,title:Optional[str]=None):
    book=get_books_db_by_filter(db=db,author=author,year=year,tilte=title)
    return book

def patch_book(db:Session,id:int,updated_data:dict):
    book=patch_book_by_id(db,id,updated_data)
    return book

def delete_book(db:Session,id:int)->int:
    number_of_books_deleted=delete_book_by_id(db,id)
    return number_of_books_deleted





