import React, { useState } from "react";
import axios from "axios";
import AlertBanner from "./AlertBanner";

const TriageForm = () => {
  const [formData, setFormData] = useState({
    symptom_description: "",
    severity: "mild",
    duration: "<1 day",
    age: "",
    risk_factors: [],
  });

  const [response, setResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const riskOptions = ["chronic illness", "pregnancy", "immunocompromised"];

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (type === "checkbox") {
      const updatedRisks = checked
        ? [...formData.risk_factors, value]
        : formData.risk_factors.filter((rf) => rf !== value);
      setFormData({ ...formData, risk_factors: updatedRisks });
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:8000/triage", formData);
      setResponse(res.data);
    } catch {
      alert("API error. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>Emergency Triage Bot</h2>
      <form onSubmit={handleSubmit}>
        <label>Symptom Description:</label>
        <textarea
          name="symptom_description"
          value={formData.symptom_description}
          onChange={handleChange}
          required
        />

        <label>Severity:</label>
        <select name="severity" value={formData.severity} onChange={handleChange}>
          <option value="mild">Mild</option>
          <option value="medium">Medium</option>
          <option value="severe">Severe</option>
        </select>

        <label>Duration:</label>
        <select name="duration" value={formData.duration} onChange={handleChange}>
          <option value="<1 day">&lt;1 day</option>
          <option value="1–3 days">1–3 days</option>
          <option value=">3 days">&gt;3 days</option>
        </select>

        <label>Age:</label>
        <input
          type="number"
          name="age"
          value={formData.age}
          onChange={handleChange}
          required
        />

        <label>Risk Factors:</label>
        {riskOptions.map((risk) => (
          <div key={risk}>
            <input
              type="checkbox"
              name="risk_factors"
              value={risk}
              checked={formData.risk_factors.includes(risk)}
              onChange={handleChange}
            />
            {risk}
          </div>
        ))}

        <button type="submit" disabled={isLoading}>
          {isLoading ? "Analyzing..." : "Submit"}
        </button>
      </form>

      {response && (
        <div className="response-box">
          <h3>GPT Response:</h3>
          <p>{response.gpt_response}</p>
          <p><strong>Urgency:</strong> {response.urgency_level}</p>
        </div>
      )}

      {response?.alert_trigger && <AlertBanner />}

      <p className="disclaimer">
        Disclaimer: This tool does not provide medical advice. Always consult a licensed physician in case of emergencies.
      </p>
    </div>
  );
};

export default TriageForm;
