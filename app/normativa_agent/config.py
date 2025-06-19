"""
Configuration settings for the regulatory agent.
"""

# Model configuration
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash-exp"

# Application configuration
APP_NAME = "normativa_agent"

# Database configuration
CHROMA_DB_PATH = "chroma_db"
COLLECTION_NAME = "pdf_documents"

# Session configuration
DEFAULT_USER_ID = "user_001"
DEFAULT_SESSION_ID = "session_001"

# Tool configuration
MAX_SEARCH_RESULTS = 5
MAX_FORMULA_RESULTS = 3
MAX_CALCULATION_RESULTS = 10
MAX_VERIFICATION_RESULTS = 5

# PDF processing configuration
MAX_TEXT_LENGTH = 2000
MAX_CONTENT_LENGTH = 1500
MAX_TABLE_ROWS = 5
MAX_TABLES = 3
MAX_IMAGES = 10

# Regulation patterns
REGULATION_PATTERN = r'NCh[0-9]+'
CALCULATION_PATTERN = r'[0-9]+\s*[+\-*/]\s*[0-9]+'
FORMULA_PATTERN = r'[A-Za-z]+\s*=\s*[0-9.+\-*/√()²³]+'
VERIFICATION_PATTERN = r'verifica|comprueba|revisa|cumple|cumplimiento'
MATERIAL_PATTERN = r'H[0-9]+|A[0-9]+-[0-9]+H|concreto|hormigón|acero'

# Default material properties
DEFAULT_CONCRETE_STRENGTH = 25  # MPa
DEFAULT_STEEL_YIELD = 420  # MPa
DEFAULT_STEEL_MODULUS = 200000  # MPa

# Chilean regulations
CHILEAN_REGULATIONS = {
    "NCh430": "Diseño Estructural de Edificios - Hormigón Armado",
    "NCh1537": "Diseño Estructural de Edificios - Cargas",
    "NCh2369": "Diseño Estructural de Edificios - Acero",
    "NCh433": "Diseño Sísmico de Edificios",
    "NCh1537": "Diseño Estructural de Edificios - Cargas",
    "NCh432": "Hormigón Armado - Cálculo y Diseño"
} 