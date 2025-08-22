from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import TriageInput, TriageResponse
from scoring import calculate_triage_score
from gpt_response import generate_gpt_response

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/triage", response_model=TriageResponse)
async def triage_handler(input_data: TriageInput):
    score = calculate_triage_score(input_data)

    # Determine urgency level and alert trigger
    if score <= 4:
        urgency = "Monitor at home"
        alert = False
    elif score <= 7:
        urgency = "Visit doctor"
        alert = False
    elif score <= 9:
        urgency = "Visit ER"
        alert = True
    else:
        urgency = "Call ambulance NOW"
        alert = True

    gpt_message = generate_gpt_response(input_data, urgency)

    return TriageResponse(
        score=score,
        urgency_level=urgency,
        gpt_response=gpt_message,
        alert_trigger=alert
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)