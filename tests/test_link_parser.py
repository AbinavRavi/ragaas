import pytest
from data_ingestion.integrations.web_scraper import LinkParser


@pytest.mark.integrations
def test_scraper():
    url = "https://abinavravi.github.io/about/"
    parser = LinkParser(url)
    output = parser.clean_text()
    print(output)
