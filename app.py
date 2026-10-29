from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from service.router import api_router

app = FastAPI(
    title="PunkAPI",
    docs_url="/docs",  # Swagger UI будет доступен здесь
    openapi_url="/api/v3/openapi.json",  # Спецификация для Swagger
    version="3.0",
    summary="REST API serving as a digital archive of BrewDog's DIY Dog beer catalog",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # allow all sources
    allow_methods=["GET"], # allow only GET method
    allow_headers=["*"], # allow all header
)

app.include_router(api_router, prefix="/api/v3")


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTP Error",
            "message": exc.detail,
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": str(exc),
        },
    )


@app.get("/api/v3")
async def root():
    return {
        "name": "PunkAPI",
        "version": "3.0",
        "status": "healthy",
        "documentation": "https://punkapi.dev/docs",
        "source": "https://github.com/alxiw/punkapi",
        "author": "alxiw",
        "email": "alxiw@outlook.com",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="debug")
