
from fastapi import FastAPI
from fastapi.testclient import TestClient


from controllers.libraryController import router

# Set up FastAPI test client with the router
app = FastAPI()
app.include_router(router)

client = TestClient(app)


# Tests of endpoint to get all books, mocking service layer
def test_get_books(mocker):
    mock_books = [
        {
            "id": 1,
            "title": "test1",
            "author": "author test 1",
            "ano_de_publicacion": "2024",
            "isbn": "456asd"
        },
        {
            "id": 2,
            "title": "test2",
            "author": "author test 2",
            "ano_de_publicacion": "2024",
            "isbn": "476asd"
        }
    ]
    mock_get_books = mocker.patch("controllers.libraryController.get_all_books", return_value=mock_books)
    result = client.get("/books")

    assert result.json() == {
        "success": True,
        "content": mock_books
    }
    assert result.status_code == 200


# Tests of endpoint to get books by filter, mocking service layer
def test_get_books_by_filter(mocker):
    mock_books = [
        {
            "id": 1,
            "title": "test1",
            "author": "author test 1",
            "ano_de_publicacion": "2024",
            "isbn": "456asd"
        },
        {
            "id": 2,
            "title": "test2",
            "author": "author test 2",
            "ano_de_publicacion": "2024",
            "isbn": "476asd"
        }
    ]
    mock_get_books = mocker.patch("controllers.libraryController.get_books_by_filters", return_value=mock_books)
    result = client.get("/books_by_author_or_year")

    assert result.json() == {
        "success": True,
        "content": mock_books
    }
    assert result.status_code == 200


def test_update_book(mocker):
    mock_book = {
            "id": 1,
            "title": "test update",
            "author": "author test 1",
            "ano_de_publicacion": "2024",
            "isbn": "456asd"
        }

    mock_post_books = mocker.patch("controllers.libraryController.patch_book", return_value=mock_book)
    result = client.patch("/book/1", json={"title": "test update"})

    assert result.json() == {
        "success": True,
        "content": mock_book
    }
    assert result.status_code == 200

def test_created_book(mocker):
    mock_book = {
            "id": 34,
            "title": "test1",
            "author": "author test 1",
            "ano_de_publicacion": "2024",
            "isbn": "456asd"
        }

    mock_post_books = mocker.patch("controllers.libraryController.create_book_service", return_value=mock_book)
    result = client.post("/create_book",json=mock_book)
    print(result.json())

    assert result.json() == {
        "success": True,
        "content": mock_book
    }
    assert result.status_code == 200

def test_delete_book(mocker):
    mock_string="the number of books deleted were 1"

    mock_post_books = mocker.patch("controllers.libraryController.delete_book", return_value=1)
    result = client.delete("/book/34")
    print(result.json())

    assert result.json() == {
        "success": True,
        "content": mock_string
    }
    assert result.status_code == 200
