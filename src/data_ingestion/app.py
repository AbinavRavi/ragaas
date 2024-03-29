from fastapi import FastAPI

app = FastAPI("Ingestion endpoints")


@app.get("/document")
def get_document():
    pass
