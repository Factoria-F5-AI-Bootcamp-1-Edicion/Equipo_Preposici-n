from fastapi import APIRouter

from routes import hate_speech

api_router = APIRouter()
api_router.include_router(hate_speech.router, prefix="/hatespeech", tags=["hateSpeech"])

