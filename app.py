from flask import Flask
from flask_login import LoginManager
from routes import register_routes
from db import init_db, db, User

app = Flask(__name__)
app.secret_key = 'supersecretkey'

init_db(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

register_routes(app, login_manager)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


