from pydantic import BaseModel
from enum import StrEnum


class SingleDocument(BaseModel):
    file: str


class Directory(BaseModel):
    directory_path: str


class DriveLink(BaseModel):
    drive_link: str


class InputDataTypes(StrEnum):
    pdf = ".pdf"
    txt = ".txt"
    doc = ".doc"
    docx = ".docx"


class Status(StrEnum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    UNAVAILABLE = "UNAVAILABLE"


class IngestionResponse(BaseModel):
    status: Status
    message: str
