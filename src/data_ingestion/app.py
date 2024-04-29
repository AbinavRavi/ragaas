from fastapi import FastAPI
from types.ingestion import SingleDocument, Directory, WebLink, IngestionResponse
from integrations.web_scraper import LinkParser

app = FastAPI("Ingestion endpoints")


@app.post("/document")
async def get_document(document: SingleDocument) -> IngestionResponse:
    pass


@app.post("/local_directory")
def get_documents_directory(directory_path: Directory) -> IngestionResponse:
    pass


@app.post("/drive")
def get_documents_from_drive(drive_link: str) -> IngestionResponse:
    pass


@app.post("/web_link")
def scrape_web_link(link: WebLink) -> IngestionResponse:
    url = WebLink.web_link
    parser = LinkParser(url)
    text = parser.clean_text()
    response = {"status": "SUCCESS", "message": text}
    return response
