from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import logging
from dotenv import load_dotenv
from datetime import datetime
from typing import Dict, Any
import os
import json
import logging
from datetime import datetime


# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("autopilot_hr.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="AutoPilot HR AI Services",
    description="AI-powered hiring automation backend for Windows",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize new-style OpenAI client
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    logger.info("OpenAI client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {e}")
    raise

# Pydantic models
class ResumeAnalysisRequest(BaseModel):
    text: str

class SkillMatchRequest(BaseModel):
    candidate_profile: Dict[str, Any]
    job_profile: Dict[str, Any]

class CommunicationRequest(BaseModel):
    candidate_profile: Dict[str, Any]
    analysis_result: Dict[str, Any]
    message_type: str = "acknowledgment"

# Health check
@app.get("/health")
async def health_check():
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o"),
            messages=[
                {"role": "system", "content": "Health check"},
                {"role": "user", "content": "ping"}
            ],
            max_tokens=5
        )
        return {
            "status": "healthy",
            "openai_connection": "active",
            "timestamp": datetime.now().isoformat(),
            "model": os.getenv("OPENAI_MODEL", "gpt-4o")
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {
            "status": "degraded",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

# Example resume parsing
@app.post("/parse-resume")
async def parse_resume(request: ResumeAnalysisRequest):
    try:
        prompt = f"""
        Analyze this resume and extract structured information. Return valid JSON only.

        Resume Text:
        {request.text}

        Format:
        {{
          "name": "...",
          "email": "...",
          "skills": ["..."],
          "experience": [{{"company": "...", "position": "...", "years": 1.5}}],
          "education": ["..."]
        }}
        """
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o"),
            messages=[
                {"role": "system", "content": "You are an HR AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )

        # ✅ Extract only the content string
        result_text = response.choices[0].message.content.strip()

        # ✅ Convert it into real Python dict
        parsed_json = json.loads(result_text)

        # ✅ Return it properly from FastAPI
        return {"status": "success", "data": parsed_json}

    except Exception as e:
        logger.error(f"Resume parsing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)


