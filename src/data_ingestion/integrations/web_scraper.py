import aiohttp
import asyncio
from bs4 import BeautifulSoup


class LinkParser:
    def __init__(self, url: str) -> None:
        self.url = url

    async def fetch_data_page(self, url) -> str:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.text()
                    return data
        except Exception as e:
            raise e

    def fetch_all_pages(self) -> str:
        text = []
        current_page = self.url
        while current_page:
            data = asyncio.run(self.fetch_data_page(current_page))

            soup = BeautifulSoup(data, "html.parser")
            for link in soup.find_all("a", href=True):
                if link["href"].startswith("/"):
                    current_page = f"{self.url}{link['href']}"
                    break
                else:
                    current_page = None
            for script in soup(["script", "style"]):
                script.extract()  # rip it out
            text.extend(soup.get_text())

        return "".join(text)

    def clean_text() -> str:
        pass
