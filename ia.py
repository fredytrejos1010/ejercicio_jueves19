from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def chat_with_gemini(prompt):
    prompt = f"Responde con una rima a la última palabra del siguiente texto: \"{prompt}\""
    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=prompt,
    )
    
    return interaction.output_text
