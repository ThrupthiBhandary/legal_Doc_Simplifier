from deep_translator import GoogleTranslator
import time

TRANSLATE_CHUNK_SIZE = 4000  # Max chars per translation chunk
TRANSLATE_RETRIES = 3
TRANSLATE_WAIT = 2  # seconds

def translate_text(text, target_lang="en", chunk_size=TRANSLATE_CHUNK_SIZE):
    """
    Translate long text in chunks to avoid deep-translator 5000 char limit.
    Retries on network errors.
    """
    translated_text = ""
    start = 0
    while start < len(text):
        chunk = text[start:start + chunk_size]
        for attempt in range(TRANSLATE_RETRIES):
            try:
                translated_chunk = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
                translated_text += translated_chunk + " "
                break
            except Exception:
                if attempt < TRANSLATE_RETRIES - 1:
                    time.sleep(TRANSLATE_WAIT)
                    continue
                else:
                    # fallback: keep original chunk if translation fails
                    translated_text += chunk + " "
        start += chunk_size
    return translated_text.strip()
