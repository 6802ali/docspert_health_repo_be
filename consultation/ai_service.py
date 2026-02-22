from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)

MOCK_SUMMARY = """
- Chief Complaint: Patient presented with reported symptoms requiring medical evaluation.
- Key Symptoms: As documented in the consultation record.
- Diagnosis Summary: Preliminary assessment has been recorded by the attending physician.
- Recommended Follow-up: Please consult with the attending physician for detailed follow-up instructions and treatment plan.

Note: This is an automated placeholder summary. The AI-generated summary is temporarily unavailable. Please try again later or consult the full consultation record.
"""

def generate_consultation_summary(symptoms: str, diagnosis: str) -> str:
    prompt = f"""
You are a medical assistant. Given the following patient consultation details, 
generate a concise, structured clinical summary.

Symptoms: {symptoms}
Diagnosis: {diagnosis}

Return the summary in this format:
- Chief Complaint: ...
- Key Symptoms: ...
- Diagnosis Summary: ...
- Recommended Follow-up: ...
"""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        error_message = str(e).lower()
        if "429" in error_message or "rate limit" in error_message:
            return MOCK_SUMMARY
        raise  # re-raise any other unexpected errors so the view handles them