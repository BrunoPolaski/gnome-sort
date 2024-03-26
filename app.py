from fastapi import FastAPI, staticfiles
from pydantic import BaseModel
from algorithms import yield_gnome_sort


class SortRequest(BaseModel):
    array: list


app = FastAPI()

app.mount("/views", staticfiles.StaticFiles(directory="views"), name="views")


@app.post("/sort")
async def sort(data: SortRequest):
    indexes = [data for data in yield_gnome_sort(data.array)]
    return indexes
