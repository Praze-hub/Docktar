import os
import google.generativeai as genai
import environ


env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

_api_key = env("GOOGLE_API_KEY")
if not _api_key:
    raise RuntimeError("Api key not set")

genai.configure(api_key=_api_key)

MODEL_ID = 'gemini-pro'
# _model = genai.get_model(MODEL_ID)

def ask_gemini(prompt: str) -> str:
    try:
        resp = MODEL_ID.generate_content(prompt)
        return (resp.text or "").strip()
    except Exception as e:
        return "Sorry I could not generate a response at the moment"
    
    