from google.adk.agents import Agent
import chromadb
from chromadb.config import Settings
import os
from typing import List, Dict, Any
import json
from datetime import datetime

# Definir el agente raíz
root_agent = Agent(
    name="normativa_agent",
    model="gemini-2.0-flash",
    description="Agente especializado en consultar normativa chilena",
    instruction="""Eres un asistente especializado en normativa chilena. 
    Debes responder basándote ÚNICAMENTE en los documentos proporcionados en el contexto.
    Si la información no está en los documentos proporcionados, indica que no tienes esa información.
    No inventes información ni uses conocimiento externo."""
)

class NormativaAgent:
    def __init__(self):
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="chroma_db"
        ))
        self.collection = self.client.get_collection("normativa")

    async def consultar_normativa(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=max_results
            )
            
            documentos = []
            for i, (doc, metadata, distance) in enumerate(zip(results['documents'][0], results['metadatas'][0], results['distances'][0])):
                documentos.append({
                    "contenido": doc,
                    "metadata": metadata,
                    "relevancia": 1 - distance
                })
            
            return documentos
        except Exception as e:
            print(f"Error al consultar la normativa: {str(e)}")
            return []

    async def procesar_consulta(self, query: str) -> Dict[str, Any]:
        try:
            documentos = await self.consultar_normativa(query)
            
            if not documentos:
                return {
                    "respuesta": "No se encontraron documentos relevantes para tu consulta en la base de datos de normativa.",
                    "documentos": []
                }
            
            # Preparar el contexto para el agente
            contexto = "\n\n".join([
                f"Documento {i+1} (Relevancia: {doc['relevancia']:.2f}):\n{doc['contenido']}\n"
                f"Fuente: {doc['metadata'].get('fuente', 'No especificada')}"
                for i, doc in enumerate(documentos)
            ])
            
            # Procesar la consulta con el agente ADK
            respuesta = await root_agent.run(
                query=f"""Contexto de normativa chilena:
{contexto}

Consulta del usuario: {query}

Recuerda: Solo responde basándote en la información proporcionada en el contexto. Si la información no está disponible, indícalo claramente."""
            )
            
            return {
                "respuesta": respuesta,
                "documentos": documentos
            }
            
        except Exception as e:
            print(f"Error al procesar la consulta: {str(e)}")
            return {
                "respuesta": "Ocurrió un error al procesar tu consulta.",
                "documentos": []
            }

    def guardar_consulta(self, query: str, respuesta: Dict[str, Any]) -> None:
        try:
            with open("consultas_normativa.json", "a", encoding="utf-8") as f:
                json.dump({
                    "query": query,
                    "respuesta": respuesta,
                    "timestamp": str(datetime.now())
                }, f, ensure_ascii=False)
                f.write("\n")
        except Exception as e:
            print(f"Error al guardar la consulta: {str(e)}") 