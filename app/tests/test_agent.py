import asyncio
import sys
import os
import pytest

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.normativa_agent.agent import NormativaAgent
from app.tests.preguntas_prueba import preguntas_prueba

@pytest.mark.asyncio
async def test_agent():
    agent = NormativaAgent()
    resultados = []
    
    for i, pregunta in enumerate(preguntas_prueba, 1):
        print(f"\nProbando pregunta {i}/{len(preguntas_prueba)}")
        print(f"Tipo: {pregunta['tipo']}")
        print(f"Pregunta: {pregunta['pregunta']}")
        
        respuesta = await agent.procesar_consulta(pregunta['pregunta'])
        
        resultado = {
            "numero": i,
            "tipo": pregunta['tipo'],
            "pregunta": pregunta['pregunta'],
            "respuesta_esperada": pregunta['respuesta_esperada'],
            "respuesta_obtenida": respuesta['respuesta'],
            "documentos_usados": respuesta['documentos']
        }
        resultados.append(resultado)
        
        print(f"Respuesta obtenida: {respuesta['respuesta']}")
        print("-" * 80)
    
    # Guardar resultados
    with open("resultados_test.txt", "w", encoding="utf-8") as f:
        for r in resultados:
            f.write(f"Pregunta {r['numero']} ({r['tipo']}):\n")
            f.write(f"Pregunta: {r['pregunta']}\n")
            f.write(f"Respuesta esperada: {r['respuesta_esperada']}\n")
            f.write(f"Respuesta obtenida: {r['respuesta_obtenida']}\n")
            f.write(f"Documentos usados: {len(r['documentos_usados'])}\n")
            f.write("-" * 80 + "\n")

if __name__ == "__main__":
    asyncio.run(test_agent()) 