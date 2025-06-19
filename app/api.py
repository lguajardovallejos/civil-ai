from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import chromadb
from chromadb.config import Settings
import os
from pathlib import Path
import re
from datetime import datetime, timedelta
import random

app = FastAPI(title="API de Normativas", version="1.0.0")

# Configurar CORS para el dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de la base de datos vectorial
COLLECTION_NAME = os.getenv("VECTOR_COLLECTION_NAME", "pdf_documents")
CHROMA_DB_PATH = "../chroma_db"

class NormativaItem(BaseModel):
    id: str
    norma: str
    titulo: str
    año: str
    tema: str
    tipo: str
    pagina: Optional[int] = None

class NormativaResponse(BaseModel):
    normativas: List[NormativaItem]
    total: int
    estadisticas: Dict[str, Any]

def get_vector_store():
    try:
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        collection = client.get_collection(COLLECTION_NAME)
        return collection
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error conectando a la base de datos: {str(e)}")

def extraer_info_documento(filename):
    """Extrae información detallada del nombre del archivo"""
    # Mapeo de instituciones
    instituciones = {
        'NCh': 'Instituto Nacional de Normalización (INN) - Chile',
        'AISC': 'American Institute of Steel Construction',
        'ASCE': 'American Society of Civil Engineers',
        'SEI': 'Structural Engineering Institute',
        'DS': 'Decreto Supremo - Chile'
    }
    
    # Extraer código principal
    codigo = ""
    institucion = "Desconocida"
    titulo = filename.replace('.pdf', '')
    
    # Buscar códigos conocidos
    for cod in instituciones.keys():
        if cod in filename:
            codigo = cod
            institucion = instituciones[cod]
            break
    
    # Extraer año si existe
    año_match = re.search(r'(\d{4})', filename)
    año = año_match.group(1) if año_match else "N/A"
    
    # Mejorar título basado en códigos
    if 'NCh' in filename:
        if '203' in filename:
            titulo = "Norma Chilena NCh 203 - Diseño Estructural de Edificios"
        elif '427' in filename:
            titulo = "Norma Chilena NCh 427 - Cálculo de Estructuras de Acero"
        elif '430' in filename:
            titulo = "Norma Chilena NCh 430 - Diseño Estructural de Edificios"
        elif '431' in filename:
            titulo = "Norma Chilena NCh 431 - Cargas de Nieve"
        elif '432' in filename:
            titulo = "Norma Chilena NCh 432 - Cargas de Viento"
        elif '433' in filename:
            titulo = "Norma Chilena NCh 433 - Diseño Estructural de Edificios"
        elif '1508' in filename:
            titulo = "Norma Chilena NCh 1508 - Diseño Estructural"
        elif '1537' in filename:
            titulo = "Norma Chilena NCh 1537 - Diseño Estructural"
        elif '2369' in filename:
            titulo = "Norma Chilena NCh 2369 - Diseño Sísmico de Estructuras"
        elif '3171' in filename:
            titulo = "Norma Chilena NCh 3171 - Diseño Estructural"
    elif 'AISC' in filename:
        if '341' in filename:
            titulo = "AISC 341-10 - Seismic Provisions for Structural Steel Buildings"
        elif 'Design Guide' in filename:
            titulo = "AISC Design Guide - " + filename.split('Design Guide')[1].split('.pdf')[0]
    elif 'ASCE' in filename:
        titulo = "ASCE/SEI 41-17 - Seismic Evaluation and Retrofit of Existing Buildings"
    
    return {
        "codigo": codigo,
        "institucion": institucion,
        "año": año,
        "titulo": titulo
    }

def generar_fecha_carga():
    """Genera una fecha de carga aleatoria en los últimos 2 años"""
    fecha_actual = datetime.now()
    dias_atras = random.randint(1, 730)  # Últimos 2 años
    return (fecha_actual - timedelta(days=dias_atras)).strftime("%Y-%m-%d")

