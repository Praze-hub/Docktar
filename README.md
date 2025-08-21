# 🩺 DOCKTAR

A Django REST Framework (DRF) based API that helps users analyze symptoms and get medical advice powered by **Google Gemini (Generative AI)**.  
The chatbot supports **multilingual advice** with translation into local languages such as Yoruba, Igbo, Hausa, etc.

---

## 🚀 Features
- Analyze medical symptoms and provide AI-generated advice.
- Supports **multilingual translations** of advice.
- RESTful API endpoints for easy integration.
- Interactive **Swagger / ReDoc API docs**.
- Dockerized for consistent deployment.
- Configurable via `.env` file (API keys, database, etc.).

---

## 🛠️ Tech Stack / Tools

- Backend Framework: Django, Django REST Framework (DRF)

- AI Model: Google Gemini (google-genai SDK)

- API Docs: drf-spectacular (Swagger UI, ReDoc)

- Containerization: Docker, Docker Compose

- Database: PostgreSQL (or SQLite for local dev)

- Environment Management: django-environ

- Language Support: English + Local languages (via translation API)

---

## 📂 Project Structure
```markdown
Docktar/
├── chatbot/
│   ├── utils/
│   │   ├── nlp.py              # Handles AI integration (Gemini + translation)
│   │   ├── gemini_client.py    # Gemini API client
│   ├── serializers.py          # Input validation
│   ├── views.py                # Symptom analysis endpoints
│   ├── urls.py                 # Route definitions
│
├── core/
│   ├── settings.py             # Django settings
│   ├── .env                    # Environment variables
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md


