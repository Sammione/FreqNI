BASE_URL = "baseURL"
FAQ_ENDPOINT = "EndPoint"

def get_auth_headers(token: str):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }



