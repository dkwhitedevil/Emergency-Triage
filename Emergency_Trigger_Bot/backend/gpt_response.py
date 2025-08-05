import os
from openai import OpenAI
from dotenv import load_dotenv
from models import TriageInput

# Load .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API key not found. Check your .env file.")
else:
    print("✅ Loaded API Key:", api_key[:8] + "********")

# Create OpenAI client (new format)
client = OpenAI(api_key=api_key)

def generate_gpt_response(data: TriageInput, urgency_level: str) -> str:
    prompt = (
        f"You are an AI assistant helping a user with health symptoms.\n"
        f"Symptom: {data.symptom_description}\n"
        f"Severity: {data.severity}\n"
        f"Duration: {data.duration}\n"
        f"Age: {data.age}\n"
        f"Risk Factors: {', '.join(data.risk_factors) if data.risk_factors else 'None'}\n"
        f"Triage Score indicates: {urgency_level}\n\n"
        f"Provide a friendly summary and advice. Add this disclaimer: "
        f"'This tool does not provide medical advice. Always consult a licensed physician in case of emergencies.'"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"🔥 GPT API Error: {e}")
        return "⚠️ Unable to generate response. Please try again later."
