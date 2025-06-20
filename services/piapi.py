import requests

PIAPI_KEY = "8e3d8fed2b1f01ff8d1eb8e6bfd09bdbc41ebc3d230e7306564f63a692668d86"

def generate_image(prompt):
    headers = {"Authorization": f"Bearer {PIAPI_KEY}"}
    payload = {"prompt": prompt}
    response = requests.post("https://api.piapi.ai/generate", json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("image_url")
    return "Erro ao gerar imagem"
