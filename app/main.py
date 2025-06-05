from fastapi import FastAPI, Depends
from app.schemas import ScoreRequest, ScoreResponse, FlagRequest, FlagResponse
from app.score_engine import calculate_score
from app.dfc import get_flags, update_flags
from app.auth import get_api_key
from app.crud import save_score_event
import os

app = FastAPI(title="FoundLab ScoreLab MVP")

@app.get("/health/")
async def health():
    return {"status": "ok"}

@app.post("/score/", response_model=ScoreResponse)
async def score_endpoint(req: ScoreRequest, api_key: str = Depends(get_api_key)):
    score_data = calculate_score(req)
    webhook_status = await save_score_event(score_data)
    score_data["webhook_status"] = webhook_status
    return score_data

@app.get("/flags/", response_model=FlagResponse)
async def get_flags_endpoint(api_key: str = Depends(get_api_key)):
    return get_flags()

@app.post("/flags/", response_model=FlagResponse)
async def update_flags_endpoint(flag_req: FlagRequest, api_key: str = Depends(get_api_key)):
    return update_flags(flag_req)
