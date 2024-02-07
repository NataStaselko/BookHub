from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from fastapi.requests import Request


async def http_exception_handler(request: Request, exc: HTTPException):
    status_code = exc.status_code
    detail = exc.detail
    if status_code == 404:
        return JSONResponse({"error": "Resource not found", "detail": detail}, status_code=status_code)
    return JSONResponse({"error": "Unknown Error", "detail": "An error occurred"}, status_code=status_code)


async def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Validation Error", "errors": exc.errors()},
    )


async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )
