import chromadb
import os
from pathlib import Path
from datetime import datetime

# Configuración
CHROMA_DB_PATH = "chroma_db"
COLLECTION_NAME = "pdf_documents"

def test_connection():
    try:
        print(f"Conectando a: {CHROMA_DB_PATH}")
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        
        # Listar todas las colecciones
        collections = client.list_collections()
        print(f"Colecciones encontradas: {len(collections)}")
        
        for collection in collections:
            print(f"- {collection.name}")
        
        # Intentar obtener la colección específica
        try:
            collection = client.get_collection(COLLECTION_NAME)
            print(f"\nColección '{COLLECTION_NAME}' encontrada")
            
            # Obtener todos los documentos
            results = collection.get()
            print(f"Total de documentos: {len(results['ids'])}")
            
            # Analizar metadatos únicos y contenido
            print("\n=== ANÁLISIS DETALLADO ===")
            unique_filenames = set()
            unique_paths = set()
            
            # Diccionario para agrupar por archivo
            archivos_info = {}
            
            for i, metadata in enumerate(results['metadatas']):
                if metadata:
                    filename = metadata.get('filename', '')
                    chunk_index = metadata.get('chunk_index', 0)
                    documento = results['documents'][i]
                    
                    if filename not in archivos_info:
                        archivos_info[filename] = {
                            'chunks': [],
                            'metadata': metadata
                        }
                    
                    archivos_info[filename]['chunks'].append({
                        'index': chunk_index,
                        'content': documento[:200] + "..." if len(documento) > 200 else documento
                    })
                    
                    if 'filename' in metadata:
                        unique_filenames.add(metadata['filename'])
                    if 'path' in metadata:
                        unique_paths.add(metadata['path'])
                    
                    # Mostrar primeros 3 archivos completos
                    if len(archivos_info) <= 3:
                        if i == 0 or chunk_index == 0:  # Solo mostrar el primer chunk de cada archivo
                            print(f"\n📄 ARCHIVO: {filename}")
                            print(f"  📍 Ruta: {metadata.get('path', 'N/A')}")
                            print(f"  📊 Chunks: {len([c for c in results['metadatas'] if c and c.get('filename') == filename])}")
                            print(f"  📝 Primer chunk (índice {chunk_index}):")
                            print(f"    {documento[:300]}...")
                            print("-" * 80)
            
            print(f"\n=== RESUMEN ===")
            print(f"Archivos únicos: {len(unique_filenames)}")
            print(f"Rutas únicas: {len(unique_paths)}")
            
            print(f"\n📋 LISTA COMPLETA DE ARCHIVOS:")
            for i, filename in enumerate(sorted(list(unique_filenames)), 1):
                chunks_count = len([c for c in results['metadatas'] if c and c.get('filename') == filename])
                print(f"  {i:2d}. {filename} ({chunks_count} chunks)")
                
        except Exception as e:
            print(f"Error obteniendo colección: {e}")
            
    except Exception as e:
        print(f"Error conectando: {e}")

if __name__ == "__main__":
    test_connection() 