@app.get("/")
async def root():
    return {"message": "API de Normativas Civil AI"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@app.get("/api/normativas")
async def get_normativas():
    try:
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        collection = client.get_collection(COLLECTION_NAME)
        results = collection.get()
        
        # Agrupar por archivo único
        archivos_unicos = {}
        for i, metadata in enumerate(results['metadatas']):
            if metadata and 'filename' in metadata:
                filename = metadata['filename']
                if filename not in archivos_unicos:
                    info = extraer_info_documento(filename)
                    archivos_unicos[filename] = {
                        "id": len(archivos_unicos) + 1,
                        "filename": filename,
                        "titulo": info["titulo"],
                        "codigo": info["codigo"],
                        "institucion": info["institucion"],
                        "año": info["año"],
                        "tipo": info["codigo"] if info["codigo"] else "Otro",
                        "chunks": 0,
                        "fecha_carga": generar_fecha_carga()
                    }
                archivos_unicos[filename]["chunks"] += 1
        
        normativas = list(archivos_unicos.values())
        
        # Estadísticas
        total_documentos = len(normativas)
        normativas_unicas = len(set(norm.get('codigo', '') for n in normativas if n.get('codigo')))
        
        return {
            "normativas": normativas,
            "estadisticas": {
                "total_documentos": total_documentos,
                "normativas_unicas": normativas_unicas
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/api/estadisticas")
async def get_estadisticas():
    try:
        collection = get_vector_store()
        results = collection.get()
        
        if not results['ids']:
            return {
                "total_documentos": 0,
                "normas_unicas": 0
            }
        
        # Calcular estadísticas
        normas_unicas = set()
        
        for metadata in results['metadatas']:
            if metadata:
                filename = metadata.get('filename', '')
                if filename:
                    # Usar la misma lógica de extracción que en get_normativas
                    norma = "Desconocida"
                    año = "Desconocido"
                    
                    # Patrón 1: NCh chilenas
                    if 'NCh' in filename and '-' in filename:
                        partes = filename.replace('.pdf', '').split('-')
                        for parte in partes:
                            if parte.startswith('NCh'):
                                norma = parte
                                break
                        
                        for parte in partes:
                            if len(parte) == 4 and parte.isdigit():
                                año = parte
                                break
                    
                    # Patrón 2: NCh con guión bajo
                    elif 'NCh' in filename and '_' in filename:
                        partes = filename.replace('.pdf', '').split('_')
                        if len(partes) >= 2:
                            norma = partes[1]
                            if '-' in norma:
                                norma_parte, año = norma.split('-', 1)
                                norma = norma_parte
                    
                    # Patrón 3: Documento_NCh
                    elif 'NCh' in filename:
                        import re
                        match = re.search(r'NCh(\d+)', filename)
                        if match:
                            norma = f"NCh{match.group(1)}"
                        
                        year_match = re.search(r'(\d{4})', filename)
                        if year_match:
                            año = year_match.group(1)
                    
                    # Patrón 4: AISC Design Guides
                    elif 'AISC' in filename and 'Design Guide' in filename:
                        import re
                        match = re.search(r'AISC Design Guide (\d+)', filename)
                        if match:
                            numero = match.group(1)
                            norma = f"AISC DG {numero}"
                        else:
                            norma = "AISC Design Guide"
                        año = "Internacional"
                    
                    # Patrón 5: ASCE
                    elif 'ASCE' in filename:
                        import re
                        match = re.search(r'ASCE_SEI (\d+)-(\d+)', filename)
                        if match:
                            norma = f"ASCE/SEI {match.group(1)}"
                            año = match.group(2)
                        else:
                            norma = "ASCE/SEI"
                            año = "Internacional"
                    
                    # Patrón 6: Otros documentos internacionales
                    elif any(keyword in filename for keyword in ['Design_guide', 'Design guide']):
                        nombre = filename.replace('.pdf', '').replace('_', ' ')
                        norma = nombre[:30] + "..." if len(nombre) > 30 else nombre
                        año = "Internacional"
                    
                    # Patrón 7: Otros documentos
                    else:
                        nombre = filename.replace('.pdf', '').replace('_', ' ')
                        norma = nombre[:30] + "..." if len(nombre) > 30 else nombre
                        año = "Desconocido"
                    
                    normas_unicas.add(f"{norma}_{año}")
        
        return {
            "total_documentos": len(results['ids']),
            "normas_unicas": len(normativas_unicas)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error obteniendo estadísticas: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 