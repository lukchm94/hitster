from fastapi import FastAPI, Request
from fastapi.exception_handlers import http_exception_handler
from starlette.exceptions import HTTPException

from ..routers import health, songs

app = FastAPI()

app.include_router(health.router)
app.include_router(songs.router)


@app.exception_handler(Exception)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return await http_exception_handler(request, exc)
