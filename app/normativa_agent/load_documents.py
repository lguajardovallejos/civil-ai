import chromadb
from chromadb.config import Settings
import os
from typing import List, Dict, Any
import json

# Configuración de ChromaDB
COLLECTION_NAME = os.getenv("VECTOR_COLLECTION_NAME", "pdf_documents")

# Base de datos expandida de normativas chilenas
NORMATIVAS_CHILENAS = [
    # Estructural - Hormigón
    {
        "contenido": """NCh430 - Hormigón Armado - Requisitos de Diseño y Cálculo:
        - Resistencia característica del hormigón: f'c ≥ 25 MPa para estructuras
        - Resistencia de diseño: fc = 0.8 * f'c
        - Módulo de elasticidad: Ec = 4700 * √f'c
        - Deformación unitaria máxima: εc = 0.003""",
        "metadata": {"fuente": "NCh430", "norma": "NCh430 - Hormigón Armado", "año": "2008", "tema": "estructural_hormigon"}
    },
    {
        "contenido": """NCh163 - Hormigón - Requisitos Generales:
        - Agregados gruesos: tamaño máximo nominal 40mm para estructural
        - Agregados finos: módulo de finura entre 2.3 y 3.1
        - Contenido de aire: 4-8% para hormigón expuesto a congelamiento
        - Consistencia: según método de compactación""",
        "metadata": {"fuente": "NCh163", "norma": "NCh163 - Hormigón", "año": "2009", "tema": "estructural_hormigon"}
    },
    # Estructural - Acero
    {
        "contenido": """NCh2369 - Diseño Estructural de Edificios - Antecedentes y Criterios de Diseño:
        - Acero estructural: Grado A630-420H (fy=420 MPa, fu=630 MPa)
        - Factor de reducción: φ = 0.9 para tracción, φ = 0.85 para compresión
        - Deformación máxima: L/360 para cargas de servicio
        - Estabilidad lateral: verificar pandeo en elementos comprimidos""",
        "metadata": {"fuente": "NCh2369", "norma": "NCh2369 - Diseño Estructural", "año": "2003", "tema": "estructural_acero"}
    },
    # Geotécnico - Suelos
    {
        "contenido": """NCh1537 - Diseño Estructural de Edificios - Cargas de Diseño:
        - Capacidad de soporte del suelo: qadm ≥ 2 kg/cm² para fundaciones superficiales
        - Asentamiento máximo: 2.5 cm para estructuras convencionales
        - Profundidad mínima: 0.8 m para fundaciones aisladas
        - Factor de seguridad: FS ≥ 3 para capacidad de soporte""",
        "metadata": {"fuente": "NCh1537", "norma": "NCh1537 - Cargas de Diseño", "año": "2009", "tema": "geotecnico_suelos"}
    },
    {
        "contenido": """NCh433 - Diseño Sísmico de Edificios:
        - Zona sísmica: clasificación según aceleración máxima del suelo
        - Coeficiente sísmico: C = A0 * I * R / T
        - Período fundamental: T = Ct * H^(3/4)
        - Ductilidad: μ ≥ 4 para estructuras de hormigón armado""",
        "metadata": {"fuente": "NCh433", "norma": "NCh433 - Diseño Sísmico", "año": "2012", "tema": "geotecnico_sismico"}
    },
    # Instalaciones - Sanitarias
    {
        "contenido": """NCh Agua - Instalaciones Domiciliarias de Agua Potable:
        - Presión mínima: 10 m.c.a. en cualquier punto de la red
        - Presión máxima: 50 m.c.a. para evitar daños
        - Diámetro mínimo: 13 mm para conexiones domiciliarias
        - Materiales: cobre, PVC, polietileno según presión de servicio""",
        "metadata": {"fuente": "NCh Agua", "norma": "NCh Agua - Agua Potable", "año": "2018", "tema": "instalaciones_sanitarias"}
    },
    {
        "contenido": """NCh Elec - Instalaciones Eléctricas de Consumo:
        - Tensión nominal: 220/380V para instalaciones domiciliarias
        - Potencia mínima: 3.5 kW por vivienda
        - Factor de demanda: 0.7 para viviendas unifamiliares
        - Protecciones: interruptor diferencial obligatorio""",
        "metadata": {"fuente": "NCh Elec", "norma": "NCh Elec - Instalaciones Eléctricas", "año": "2017", "tema": "instalaciones_electricas"}
    },
    # Urbanismo
    {
        "contenido": """OGUC - Ordenanza General de Urbanismo y Construcciones:
        - Densidad máxima: según zonificación urbana
        - Altura máxima: según plano regulador comunal
        - Estacionamientos: 1 por cada 50m² de construcción
        - Áreas verdes: 15% mínimo del terreno""",
        "metadata": {"fuente": "OGUC", "norma": "OGUC - Urbanismo y Construcciones", "año": "2021", "tema": "urbanismo"}
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
        
        for i, doc in enumerate(NORMATIVAS_CHILENAS):
            documentos.append(doc["contenido"])
            metadatos.append(doc["metadata"])
            ids.append(f"norma_{i+1}")
        
        # Insertar documentos
        collection.add(
            documents=documentos,
            metadatas=metadatos,
            ids=ids
        )
        
        print(f"✅ Se cargaron {len(documentos)} normativas en la colección {COLLECTION_NAME}")
        
    except Exception as e:
        print(f"❌ Error al cargar documentos: {str(e)}")

if __name__ == "__main__":
    cargar_documentos() 