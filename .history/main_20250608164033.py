from crawler import get_links_and_text
from save_to_json import save_result

url = "https://aima.gov.pt/"
paragraphs, links = get_links_and_text(url, domain="aima.gov.pt")

print(f"📝 Extracted {len(paragraphs)} paragraphs from {url}")
print(f"🔗 Found {len(links)} internal links")

save_result(url, paragraphs, links)
