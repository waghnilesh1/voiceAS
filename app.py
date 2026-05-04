from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 🔑 Replace with your API key
openai.api_key = "key_418qaIx61CESncoF"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Handle date/time in backend also (extra safety)
    if "date" in user_message.lower():
        return jsonify({"reply": datetime.now().strftime("%A, %d %B %Y")})

    if "time" in user_message.lower():
        return jsonify({"reply": datetime.now().strftime("%H:%M:%S")})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a smart voice assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response["choices"][0]["message"]["content"]

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Error: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True)