from flask import Flask, request, jsonify, render_template # <--- 1. Add render_template
from flask_cors import CORS
from rag_faq.rag_faq import get_faq_answer

app = Flask(__name__)
CORS(app)

# 2. Add this new route for the Homepage
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/faq-answer", methods=["POST"])
def faq_answer():
    data = request.get_json()
    # ... (Keep the rest of your existing code exactly the same) ...
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    user_question = data.get("question", "")
    result = get_faq_answer(user_question)
    MIN_CONFIDENCE = 0.60
    current_confidence = result.get("confidence", 0) if result else 0

    if result is None or current_confidence < MIN_CONFIDENCE:
        return jsonify({
            "answer": "I'm not completely sure about this. Could you please rephrase?",
            "confidence": current_confidence,
            "matched_question": "N/A"
        })

    return jsonify({
        "answer": result.get("answer", "No answer found"),
        "confidence": round(float(current_confidence), 3),
        "matched_question": result.get("question", "Hidden") 
    })

if __name__ == "__main__":
    app.run(debug=True)