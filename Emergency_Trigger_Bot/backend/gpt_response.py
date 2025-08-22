
import os
from dotenv import load_dotenv
import google.generativeai as genai
from models import TriageInput

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
        load_dotenv()
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        if not GEMINI_API_KEY:
            print("❌ Gemini API key not found. Check your .env file.")
            return "⚠️ Unable to generate response. Please try again later."
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, 'text') else str(response)
    except Exception as e:
        import traceback
        print("🔥 Gemini API Error:", e)
        traceback.print_exc()
        return "⚠️ Unable to generate response. Please try again later."
