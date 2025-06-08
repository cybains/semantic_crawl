import os
import json
from urllib.parse import urlparse

def url_to_filename(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.replace('/', '_').strip('_')
    if not path:
        path = 'root'
    return f"{parsed.netloc}_{path}.json"

def save_result(url: str, paragraphs: list[str], links: list[str], output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    filename = url_to_filename(url)
    filepath = os.path.join(output_dir, filename)

    data = {
        "url": url,
        "paragraphs": paragraphs,
        "links": links
    }

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved data to {filepath}")
