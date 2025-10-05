from transformers import pipeline

# Load summarization model once
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
MAX_TOKENS = 1000

def chunk_text(text, max_tokens=MAX_TOKENS):
    words = text.split()
    for i in range(0, len(words), max_tokens):
        yield " ".join(words[i:i + max_tokens])

def summarize_text(text):
    simplified_text = ""
    for chunk in chunk_text(text):
        summary_chunk = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        simplified_text += summary_chunk + " "
    return simplified_text.strip()
