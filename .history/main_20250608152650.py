

from crawler import crawler

if __name__ == "__main__":
    base_url = "https://aima.gov.pt/"
    paragraphs, links = crawler.get_links_and_text(base_url, domain="aimia.gov.pt")
    
    print(f"\n📝 Extracted {len(paragraphs)} paragraphs from {base_url}")
    print(f"🔗 Found {len(links)} internal links")
