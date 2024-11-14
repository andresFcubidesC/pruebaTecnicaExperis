from exceptiongroup import catch
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Query
from sqlalchemy import delete
from sqlalchemy.orm import Session

from Repositorys.schemas.booksSchema import BooksBaseModel
from controllers.models.booksResponse import BooksResponse, BookRequest
from infrastructure.database import get_db
from services.libraryService import get_all_books, get_books_by_filters, patch_book, delete_book, \
    create_book_service

router = APIRouter()

@router.get("/books",response_model=BooksResponse)
async def get_books(db: Session=Depends(get_db)) -> BooksResponse:
    try:
        books = get_all_books(db)
        if not books:
            return BooksResponse(success=False, content="No books found.")
        content = [BooksBaseModel.model_validate(book) for book in books]
        return BooksResponse(success=True, content=content)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Something went wrong. Please contact the applicant to see what may be wrong."+str(e))
    finally:
        db.close()

@router.get("/books_by_author_or_year",response_model=BooksResponse)
async def get_books(db: Session=Depends(get_db),
                    author:str=Query(None,description="type the author of the book or books you are looking for"),
                    year:int=Query(None,description="type the year of the book or books you are looking for"),
                    title:str=Query(None,description="type the title of the books you are looking for")) -> BooksResponse:
    try:
        books = get_books_by_filters(db,author,year,title)
        if not books:
            raise HTTPException(status_code=404, detail="Book not found")
        content = [BooksBaseModel.model_validate(book) for book in books]
        return BooksResponse(success=True, content=content)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Something went wrong. Please contact the applicant to see what may be wrong."+str(e))
    finally:
        db.close()

@router.post("/create_book",
             response_model=BooksResponse,
              summary="this URL creats a new book",
              description="This endpoint allows you to created a book by its ID. The response will indicate whether the operation was successful or not, Keep in mind that you may create two identical books. The ID will change, but the information will remain the same.",
              response_description="The response will indicate whether the book was successfully created or not, along with the content details.",
              )
async def post_books(book:BookRequest,db: Session=Depends(get_db)) -> BooksResponse:
    try:
        book = create_book_service(db,book)
        content = BooksBaseModel.model_validate(book)
        return BooksResponse(success=True, content=content)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Something went wrong. Please contact the applicant to see what may be wrong."+str(e))
    finally:
        db.close()

@router.patch("/book/{id}",
              response_model=BooksResponse,
              summary="this URL updates a book by id",
              description="This endpoint allows you to update a book by its ID. If the book is not found, it will raise an error. The response will indicate whether the operation was successful or not, you can use one or more files of the BooksbaseModel for the filds you whant to update",
              response_description="The response will indicate whether the book was successfully deleted or not, along with the content details.",
              )
async def update_books(id:int,updated_data: dict,db: Session=Depends(get_db)) -> BooksResponse:
    try:
        book = patch_book(db,id,updated_data)

        content = BooksBaseModel.model_validate(book)
        return BooksResponse(success=True, content=content)
    except Exception as e:
        db.rollback()
        db.close()
        raise HTTPException(status_code=400, detail="Something went wrong. Please contact the applicant to see what may be wrong."+str(e))
    finally:
        db.close()

@router.delete("/book/{id}",
               response_model=BooksResponse,
               summary="this URL delete a book by id",
               description="This endpoint allows you to delete a book by its ID. If the book is not found, it will raise an error. The response will indicate whether the operation was successful or not.",
               response_description="The response will indicate whether the book was successfully deleted or not, along with the content details.",)
async def get_books(id:int,db: Session=Depends(get_db)) -> BooksResponse:
    try:
        books_deleted = delete_book(db,id)
        return BooksResponse(success=True, content=f"the number of books deleted were {books_deleted}")
    except Exception as e:
        db.rollback()
        db.close()
        raise HTTPException(status_code=400, detail="Something went wrong. Please contact the applicant to see what may be wrong."+str(e))
    finally:
        db.close()




