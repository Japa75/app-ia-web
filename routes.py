from flask import request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from services.piapi import generate_image

def get_db():
    return sqlite3.connect("users.db")

def register_routes(app):
    @app.route("/")
    def index():
        if "user" in session:
            return render_template("dashboard.html", user=session["user"])
        return redirect(url_for("login"))

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            email = request.form["email"]
            password = generate_password_hash(request.form["password"])
            with get_db() as db:
                db.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            return redirect(url_for("login"))
        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            with get_db() as db:
                user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
            if user and check_password_hash(user[2], password):
                session["user"] = email
                return redirect(url_for("index"))
            flash("Login inválido")
        return render_template("login.html")

    @app.route("/logout")
    def logout():
        session.pop("user", None)
        return redirect(url_for("login"))

    @app.route("/generate", methods=["POST"])
    def generate():
        if "user" not in session:
            return redirect(url_for("login"))
        prompt = request.form["prompt"]
        image_url = generate_image(prompt)
        return render_template("dashboard.html", user=session["user"], image_url=image_url)
