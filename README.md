
# Legal Document Simplifier

A web application that extracts text from PDF documents, translates it if needed, and generates a simplified summary using NLP models. Built with **Flask** for the backend and **React** for the frontend.

---

## Features

- Extract text from PDF documents.
- Detect the language of the document.
- Translate text to English (if needed) for processing.
- Summarize the text using **Hugging Face transformers** (`sshleifer/distilbart-cnn-12-6`).
- Translate simplified text back to the original language.
- Placeholders for NER, Classification, and Prediction (for future implementation).

---

## File Structure

```

legal_doc/
├── backend/
│   ├── app.py                 # Main Flask app
│   ├── models/                # Future fine-tuned models for NER, Classification, Prediction
│   ├── utils/
│   │   ├── extract.py         # PDF text extraction
│   │   ├── translate.py       # Translation utilities
│   │   ├── nlp.py             # NLP pipeline functions
│   │   └── summarize.py       # Text summarization functions
├── frontend/
│   └── src/                   # React frontend code
├── requirements.txt           # Python dependencies

````

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/ThrupthiBhandary/legal_Doc_Simplifier.git
cd legal_Doc_Simplifier/backend
````

### 2. Create a virtual environment and activate it

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python app.py
```

The backend will run on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

You can then use the React frontend to upload PDFs and get simplified text.

---

## Usage

1. Open the frontend in a browser.
2. Upload a PDF document.
3. The backend will:

   * Extract text from the PDF
   * Translate text to English (if not already English)
   * Summarize the text in chunks
   * Translate back to the original language (if needed)
4. The simplified text is displayed in the frontend.

---

## Notes

* Make sure you have a **stable internet connection** for translations.
* The current summarization model is `sshleifer/distilbart-cnn-12-6` from Hugging Face.
* NER, Classification, and Prediction features are placeholders and will be implemented in the future.

---

## Dependencies

* Flask
* Flask-CORS
* Transformers
* Torch
* PyMuPDF
* deep-translator
* langdetect
* PyPDF2

```


```
