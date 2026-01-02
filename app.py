from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message manquant"}), 400

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_message
        )

        reply = response.output_text
        return jsonify({"reply": reply})

    except Exception as e:
        print(e)
        return jsonify({"error": "Erreur serveur"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
