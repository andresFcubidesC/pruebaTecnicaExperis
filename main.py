import os
from contextlib import asynccontextmanager

import uvicorn

from controllers import libraryController

from fastapi import FastAPI, Depends

from infrastructure.database import init_db, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    app.include_router(libraryController.router, dependencies=[Depends(get_db)])
    yield



app = FastAPI(lifespan=lifespan,
              title="library API",
              description="This API allows you to manage a collection of books. You can create, update, delete, and search for books. Please keep in mind that 1)if you create two identical books, the ID will change, but the information will remain the same. 2) you can look a book by its author, title or year using the /books_by_author_or_year url, or you can fetch all the books using /books",
              version="1.0.0"
              )


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT_MICROSERVICE")))
