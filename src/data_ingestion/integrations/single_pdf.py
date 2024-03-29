from pypdf import PdfReader


class SinglePdfExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = PdfReader(self.file_path)

    def extract_text(self):
        text = ""
        for page in self.reader.pages:
            text += page.extract_text()
        return text
