from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from devopslib.logic import search_wiki
from devopslib.logic import wiki as wikilogic
from devopslib.logic import phrase as wikiphrases
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API.  Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""
    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page and return phrases"""
    result = wikiphrases(name)
    return {"result": result}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Serve the favicon.ico file if requested."""
    return FileResponse("static/favicon.ico")


@app.get("/War")
async def war():
    """Example route for /War"""
    return {"message": "Welcome to the War page!"}


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    """Custom handler for 404 errors."""
    return JSONResponse(
        status_code=404,
        content={"message": f"Route {request.url.path} not found."},
    )


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
