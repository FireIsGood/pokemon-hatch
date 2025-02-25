import requests


def get_endpoint(port: int, endpoint: str):
    r = requests.get(f"http://localhost:{port}/{endpoint}")
    if r.status_code == 200:
        response = r.json()
    else:
        response = None
    return response


def post_endpoint(port: int, endpoint: str, data: dict):
    r = requests.post(f"http://localhost:{port}/{endpoint}", json=data)
    if r.status_code == 200:
        response = r.json()
    else:
        response = None
    return response
