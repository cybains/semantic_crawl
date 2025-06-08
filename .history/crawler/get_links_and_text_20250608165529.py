# crawler/get_links_and_text.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links_and_text(url, domain=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)

    if "text/html" not in response.headers.get("Content-Type", ""):
        return [], []

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove non-content elements
    for tag in soup(["footer", "nav", "script", "style", "header"]):
        tag.decompose()

    # Get breadcrumbs if present
    breadcrumbs = soup.select(".breadcrumb li")
    breadcrumb_text = " > ".join(item.get_text(strip=True) for item in breadcrumbs) if breadcrumbs else None

    # Extract structured content in order
    content_tags = soup.select("h1, h2, h3, p, li")
    paragraphs = []

    if breadcrumb_text:
        paragraphs.append(f"Breadcrumbs: {breadcrumb_text}")

    title = soup.title.string.strip() if soup.title else None
    if title:
        paragraphs.append(f"Title: {title}")

    for tag in content_tags:
        text = tag.get_text(strip=True)
        if text and len(text) > 1:
            paragraphs.append(text)

    # Collect internal links
    links = set()
    for tag in soup.find_all("a", href=True):
        href = tag['href']
        joined = urljoin(url, href)
        parsed = urlparse(joined)
        if domain and domain in parsed.netloc:
            links.add(joined)

    return paragraphs, list(links)
