# print(wiki())

from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as wikilogic, search_wiki, phrase as wikiphrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call/Search for Wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia Page to search in wikipedia"""

    result = wikilogic(name)
    return {"result": result}


@app.get("/phrases/{name}")
async def phrases(name: str):
    """Retrieve wikipedia Page and return phrases"""
    print(f"Passed in name : {name}")
    result = wikiphrases(name)
    print(f"result: {result}")
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
