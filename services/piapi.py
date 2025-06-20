import os
import requests

# Carrega a chave da PIAPI de uma variável de ambiente
PIAPI_KEY = os.getenv("PIAPI_KEY")

# Endpoint da API PIAPI — atualize se for diferente!
PIAPI_URL = "https://api.piapi.ai/generate"

def generate_image(prompt):
    if not PIAPI_KEY:
        print("❌ ERRO: PIAPI_KEY não configurada!")
        return None

    headers = {
        "Authorization": f"Bearer {PIAPI_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt
    }

    try:
        response = requests.post(PIAPI_URL, json=payload, headers=headers)
        response.raise_for_status()  # dispara erro automático se status != 200

        data = response.json()
        print("✅ Resposta da PIAPI:", data)

        # Tente adaptar de acordo com a estrutura real retornada
        return data.get("image_url") or data.get("url") or data.get("data", {}).get("image")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar PIAPI: {e}")
        return None





