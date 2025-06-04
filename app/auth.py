from fastapi import Header, HTTPException
import os

def get_api_key(x_api_key: str = Header(...)):
    api_key = os.getenv("API_KEY", "testkey")
    if x_api_key != api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key
