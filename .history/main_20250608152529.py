

from crawler import crawler

if __name__ == "__main__":
    base_url = "https://www.eesti.ee/eraisik/en/artikkel/citizenship-and-documents/right-of-residence-and-residence-permit-for-foreign-nationals"
    paragraphs, links = crawler.get_links_and_text(base_url, domain="eesti.ee")
    
    print(f"\n📝 Extracted {len(paragraphs)} paragraphs from {base_url}")
    print(f"🔗 Found {len(links)} internal links")
