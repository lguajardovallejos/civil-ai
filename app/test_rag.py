from pdf_processor.vector_store import VectorStore
from dotenv import load_dotenv
import os

def test_rag():
    load_dotenv()
    vector_store = VectorStore()
    
    # Prueba de búsqueda
    query = "¿Cuáles son los requisitos de granulometría para hormigón estructural?"
    print(f"\nBuscando: {query}")
    
    results = vector_store.search(query, n_results=2)
    
    if results and results.get('documents'):
        print("\nResultados encontrados:")
        for i, doc in enumerate(results['documents'][0], 1):
            print(f"\nDocumento {i}:")
            print(f"Contenido: {doc[:200]}...")
            if results.get('metadatas') and results['metadatas'][0]:
                metadata = results['metadatas'][0][i-1]
                print(f"Archivo: {metadata.get('filename', 'N/A')}")
    else:
        print("No se encontraron resultados")

if __name__ == '__main__':
    test_rag() 