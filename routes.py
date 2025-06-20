@app.route("/generate", methods=["POST"])
def generate():
    if "user" not in session:
        return redirect(url_for("login"))

    prompt = request.form["prompt"]

    try:
        image_url = generate_image(prompt)
        if not image_url:
            return "Erro: imagem não foi gerada. Verifique o prompt ou a resposta da PIAPI."
    except Exception as e:
        return f"Erro ao gerar imagem: {e}"

    return render_template("dashboard.html", user=session["user"], image_url=image_url)

      
