from flask import Flask
from routes import register_routes
from db import init_db

app = Flask(__name__)
app.secret_key = 'supersecretkey'
init_db()
register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

