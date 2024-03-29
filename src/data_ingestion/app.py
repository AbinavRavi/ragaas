from fastapi import FastAPI

app = FastAPI("Ingestion endpoints")


@app.post("/document")
async def get_document(file_path: str):
    pass
