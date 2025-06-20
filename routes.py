from flask import render_template, request, redirect, url_for, session
from services.piapi import generate_image

def register_routes(app):
    @app.route("/")
    def index():
        return redirect(url_for("login"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        # ...

    @app.route("/generate", methods=["POST"])
    def generate():
        # ...


      
