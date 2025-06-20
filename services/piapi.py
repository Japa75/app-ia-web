import requests

# Sua chave está diretamente aqui (não depende de variável externa)
PIAPI_KEY = "8e3d8fed2b1f01ff8d1eb8e6bfd09bdbc41ebc3d230e7306564f63a692668d86"

def generate_image(prompt):
    headers = {"Authorization": f"Bearer {PIAPI_KEY}"}
    payload = {"prompt": prompt}
    response = requests.post("https://api.piapi.ai/generate", json=payload, headers=headers)

    # Verifica e imprime a resposta no terminal
    print("DEBUG status:", response.status_code)
    print("DEBUG body:", response.text)

    if response.status_code == 200:
        try:
            return response.json().get("image_url")
        except Exception as e:
            print("Erro ao converter resposta JSON:", e)
            return None
    return None



