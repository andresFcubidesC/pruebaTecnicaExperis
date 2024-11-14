from typing import Union

from pydantic import BaseModel

from Repositorys.schemas.booksSchema import BooksBaseModel


class BooksResponse(BaseModel):
    success: bool
    content: Union[str, dict, list[BooksBaseModel],BooksBaseModel, None]

    class Config:
        from_attributes = True

class BookRequest(BaseModel):
    title: str
    author: str
    ano_de_publicacion: str
    isbn: str

    class Config:
        from_attributes = True