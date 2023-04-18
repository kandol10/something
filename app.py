from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.form["user_message"]
    # TODO: Add your chatbot logic here
    return {"bot_message": "Hello, World!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
