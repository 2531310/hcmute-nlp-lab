
import os
import spacy
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route("/")
def index():
    return send_file("src/index.html")

@app.route("/process", methods=["POST"])
def process():
    """
    Processes the input text and returns tokens, POS tags, and named entities.
    """
    data = request.get_json()
    text = data.get("text", "")

    # Process the text with spaCy
    doc = nlp(text)

    # Extract tokens and POS tags
    tokens = [{"text": token.text, "pos": token.pos_} for token in doc]

    # Extract named entities
    entities = [{"text": ent.text, "label": ent.label_, "start_char": ent.start_char, "end_char": ent.end_char} for ent in doc.ents]

    return jsonify({
        "tokens": tokens,
        "entities": entities
    })

def main():
    app.run(port=int(os.environ.get("PORT", 80)))

if __name__ == "__main__":
    main()
