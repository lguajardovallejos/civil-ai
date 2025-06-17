import asyncio
from normativa_agent.agent import NormativaAgent
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Inicializar el agente
    agent = NormativaAgent()
    
    # Ejemplo de consulta
    query = "¿Cuáles son los requisitos para obtener una licencia de conducir en Chile?"
    
    # Procesar la consulta
    resultado = await agent.procesar_consulta(query)
    
    # Mostrar resultados
    print("\nRespuesta:")
    print(resultado["respuesta"])
    
    print("\nDocumentos relevantes:")
    for i, doc in enumerate(resultado["documentos"], 1):
        print(f"\nDocumento {i}:")
        print(f"Relevancia: {doc['relevancia']:.2f}")
        print(f"Contenido: {doc['contenido'][:200]}...")
        print(f"Metadata: {doc['metadata']}")

if __name__ == "__main__":
    asyncio.run(main()) 