from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    ano_de_publicacion = Column(String)
    isbn = Column(String)

    def __repr__(self) -> str:
        return f"Book(id={self.id},title={self.title},author={self.author},año de publicacion = {self.ano_de_publicacion},ISBN={self.isbn})"


class BooksBaseModel(BaseModel):
    id: int=Field(..., description="The id of the book in our data base.")
    title: str=Field(..., description="The title of the book.")
    author: str=Field(..., description="The author of the book.")
    ano_de_publicacion: str=Field(..., description="The year the book was published.")
    isbn: str =Field(..., description="The ISNB number of the book.")

    class Config:
        from_attributes = True
