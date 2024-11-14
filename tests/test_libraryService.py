from typing import List
from unittest.mock import MagicMock

import services.libraryService
from Repositorys.schemas.booksSchema import Books
from controllers.models.booksResponse import BookRequest


def test_get_all_books(mocker):
    mock_books:List[Books] = [
        Books(id=1, title='Book1', author='Author1', ano_de_publicacion=2024, isbn="456asd"),
        Books(id=2, title='Book2', author='Author2', ano_de_publicacion=2024, isbn="457asd"),
    ]
    mock_repository=mocker.patch("services.libraryService.get_books_from_dataBased", return_value=mock_books)
    fake_session = MagicMock()
    actual=services.libraryService.get_all_books(fake_session)

    assert mock_books == actual



def test_create_book_service(mocker):
    mock_books:Books = Books(id=1, title='Book1', author='Author1', ano_de_publicacion="2024", isbn="456asd")
    mock_book_request=BookRequest(title='Book1', author='Author1', ano_de_publicacion="2024", isbn="456asd")

    mock_repository=mocker.patch("services.libraryService.creat_book_into_dataBased", return_value=mock_books)
    fake_session = MagicMock()
    actual=services.libraryService.create_book_service(fake_session(),mock_book_request)

    assert mock_books == actual

def test_get_books_by_filters(mocker):
    mock_books:Books = Books(id=1, title='Book1', author='Author1', ano_de_publicacion="2024", isbn="456asd")
    mock_author='Author1'
    mock_year=2024
    mock_title='Book1'

    mock_repository=mocker.patch("services.libraryService.get_books_db_by_filter", return_value=mock_books)
    fake_session = MagicMock()
    actual=services.libraryService.get_books_by_filters(fake_session(),year=mock_year,author=mock_author,title=mock_title)

    assert mock_books == actual

def test_patch_book(mocker):
    mock_books:Books = Books(id=1, title='Book1', author='Author1', ano_de_publicacion="2024", isbn="456asd")
    mock_id=1
    update_data={"title":"book1"}

    mock_repository=mocker.patch("services.libraryService.patch_book_by_id", return_value=mock_books)
    fake_session = MagicMock()
    actual=services.libraryService.patch_book_by_id(fake_session(),mock_id,update_data)

    assert mock_books == actual

def test_delete_book(mocker):
    mock_id=1

    mock_repository=mocker.patch("services.libraryService.delete_book_by_id", return_value=1)
    fake_session = MagicMock()
    actual=services.libraryService.delete_book(fake_session(),mock_id)

    assert 1 == actual
