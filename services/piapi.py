def generate_image(prompt):
    headers = {"Authorization": f"Bearer {PIAPI_KEY}"}
    payload = {"prompt": prompt}
    response = requests.post("https://api.piapi.ai/generate", json=payload, headers=headers)
    
    print("DEBUG:", response.status_code, response.text)  # ← adicione esta linha

    if response.status_code == 200:
        return response.json().get("image_url")
    return None

