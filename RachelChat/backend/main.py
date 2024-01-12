# uvicorn main:app --reload
# venv\Scripts\activate

# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response


# Initiate App
app = FastAPI()


# CORS - Origins
origins = [
    "https://localhost:5173",
    "https://localhost:5174",
    "https://localhost:4173",
    "https://localhost:4174",
    "https://localhost:3000",
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # GET, POST, PUT, DELETE, OPTIONS, HEAD
    allow_headers=["*"],
)


# Check Health
@app.get("/health")
async def check_health():
    return {"message": "Healthy"}

# Get audio
@app.get("/post-audio-get/")
async def get_audio():

    # Get saved audio
    audio_input = open("voice.mp3", "rb")

    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message decoded
    if not message_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode audio")
    
    # Get ChatGPT Response
    chat_response = get_chat_response(message_decoded)

    print(chat_response)

    return "Done"


# # Post bot response
# # Note: Not playing in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#     print("hello")