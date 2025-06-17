# Civil AI - Agente de Normativa Chilena

Agente de inteligencia artificial especializado en consultar normativa chilena utilizando una base de datos vectorial.

## Características

- Procesamiento de documentos PDF
- Extracción de texto, imágenes y tablas
- Base de datos vectorial con ChromaDB
- Agente de consulta usando Google ADK
- Respuestas basadas en documentos oficiales

## Requisitos

- Python 3.8+
- Google API Key
- Poppler (para procesamiento de PDFs)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/civil-ai.git
cd civil-ai
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
Crear archivo `.env` con:
```
GOOGLE_API_KEY=tu_api_key
```

## Uso

1. Procesar documentos PDF:
```bash
python app/main.py
```

2. Consultar normativa:
```bash
python app/ejemplo_uso_agent.py
```

## Estructura del Proyecto

```
civil-ai/
├── app/
│   ├── normativa_agent/
│   │   ├── __init__.py
│   │   └── agent.py
│   ├── main.py
│   └── ejemplo_uso_agent.py
├── chroma_db/
├── .env
├── .gitignore
└── README.md
```

## Licencia

MIT 