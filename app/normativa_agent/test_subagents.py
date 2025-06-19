import asyncio
import logging
from agent import call_agent_async

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_subagents():
    consultas_prueba = [
        {
            "tipo": "Estructural",
            "query": "¿Cuáles son los requisitos de resistencia para hormigón estructural según NCh430?"
        },
        {
            "tipo": "Geotécnico", 
            "query": "¿Qué especificaciones de suelo se requieren para fundaciones según NCh1537?"
        },
        {
            "tipo": "Instalaciones",
            "query": "¿Cuáles son los requisitos para instalaciones sanitarias según la normativa chilena?"
        },
        {
            "tipo": "General",
            "query": "¿Qué normativas aplican para el diseño de un edificio de 10 pisos?"
        }
    ]
    
    for consulta in consultas_prueba:
        try:
            logger.info(f"\n{'='*50}")
            logger.info(f"Probando consulta {consulta['tipo']}: {consulta['query']}")
            logger.info(f"{'='*50}")
            
            respuesta = await call_agent_async(consulta['query'])
            
            logger.info(f"Respuesta del agente:")
            print(f"\n{respuesta}\n")
            
        except Exception as e:
            logger.error(f"Error en consulta {consulta['tipo']}: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_subagents()) 