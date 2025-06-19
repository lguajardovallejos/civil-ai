import asyncio
import logging
from agent import call_agent_async

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def ejemplo_procesamiento_pdf():
    """
    Ejemplo de uso del agente para procesar documentos PDF y verificar cumplimiento normativo.
    """
    
    print("📄 EJEMPLO DE PROCESAMIENTO DE PDF CON AGENTE DE NORMATIVAS")
    print("=" * 70)
    print("Este ejemplo demuestra cómo el agente puede procesar documentos PDF")
    print("y verificar cumplimiento con normativas chilenas.")
    print("=" * 70)
    
    # Ejemplo 1: Procesamiento básico de PDF
    print("\n🔍 EJEMPLO 1: Procesamiento básico de documento PDF")
    print("-" * 50)
    
    query1 = """
    Tengo un documento PDF llamado 'memoria_calculo_edificio.pdf' que contiene 
    una memoria de cálculo para un edificio de hormigón armado. 
    Por favor procesa este documento y extrae su contenido para análisis.
    """
    
    try:
        response1 = await call_agent_async(query1)
        print(f"Respuesta: {response1[:400]}...")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Ejemplo 2: Extracción de contenido normativo específico
    print("\n📋 EJEMPLO 2: Extracción de contenido normativo específico")
    print("-" * 50)
    
    query2 = """
    Del documento PDF 'memoria_calculo_edificio.pdf', extrae específicamente 
    el contenido relacionado con la normativa NCh430 para verificar 
    el cumplimiento de los requisitos de hormigón armado.
    """
    
    try:
        response2 = await call_agent_async(query2)
        print(f"Respuesta: {response2[:400]}...")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Ejemplo 3: Análisis completo de memoria de cálculo
    print("\n📊 EJEMPLO 3: Análisis completo de memoria de cálculo")
    print("-" * 50)
    
    query3 = """
    Analiza completamente la memoria de cálculo en el PDF 'memoria_calculo_edificio.pdf' 
    para verificar el cumplimiento normativo. Busca:
    1. Referencias a normativas chilenas
    2. Cálculos estructurales
    3. Verificaciones de resistencia
    4. Especificaciones de materiales
    5. Criterios de cumplimiento
    """
    
    try:
        response3 = await call_agent_async(query3)
        print(f"Respuesta: {response3[:500]}...")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Ejemplo 4: Verificación de múltiples documentos
    print("\n📚 EJEMPLO 4: Verificación de múltiples documentos")
    print("-" * 50)
    
    query4 = """
    Necesito verificar el cumplimiento normativo de varios documentos PDF:
    1. 'memoria_calculo_edificio.pdf' - Memoria de cálculo estructural
    2. 'estudio_suelos.pdf' - Estudio geotécnico
    3. 'especificaciones_tecnicas.pdf' - Especificaciones técnicas
    
    Por favor procesa cada documento y verifica el cumplimiento con las normativas 
    correspondientes (NCh430 para estructuras, NCh1537 para geotecnia).
    """
    
    try:
        response4 = await call_agent_async(query4)
        print(f"Respuesta: {response4[:500]}...")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Ejemplo 5: Generación de reporte técnico basado en PDF
    print("\n📋 EJEMPLO 5: Generación de reporte técnico basado en PDF")
    print("-" * 50)
    
    query5 = """
    Basándote en el análisis del PDF 'memoria_calculo_edificio.pdf', 
    genera un reporte técnico que incluya:
    1. Resumen ejecutivo del cumplimiento normativo
    2. Análisis de cálculos estructurales
    3. Verificación de especificaciones de materiales
    4. Recomendaciones de mejora si aplica
    5. Referencias específicas a normativas chilenas
    """
    
    try:
        response5 = await call_agent_async(query5)
        print(f"Respuesta: {response5[:500]}...")
    except Exception as e:
        print(f"Error: {str(e)}")

async def ejemplo_contenido_especifico():
    """
    Ejemplo con contenido específico de memoria de cálculo.
    """
    
    print("\n📄 EJEMPLO CON CONTENIDO ESPECÍFICO DE MEMORIA DE CÁLCULO")
    print("=" * 70)
    
    # Simular contenido de un PDF
    contenido_memoria = """
    MEMORIA DE CÁLCULO - ESTRUCTURA DE HORMIGÓN ARMADO
    
    PROYECTO: Edificio Residencial "Las Condes"
    UBICACIÓN: Las Condes, Santiago
    NORMATIVA: NCh430:2008 - Diseño Estructural de Edificios
    
    DATOS DE PROYECTO:
    - Tipo de estructura: Hormigón armado
    - Número de pisos: 15
    - Altura total: 45 metros
    - Zona sísmica: 3
    
    ESPECIFICACIONES DE MATERIALES:
    - Hormigón: H30 (f'c = 30 MPa)
    - Acero de refuerzo: A630-420H (fy = 420 MPa)
    - Módulo elástico hormigón: Ec = 4700 * √30 = 25700 MPa
    
    CÁLCULOS ESTRUCTURALES:
    
    1. ANÁLISIS DE CARGAS:
       Carga muerta: 25 kN/m²
       Carga viva: 20 kN/m²
       Carga sísmica: 0.3g (Zona 3)
    
    2. DISEÑO DE VIGAS:
       Viga principal: 30x60 cm
       Momento máximo: M = 180 kN·m
       Resistencia requerida: Mu = 180 / 0.9 = 200 kN·m
       Armadura requerida: As = 200000000 / (0.9 * 420 * 0.85 * 0.55) = 1130 mm²
       Armadura adoptada: 6φ16 (As = 1206 mm²)
    
    3. DISEÑO DE COLUMNAS:
       Columna típica: 40x40 cm
       Carga axial: P = 1200 kN
       Resistencia requerida: Pu = 1200 / 0.65 = 1846 kN
       Armadura requerida: As = 1846000 / (0.9 * 420) = 4880 mm²
       Armadura adoptada: 8φ25 (As = 3927 mm²) + estribos φ8@15cm
    
    VERIFICACIONES NORMATIVAS:
    
    ✓ Resistencia del hormigón: f'c = 30 MPa ≥ 25 MPa (NCh430 Art. 5.1.1)
    ✓ Cuantía mínima de armadura: ρ = 1.2% ≥ 1.0% (NCh430 Art. 5.4.1)
    ✓ Ductilidad de elementos: μ ≥ 3.0 (NCh430 Art. 5.2.1)
    ✓ Control de fisuración: w ≤ 0.3 mm (NCh430 Art. 5.3.1)
    ✓ Detallado sísmico: Cumple especificaciones NCh430 Cap. 6
    
    CONCLUSIONES:
    La estructura cumple con todos los requisitos de la normativa NCh430:2008
    y está diseñada para resistir las cargas de servicio y sísmicas especificadas.
    """
    
    query = f"""
    Analiza la siguiente memoria de cálculo extraída de un PDF:
    
    {contenido_memoria}
    
    Verifica el cumplimiento con la normativa NCh430:2008 y genera un reporte 
    técnico detallado con las siguientes secciones:
    1. Resumen ejecutivo
    2. Verificación de cálculos
    3. Cumplimiento normativo
    4. Recomendaciones
    """
    
    try:
        response = await call_agent_async(query)
        print(f"Análisis de memoria de cálculo:\n{response}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(ejemplo_procesamiento_pdf())
    asyncio.run(ejemplo_contenido_especifico()) 