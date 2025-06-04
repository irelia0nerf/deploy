from pydantic import BaseModel
from typing import List, Optional

class ScoreRequest(BaseModel):
    wallet_address: str
    tx_count: int
    balance: float
    risk_inputs: Optional[List[str]] = []

class ScoreResponse(BaseModel):
    wallet_address: str
    score: int
    spread: float
    status: str
    flags: List[str]
    reasons: Optional[List[str]] = []
    timestamp: str

class FlagRequest(BaseModel):
    flag: str
    action: str

class FlagResponse(BaseModel):
    flags: List[str]
    updated: bool
