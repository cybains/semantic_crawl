
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links_and_text(url, domain):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

        base = "{0.scheme}://{0.netloc}".format(urlparse(url))
        hrefs = [a["href"] for a in soup.find_all("a", href=True)]

        all_links = [urljoin(base, h) for h in hrefs]
        internal_links = [link for link in all_links if domain in link]

        # Print for debugging
        print("\nAll links found on page:")
        for link in all_links:
            print("🔗", link)

        return paragraphs, internal_links

    except Exception as e:
        print(f"❌ Error: {e}")
        return [], []

