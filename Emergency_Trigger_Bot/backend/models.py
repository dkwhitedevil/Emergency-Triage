from pydantic import BaseModel
from typing import List, Optional

class TriageInput(BaseModel):
    symptom_description: str
    severity: str  # mild, medium, severe
    duration: str  # <1 day, 1–3 days, >3 days
    age: int
    risk_factors: Optional[List[str]] = []

class TriageResponse(BaseModel):
    score: int
    urgency_level: str
    gpt_response: str
    alert_trigger: bool
