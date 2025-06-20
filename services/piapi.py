import requests

# Chave de API da PIAPI
PIAPI_KEY = "8e3d8fed2b1f01ff8d1eb8e6bfd09bdbc41ebc3d230e7306564f63a692668d86"

def generate_image(prompt):
    headers = {"Authorization": f"Bearer {PIAPI_KEY}"}
    payload = {"prompt": prompt}

    try:
        response = requests.post("https://api.piapi.ai/generate", json=payload, headers=headers)
        print("DEBUG status:", response.status_code)
        print("DEBUG body:", response.text)

        if response.status_code == 200:
            result = response.json()
            return result.get("image_url") or result.get("url") or result.get("image")
        else:
            print("Erro na resposta da PIAPI:", response.text)
            return None
    except Exception as e:
        print("Erro na conexão com a PIAPI:", e)
        return None




