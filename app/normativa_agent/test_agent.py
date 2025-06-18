import asyncio
import logging
from agent import NormativaAgent

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_agent():
    try:
        logger.info("Iniciando prueba del agente...")
        
        # Crear instancia del agente
        agent = NormativaAgent()
        logger.info("Agente creado exitosamente")
        
        # Consulta de prueba sobre granulometría
        query = "¿Cuáles son los requisitos de granulometría para agregados según la normativa chilena?"
        logger.info(f"Consultando: {query}")
        
        # Procesar consulta
        logger.info("Procesando consulta...")
        resultado = await agent.procesar_consulta(query)
        
        # Mostrar resultado
        logger.info("Respuesta del agente:")
        print("\nRespuesta del agente:")
        print(resultado["respuesta"])
        
        # Guardar consulta
        logger.info("Guardando consulta...")
        agent.guardar_consulta(query, resultado)
        logger.info("Prueba completada exitosamente")
        
    except Exception as e:
        logger.error(f"Error durante la prueba: {str(e)}", exc_info=True)

if __name__ == "__main__":
    asyncio.run(test_agent()) 