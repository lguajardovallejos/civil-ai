# Agente de Normativas - Estructura Modular

Este directorio contiene el sistema de agentes de normativas chilenas con una estructura completamente modularizada para mejor organización y mantenibilidad.

## 📁 Estructura de Archivos

```
normativa_agent/
├── config.py                 # Configuraciones centralizadas
├── agents.py                 # Definición de agentes especializados
├── agent_modular.py          # Agente principal modular
├── agent.py                  # Agente original (legacy)
├── tools/                    # Directorio de herramientas
│   ├── __init__.py          # Exportaciones de herramientas
│   ├── regulation_tools.py  # Herramientas de normativas
│   ├── calculation_tools.py # Herramientas de cálculos
│   └── pdf_tools.py         # Herramientas de procesamiento PDF
├── test_modular_structure.py # Pruebas de estructura modular
├── ejemplo_uso_pdf.py        # Ejemplos de uso con PDF
└── README_MODULAR.md         # Este archivo
```

## 🔧 Componentes Principales

### 1. **Configuración (`config.py`)**
- Configuraciones centralizadas del modelo
- Configuraciones de base de datos
- Configuraciones de sesión
- Patrones de expresiones regulares
- Propiedades por defecto de materiales

### 2. **Agentes (`agents.py`)**
- `create_structural_agent()`: Agente especializado en análisis estructural
- `create_geotechnical_agent()`: Agente especializado en geotecnia
- `create_facilities_agent()`: Agente especializado en instalaciones
- `create_review_agent()`: Agente especializado en revisión de documentos
- `create_pdf_processor_agent()`: Agente especializado en procesamiento PDF
- `create_root_agent()`: Agente principal que coordina todos los sub-agentes

### 3. **Herramientas (`tools/`)**

#### **Regulation Tools (`regulation_tools.py`)**
- `search_regulations()`: Búsqueda en base de datos de normativas
- `extract_formulas_from_regulations()`: Extracción de fórmulas de normativas
- `verify_regulatory_compliance()`: Verificación de cumplimiento normativo

#### **Calculation Tools (`calculation_tools.py`)**
- `calculate_specifications()`: Cálculo de especificaciones de materiales
- `analyze_calculation_memo()`: Análisis de memorias de cálculo
- `generate_technical_report()`: Generación de reportes técnicos

#### **PDF Tools (`pdf_tools.py`)**
- `process_pdf_document()`: Procesamiento básico de documentos PDF
- `extract_regulatory_content_from_pdf()`: Extracción de contenido normativo
- `analyze_pdf_calculation_memo()`: Análisis de memorias de cálculo en PDF

## 🚀 Uso

### Uso Básico
```python
from agent_modular import call_agent_async

# Consulta simple
response = await call_agent_async("Search for NCh430 regulations")

# Consulta con procesamiento de PDF
response = await call_agent_async("Process memoria_calculo.pdf and verify NCh430 compliance")
```

### Información del Agente
```python
from agent_modular import get_agent_info

info = get_agent_info()
print(f"Tools: {info['tools_count']}")
print(f"Sub-agents: {info['sub_agents']}")
```

## 🧪 Pruebas

### Ejecutar Pruebas de Estructura Modular
```bash
cd app/normativa_agent
python test_modular_structure.py
```

### Ejecutar Ejemplos de Uso
```bash
python ejemplo_uso_pdf.py
```

## 🔄 Migración desde Estructura Anterior

### Antes (Monolítica)
```python
# Todo en un solo archivo
from agent import call_agent_async
```

### Después (Modular)
```python
# Importaciones específicas
from agent_modular import call_agent_async
from tools import search_regulations
from agents import create_structural_agent
```

## 📋 Ventajas de la Estructura Modular

### 1. **Mantenibilidad**
- Cada herramienta en su propio archivo
- Fácil localización y modificación de funcionalidades
- Separación clara de responsabilidades

### 2. **Escalabilidad**
- Fácil agregar nuevas herramientas
- Fácil agregar nuevos agentes especializados
- Configuración centralizada

### 3. **Testabilidad**
- Pruebas unitarias por herramienta
- Pruebas de integración separadas
- Fácil mockeo de componentes

### 4. **Reutilización**
- Herramientas pueden ser importadas individualmente
- Agentes pueden ser reutilizados en otros contextos
- Configuraciones compartidas

## 🔧 Configuración

### Variables de Entorno
```bash
# Configurar API keys
export GOOGLE_API_KEY="your_api_key"

# Configurar Poppler para PDF processing
export POPPLER_PATH="C:\Program Files\poppler-24.02.0\Library\bin"
```

### Configuraciones en `config.py`
```python
# Modelo a usar
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash-exp"

# Configuraciones de base de datos
CHROMA_DB_PATH = "chroma_db"
COLLECTION_NAME = "pdf_documents"

# Límites de procesamiento
MAX_SEARCH_RESULTS = 5
MAX_TEXT_LENGTH = 2000
```

## 📚 Herramientas Disponibles

### Búsqueda y Análisis de Normativas
- **search_regulations**: Búsqueda en base de datos de normativas
- **extract_formulas_from_regulations**: Extracción de fórmulas
- **verify_regulatory_compliance**: Verificación de cumplimiento

### Cálculos y Análisis
- **calculate_specifications**: Cálculo de especificaciones
- **analyze_calculation_memo**: Análisis de memorias
- **generate_technical_report**: Generación de reportes

### Procesamiento de PDF
- **process_pdf_document**: Procesamiento básico de PDF
- **extract_regulatory_content_from_pdf**: Extracción de contenido normativo
- **analyze_pdf_calculation_memo**: Análisis de memorias en PDF

## 🤖 Agentes Especializados

1. **structural_agent**: Análisis estructural y hormigón armado
2. **geotechnical_agent**: Geotecnia y fundaciones
3. **facilities_agent**: Instalaciones sanitarias y eléctricas
4. **review_agent**: Revisión de documentos técnicos
5. **pdf_processor_agent**: Procesamiento especializado de PDF

## 🔄 Flujo de Trabajo

1. **Entrada**: Consulta del usuario
2. **Análisis**: El agente principal analiza la consulta
3. **Delegación**: Delega a sub-agentes especializados según sea necesario
4. **Procesamiento**: Las herramientas procesan la información
5. **Verificación**: Se verifica contra normativas almacenadas
6. **Respuesta**: Se genera una respuesta estructurada

## 🚨 Solución de Problemas

### Error de Importación
```python
# Asegúrate de que el directorio esté en el path
import sys
sys.path.append('/path/to/normativa_agent')
```

### Error de Base de Datos
```python
# Verifica que ChromaDB esté configurado correctamente
from tools.regulation_tools import search_regulations
result = search_regulations("test")
```

### Error de PDF Processing
```python
# Verifica que Poppler esté instalado y configurado
export POPPLER_PATH="C:\Program Files\poppler-24.02.0\Library\bin"
``` 