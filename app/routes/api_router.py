from fastapi import APIRouter

from routes import hateSpeech

api_router = APIRouter()
api_router.include_router(hateSpeech.router, prefix="/hatespeech", tags=["hateSpeech"])

