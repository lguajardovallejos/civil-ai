from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import os
import logging
from dotenv import load_dotenv
from pathlib import Path

# Configuración básica
logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Configurar API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY no está configurada")

# Configuración del agente base
root_agent = Agent(
    name="normativa_agent",
    model="gemini-2.0-flash",
    description="Agente especializado en normativas de ingeniería civil en Chile",
    instruction="""Eres un asistente especializado en normativas de ingeniería civil en Chile. 
    Debes responder consultas sobre normativas, códigos y regulaciones del sector. 
    SIEMPRE incluye la fuente de tu información en tus respuestas usando el formato [Nombre de la norma]of[Año]. Ejemplo:NCh164of2018.
    SIEMPRE incluye la sección de la norma que se aplica a la consulta. A menos que sea muy repititivo, no lo incluyas.
    Debes responder al inicio de la respuesta la fuente de la información.
    Si no tienes la información específica, indícalo claramente."""
)


# Configuración del servicio de sesión
session_service = InMemorySessionService()
APP_NAME = "normativa_agent"
USER_ID = "user_001"
SESSION_ID = "session_001"

# Crear runner
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)

async def call_agent_async(query: str):
    try:
        content = types.Content(role='user', parts=[types.Part(text=query)])
        final_response_text = "El agente no produjo una respuesta final."
        
        async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
            if event.is_final_response():
                if event.content and event.content.parts:
                    final_response_text = event.content.parts[0].text
                break
        
        return final_response_text
    except Exception as e:
        return f"Error: {str(e)}"

async def run_conversation():
    try:
        response = await call_agent_async(
            query="¿Cuáles son los requisitos mínimos para un estacionamiento según la normativa chilena?"
        )
        print(f"Respuesta: {response}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_conversation()) 