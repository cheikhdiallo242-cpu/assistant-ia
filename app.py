from flask import Flask, request, jsonify, render_template
from brain import think

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    user_id = data.get("user", "default")

    if not user_message:
        return jsonify({"response": "Écris un message."})

    response = think(user_id, user_message)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
