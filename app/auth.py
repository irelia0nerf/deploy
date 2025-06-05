from fastapi import Header, HTTPException
import os


def _get_env_api_key() -> str:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="API key not configured")
    return api_key

def get_api_key(x_api_key: str = Header(...)):
    api_key = _get_env_api_key()
    if x_api_key != api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key
