import os
import json
from hashlib import md5

def save_result(url, paragraphs, links, out_dir="data"):
    os.makedirs(out_dir, exist_ok=True)
    filename = md5(url.encode()).hexdigest() + ".json"
    path = os.path.join(out_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump({
            "url": url,
            "paragraphs": paragraphs,
            "links": links
        }, f, ensure_ascii=False, indent=2)
