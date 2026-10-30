from fastapi import FastAPI
from ia import chat_with_gemini
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/chat/{mensaje}")
def llamarIA_IA(mensaje):
    chat_response = chat_with_gemini(mensaje)
    lReturn = {"mensaje": mensaje, "respuesta": chat_response}
    return lReturn