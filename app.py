from fastapi import FastAPI, staticfiles

app = FastAPI()

app.mount("/views", staticfiles.StaticFiles(directory="views"), name="views")
