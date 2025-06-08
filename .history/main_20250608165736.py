from get_links_and_text import get_links_and_text
from save_to_json import save_result
from urllib.parse import urljoin, urlparse
import time

visited = set()
to_visit = ["https://aima.gov.pt/"]
domain = "aima.gov.pt"
MAX_PAGES = 50
count = 0

while to_visit and count < MAX_PAGES:
    current_url = to_visit.pop(0)
    if current_url in visited:
        continue

    try:
        paragraphs, links, title, breadcrumbs = get_links_and_text(current_url, domain=domain)
    except Exception as e:
        print(f"❌ Error crawling {current_url}: {e}")
        continue

    print(f"\n✅ Crawled: {current_url}")
    print(f"📝 Extracted {len(paragraphs)} paragraphs")
    print(f"🔗 Found {len(links)} internal links")
    print(f"🏷 Title: {title}")
    print(f"📍 Breadcrumbs: {breadcrumbs}")

    save_result(current_url, paragraphs, links, title=title, breadcrumbs=breadcrumbs)
    visited.add(current_url)
    count += 1

    for link in links:
        full_url = urljoin(current_url, link)
        parsed = urlparse(full_url)
        if domain in parsed.netloc and full_url not in visited and full_url not in to_visit:
            to_visit.append(full_url)

    time.sleep(1)  # Be polite and avoid hammering the server
