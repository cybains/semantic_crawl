import json
from transformers import pipeline

# Initialize the translation pipeline for Portuguese to English
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-pt-en")

# Load the JSON file
with open("data/02f2ef8495b20ae8de905a6e2583334d.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract paragraphs from JSON (assuming 'paragraphs' is a list of strings)
portuguese_paragraphs = data.get("paragraphs", [])

# Filter out empty or null paragraphs if any
portuguese_paragraphs = [p for p in portuguese_paragraphs if p and p.strip()]

# Function to chunk large text if needed (split by approx max tokens or characters)
def chunk_text(text, max_length=500):
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_length
        # Try to cut at the last space to avoid breaking words
        if end < len(text):
            end = text.rfind(' ', start, end)
            if end == -1:
                end = start + max_length
        chunks.append(text[start:end].strip())
        start = end
    return chunks

# Translate each paragraph separately (better for keeping structure)
translated_paragraphs = []
for i, para in enumerate(portuguese_paragraphs):
    print(f"Translating paragraph {i+1}/{len(portuguese_paragraphs)}...")
    # Chunk paragraph if too long
    chunks = chunk_text(para, max_length=500)
    translated_chunks = [translator(chunk, max_length=512)[0]['translation_text'] for chunk in chunks]
    translated_paragraphs.append(" ".join(translated_chunks))

# Optional: Join all translated paragraphs or keep them separate
translated_text = "\n\n".join(translated_paragraphs)

print("\n--- Translated Text ---\n")
print(translated_text)
