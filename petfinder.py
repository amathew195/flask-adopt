import requests
from app import app, PETFINDER_API_KEY, PETFINDER_SECRET_KEY
PETFINDER_AUTH_TOKEN_URL = "https://api.petfinder.com/v2/oauth2/token"




def update_auth_token_string():
    """Aut against PetFinder and return JSON {token_type, access_token)"""

    data = {
        "grant_type": "client_credentials",
        "client_id": PETFINDER_API_KEY,
        "client_secret": PETFINDER_SECRET_KEY
    }

    resp = requests.post(PETFINDER_AUTH_TOKEN_URL, data=data)

    if resp.status_code == 401:
        raise AuthError()

    token = resp.json()
    return f"{token['token_type']} {token['access_token']}"

