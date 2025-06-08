import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links_and_text(url, domain=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)

    if "text/html" not in response.headers.get("Content-Type", ""):
        return [], []

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract visible paragraphs
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]

    # Collect internal links
    links = set()
    for tag in soup.find_all("a", href=True):
        href = tag['href']
        joined = urljoin(url, href)
        parsed = urlparse(joined)
        if domain and domain in parsed.netloc:
            links.add(joined)

    return paragraphs, list(links)
