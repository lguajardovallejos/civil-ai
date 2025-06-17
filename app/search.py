import os
import time
from pdf_processor.vector_store import VectorStore
from dotenv import load_dotenv
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def search_document(query: str):
    try:
        # Cargar variables de entorno
        load_dotenv()
        
        # Verificar API key
        if not os.getenv('GOOGLE_API_KEY'):
            raise ValueError("No se encontró la API key de Google")
        
        # Inicializar el almacenamiento vectorial
        vector_store = VectorStore()
        
        # Realizar la búsqueda
        start = time.time()
        results = vector_store.search(query, 1)
        elapsed = time.time() - start
        
        # Mostrar resultados
        print(f"\nResultados para: '{query}' (tiempo: {elapsed:.2f}s)")
        print("-" * 50)
        
        docs = results.get('documents', [[]])[0]
        if not docs:
            print("No se encontraron resultados")
            return
            
        print(f"Texto: {docs[0][:200]}...")
        if 'metadatas' in results and results['metadatas'][0]:
            metadata = results['metadatas'][0][0]
            print(f"Tipo: {metadata.get('type', 'N/A')}")
            print(f"Página: {metadata.get('page', 'N/A')}")
            print(f"Archivo: {metadata.get('filename', 'N/A')}")
        print("-" * 50)
        
    except Exception as e:
        logging.error(f"Error en la búsqueda: {str(e)}")
        raise

if __name__ == "__main__":
    search_document("acero") 