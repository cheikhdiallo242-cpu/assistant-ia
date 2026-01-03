from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def assistant_reponse(message):
    msg = message.lower()

    if "salut" in msg or "bonjour" in msg:
        return "Salut 👋 Je suis ton assistant IA. Comment puis-je t’aider ?"

    if "aide" in msg:
        return "Je peux répondre à tes questions, expliquer ton projet ou t’orienter 🙂"

    if "qui es-tu" in msg or "qui es tu" in msg:
        return "Je suis une assistante IA gratuite créée par Cheikh 🚀"

    if "contact" in msg:
        return "Tu peux me dire ici ce que tu veux savoir 📩"

    if "merci" in msg:
        return "Avec plaisir 🙏"

    return "🤖 Je réfléchis… peux-tu reformuler ta question ?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = assistant_reponse(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
