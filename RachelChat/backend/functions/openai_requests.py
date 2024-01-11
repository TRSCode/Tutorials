import openai
from decouple import config

# Retrieve Environment Variables
openai.organization = config('OPENAI_ORGANIZATION')
openai.api_key = config('OPENAI_API_KEY')


# OpenAI - Whisper
# Convert Audio to Text
def convert_audio_to_text(audio_file):
    try: 
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return