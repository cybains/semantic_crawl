
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links_and_text(url, domain):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        # Extract all paragraph text
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

        # Collect internal links
        base = "{0.scheme}://{0.netloc}".format(urlparse(url))
        hrefs = [a["href"] for a in soup.find_all("a", href=True)]
        links = [urljoin(base, h) for h in hrefs if domain in urljoin(base, h)]

        return paragraphs, links

    except Exception as e:
        print(f"❌ Error: {e}")
        return [], []
