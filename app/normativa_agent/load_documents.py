import chromadb
from chromadb.config import Settings
import os
from typing import List, Dict, Any
import json

# Configuración de ChromaDB
COLLECTION_NAME = os.getenv("VECTOR_COLLECTION_NAME", "pdf_documents")

# Documentos de ejemplo sobre granulometría
DOCUMENTOS_GRANULOMETRIA = [
    {
        "contenido": """La granulometría de los agregados debe cumplir con los siguientes requisitos según la NCh163:
        - Para hormigón estructural: Los agregados gruesos deben tener un tamaño máximo nominal de 40mm
        - Para hormigón no estructural: Los agregados gruesos pueden tener un tamaño máximo nominal de 80mm
        - Los agregados finos deben tener un módulo de finura entre 2.3 y 3.1""",
        "metadata": {
            "fuente": "NCh163",
            "norma": "NCh163 - Hormigón - Requisitos generales",
            "año": "2009",
            "tema": "granulometría"
        }
    },
    {
        "contenido": """Según la NCh164, los requisitos de granulometría para agregados son:
        - Agregados gruesos: Deben cumplir con la curva granulométrica especificada en la Tabla 1
        - Agregados finos: Deben cumplir con la curva granulométrica especificada en la Tabla 2
        - El contenido de material más fino que el tamiz N°200 no debe exceder el 1% en peso""",
        "metadata": {
            "fuente": "NCh164",
            "norma": "NCh164 - Agregados para hormigones",
            "año": "2013",
            "tema": "granulometría"
        }
    }
]

def cargar_documentos():
    try:
        # Inicializar cliente ChromaDB
        client = chromadb.PersistentClient(path="chroma_db")
        
        # Obtener o crear colección
        collection = client.get_or_create_collection(COLLECTION_NAME)
        
        # Preparar documentos para inserción
        documentos = []
        metadatos = []
        ids = []
        
        for i, doc in enumerate(DOCUMENTOS_GRANULOMETRIA):
            documentos.append(doc["contenido"])
            metadatos.append(doc["metadata"])
            ids.append(f"doc_{i+1}")
        
        # Insertar documentos
        collection.add(
            documents=documentos,
            metadatas=metadatos,
            ids=ids
        )
        
        print(f"✅ Se cargaron {len(documentos)} documentos en la colección {COLLECTION_NAME}")
        
    except Exception as e:
        print(f"❌ Error al cargar documentos: {str(e)}")

if __name__ == "__main__":
    cargar_documentos() 