from flask import Flask, request, jsonify
from flask_cors import CORS
from langdetect import detect
import time

from utils.extract import extract_text_from_pdf
from utils.translate import translate_text
from utils.summarize import summarize_text
from utils.nlp import ner_process, classify_text, predict_outcome

app = Flask(__name__)
CORS(app)

@app.route("/simplify", methods=["POST"])
def simplify():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Extract text
    text = extract_text_from_pdf(file)
    if not text:
        return jsonify({"error": "No text found in PDF"}), 400

    # Detect language
    lang = detect(text)
    original_lang = lang

    # Translate to English if needed
    if lang != "en":
        text = translate_text(text, target_lang="en")

    # NLP pipeline
    entities = ner_process(text)
    category = classify_text(text)
    prediction = predict_outcome(text)

    # Summarization
    simplified_text = summarize_text(text)

    # Translate back to original language if needed
    if original_lang != "en":
        simplified_text = translate_text(simplified_text, target_lang=original_lang)

    return jsonify({
        "original_lang": original_lang,
        "entities": entities,
        "category": category,
        "prediction": prediction,
        "simplified_text": simplified_text
    })

if __name__ == "__main__":
    app.run(debug=True)
