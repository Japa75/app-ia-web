from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from db import db, User
from services.piapi import generate_image

def register_routes(app, login_manager):

    @app.route("/")
    def index():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        return redirect(url_for("login"))

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            if User.query.filter_by(username=username).first():
                flash("Usuário já existe!")
                return redirect(url_for("register"))

            new_user = User(username=username)
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()

            flash("Conta criada com sucesso! Faça login.")
            return redirect(url_for("login"))

        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for("dashboard"))
            else:
                flash("Usuário ou senha inválidos!")
                return redirect(url_for("login"))

        return render_template("login.html")

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return render_template("dashboard.html", user=current_user)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("login"))

    @app.route("/generate", methods=["POST"])
    @login_required
    def generate():
        prompt = request.form.get("prompt")
        if not prompt:
            flash("Por favor, insira um prompt para gerar a imagem.")
            return redirect(url_for("dashboard"))

        image_url = generate_image(prompt)
        if not image_url:
            flash("Erro ao gerar a imagem. Tente novamente.")
            return redirect(url_for("dashboard"))

        return render_template("dashboard.html", user=current_user, image_url=image_url)



      
