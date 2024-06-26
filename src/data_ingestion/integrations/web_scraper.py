import aiohttp
import asyncio
from bs4 import BeautifulSoup


class LinkParser:
    def __init__(self, url: str) -> None:
        self.url = url

    async def __fetch_data_page(self, url) -> str:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.text()
                    return data
        except Exception as e:
            raise e

    async def __fetch_all_pages(self) -> str:
        text = []
        current_page = self.url
        while current_page:
            data = await self.__fetch_data_page(current_page)

            soup = BeautifulSoup(data, "html.parser")
            for link in soup.find_all("a", href=True):
                if link["href"].startswith("/"):
                    current_page = f"{self.url}{link['href']}"
                else:
                    current_page = None
            for script in soup(["script", "style"]):
                script.extract()  # rip it out
            text.extend(soup.get_text())

        return "".join(text)

    def clean_text(self) -> str:
        text = asyncio.run(self.__fetch_all_pages())
        return text
