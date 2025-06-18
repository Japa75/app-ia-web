from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, Daniel! Seu app está funcionando com Flask no Render! 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
