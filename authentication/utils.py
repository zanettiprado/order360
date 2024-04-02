import os
import requests

if os.path.isfile('env.py'):
    import env as env

def get_access_token(client_id, client_secret):

    """
    Conecta com a API, faz a autenticação e pega o access token
    que permite o acesso às informações dos pedidos
    """
    url = "https://merchant-api.ifood.com.br/authentication/v1.0/oauth/token"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grantType": "client_credentials",
        "clientId": client_id,
        "clientSecret": client_secret
    }

    response = requests.post(url, data=data, headers=headers)
    
    if response.status_code == 200:
        accessToken = response.json().get("accessToken")
        return accessToken
    else:
        print("Failed to get access token:")
        print(f"Status code: {response.status_code}\n")
        print(response.text)
        return None
