from flask import render_template, request, redirect, url_for, session
from services.piapi import generate_image

def register_routes(app):

    @app.route("/")
    def index():
        return redirect(url_for("login"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            # Aqui você pode validar usuário no banco (placeholder)
            if username == "admin" and password == "123":  # Exemplo simplificado
                session["user"] = username
                return redirect(url_for("dashboard"))
            else:
                return render_template("login.html", error="Usuário ou senha inválidos")
        return render_template("login.html")

    @app.route("/dashboard")
    def dashboard():
        if "user" not in session:
            return redirect(url_for("login"))
        return render_template("dashboard.html", user=session["user"])

    @app.route("/logout")
    def logout():
        session.pop("user", None)
        return redirect(url_for("login"))

    @app.route("/generate", methods=["POST"])
    def generate():
        if "user" not in session:
            return redirect(url_for("login"))

        prompt = request.form.get("prompt")
        if not prompt:
            return "Por favor, insira um prompt para gerar a imagem."

        image_url = generate_image(prompt)
        if not image_url:
            return "Erro ao gerar a imagem. Tente novamente."

        return render_template("dashboard.html", user=session["user"], image_url=image_url)


      
