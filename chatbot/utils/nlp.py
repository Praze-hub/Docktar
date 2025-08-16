from .gemini_client import ask_gemini

MEDICAL_SYSTEM_PROMPT = """You are an assistant for first-aid style guidance in Africa.
- You can suggest common causes and simple next steps including diagnostics.
- Always include red-flag warnings and when to seek urgent care.
- You can suggest some drugs that can help at that point as well.
- Use simple, culturally aware language.
- You are NOT a doctor; include a disclaimer."""

def analyze_symptom(symptom_text: str) -> str:
    prompt = f"""
    {MEDICAL_SYSTEM_PROMPT} 
    User symptoms: "{symptom_text}"
    Return:
    1) Likely possibilities (non-diagnostic)
    2) At-home care tips
    3) Red flags (when to go to a clinic/hospital)
    4) Short disclaimer
    """
    
    return ask_gemini(prompt)

def translate_text(text: str, target_lang: str) -> str:
     prompt = f"""Translate the following medical advice into {target_lang}.
     Keep it clear, simple, and culturally appropriate. Do not add extra info.

     Text: {text}
     """
     return ask_gemini(prompt)
 
