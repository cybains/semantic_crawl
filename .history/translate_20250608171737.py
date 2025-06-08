from transformers import pipeline

# Initialize the translation pipeline for Portuguese to English
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-pt-en")

# Example: input text chunks (replace with your actual paragraphs)
portuguese_paragraphs = [
    "Os cursos PLA são gratuitos?Sim, na sua grande maioria, embora possa depender do tipo de entidade promotora e do facto do curso ser ou não cofinanciado por fundos comunitários.",
    "Os cursos PLA são certificados?Sim. Os cursos PLA certificam os níveis A1 + A2 (Utilizador Elementar) e B1 + B2 (Utilizador Independente), de acordo com o Quadro Europeu Comum de Referência para as Línguas (QECRL).",
    # Add more paragraphs as needed
]

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

# Combine all paragraphs into a single text (or translate each paragraph separately)
full_text = " ".join(portuguese_paragraphs)

# Chunk the full text if it's too long
chunks = chunk_text(full_text, max_length=500)

translated_chunks = []
for i, chunk in enumerate(chunks):
    print(f"Translating chunk {i+1}/{len(chunks)}...")
    translation = translator(chunk, max_length=512)[0]['translation_text']
    translated_chunks.append(translation)

# Combine translated chunks
translated_text = " ".join(translated_chunks)

print("\n--- Translated Text ---\n")
print(translated_text)
