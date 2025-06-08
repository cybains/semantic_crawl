import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links_and_text(url, domain=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)

    if "text/html" not in response.headers.get("Content-Type", ""):
        return [], [], None, None

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title
    title = soup.title.string.strip() if soup.title else None

    # Extract breadcrumbs (example: elements with class 'breadcrumb' and their li children)
    breadcrumbs = soup.select(".breadcrumb li")
    breadcrumb_text = " > ".join(item.get_text(strip=True) for item in breadcrumbs) if breadcrumbs else None

    # Extract paragraphs, plus other content tags like h1, h2, h3, li (optional)
    content_tags = soup.select("h1, h2, h3, p, li")
    paragraphs = [tag.get_text(strip=True) for tag in content_tags if tag.get_text(strip=True)]

    # Collect internal links
    links = set()
    for tag in soup.find_all("a", href=True):
        href = tag['href']
        joined = urljoin(url, href)
        parsed = urlparse(joined)
        if domain and domain in parsed.netloc:
            links.add(joined)

    return paragraphs, list(links), title, breadcrumb_text
