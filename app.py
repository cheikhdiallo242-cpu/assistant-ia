from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI

app = Flask(__name__)

# 🔐 Client OpenAI (clé depuis Render > Environment)
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# =========================
# PAGE D’ACCUEIL
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# ROUTE CHAT
# =========================
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message manquant"}), 400

    user_message = data["message"]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Tu es un assistant IA utile et clair."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# LANCEMENT SERVEUR
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
