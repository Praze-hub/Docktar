import os
from google import genai
import environ


env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

_api_key = env("GOOGLE_API_KEY")
if not _api_key:
    raise RuntimeError("Api key not set")

client = genai.Client(api_key=_api_key)

def ask_gemini(prompt: str) -> str:
    try:
        # _model = genai.GenerativeModel('gemini-pro')
        resp = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)
        return (resp.text or "").strip()
    except Exception as e:
        return f"Sorry I could not generate a response at the moment. Error: {str(e)}"
        # return "Sorry I could not generate a response at the moment"
    
    