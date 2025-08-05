
# Emergency Triage Bot

An AI-powered chatbot that helps users assess the urgency of medical symptoms and recommends appropriate actions like monitoring at home, visiting a doctor, going to the ER, or calling an ambulance.

Built with **FastAPI**, **React**, and **OpenAI GPT**.

---

## Features

- Collects user inputs: symptom description, severity, duration, age, and risk factors.
- Rule-based triage scoring system determines urgency:
  - Monitor at home
  - Visit doctor
  - Visit ER
  - Call ambulance NOW
- GPT summarizes symptoms and provides friendly advice.
- Critical alert with on-screen warning and sound.
- Ethical disclaimer to ensure safety.
- Interactive frontend using React and Axios.

---

## Tech Stack

| Frontend         | Backend        | AI Integration     |
|------------------|----------------|--------------------|
| React + Axios    | FastAPI        | OpenAI GPT-3.5/4   |
| HTML/CSS         | Python 3.10+   | Dotenv for API key |

---

## Project Structure

```
EmergencyTriageBot/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── scoring.py
│   ├── gpt_response.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── public/
│   │   └── alert.mp3
│   └── src/
│       └── components/
│           ├── TriageForm.js
│           └── AlertBanner.js
│       └── App.js
│       └── App.css
```

---

## Setup Instructions

### Backend (FastAPI)

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file with your OpenAI key:

```
OPENAI_API_KEY=sk-your-openai-key
```

Run the backend:

```bash
uvicorn main:app --reload
```

API Docs: http://127.0.0.1:8000/docs

---

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

Access the app: http://localhost:3000

---

## Alert Sound Setup

Place `alert.mp3` in the `frontend/public/` folder.

---

## Disclaimer

> This tool does **not provide medical advice**. Always consult a licensed physician in case of emergencies. This app is for demonstration and educational purposes only.

---

## Future Improvements

- Store interaction history with SQLite.
- Simulate email alerts for critical cases.
- Add reset button and better error handling.
- Multi-language support.
- Deploy backend (Render) and frontend (Vercel/Netlify).
