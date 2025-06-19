import asyncio
import logging
from agent import call_agent_async

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_pdf_processing_capabilities():
    """
    Test the new PDF processing capabilities of the regulatory agent.
    This test verifies that the agent can process PDF documents and
    extract regulatory content for analysis.
    """
    
    # Test queries for PDF processing
    test_queries = [
        {
            "type": "PDF Document Processing",
            "query": "Process a PDF document called 'memoria_calculo.pdf' and extract its content for analysis"
        },
        {
            "type": "Regulatory Content Extraction",
            "query": "Extract regulatory content from 'memoria_calculo.pdf' focusing on NCh430 requirements"
        },
        {
            "type": "PDF Calculation Memo Analysis",
            "query": "Analyze the PDF calculation memorandum 'memoria_calculo.pdf' for regulatory compliance"
        },
        {
            "type": "PDF Processing with Regulation Search",
            "query": "Process 'memoria_calculo.pdf' and search for relevant NCh430 regulations to verify compliance"
        },
        {
            "type": "Multi-PDF Analysis",
            "query": "Process multiple PDF documents: 'memoria_calculo.pdf', 'especificaciones.pdf' and analyze them for regulatory compliance"
        }
    ]
    
    print("🧪 TESTING PDF PROCESSING CAPABILITIES")
    print("=" * 60)
    print("This test verifies that the agent can process PDF documents")
    print("and extract regulatory content for analysis.")
    print("=" * 60)
    
    for i, test_query in enumerate(test_queries, 1):
        print(f"\n📋 TEST {i}: {test_query['type']}")
        print("-" * 50)
        print(f"Query: {test_query['query'][:100]}...")
        
        try:
            response = await call_agent_async(test_query['query'])
            print(f"✅ Response: {response[:300]}...")
            
            # Check if response contains PDF processing content
            if "pdf" in response.lower() or "document" in response.lower():
                print("✅ PDF processing response detected")
            else:
                print("⚠️ Response may not be PDF processing related")
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print("-" * 50)

async def test_pdf_with_sample_content():
    """
    Test PDF processing with sample content to verify functionality.
    """
    
    print("\n🧪 TESTING PDF PROCESSING WITH SAMPLE CONTENT")
    print("=" * 60)
    
    # Test with a hypothetical PDF analysis
    test_query = """
    I have a PDF calculation memorandum with the following content:
    
    MEMORIA DE CÁLCULO - VIGA DE HORMIGÓN ARMADO
    
    Proyecto: Edificio de Oficinas
    Normativa: NCh430:2008
    
    Datos de entrada:
    - Carga muerta: 25 kN/m
    - Carga viva: 15 kN/m
    - Luz: 6.0 m
    - Hormigón: H25 (f'c = 25 MPa)
    - Acero: A630-420H (fy = 420 MPa)
    
    Cálculos según NCh430:
    Carga total = 25 + 15 = 40 kN/m
    Momento máximo = 40 * 6² / 8 = 180 kN·m
    Resistencia requerida = 180 / 0.9 = 200 kN·m
    
    Verificación de resistencia del hormigón:
    - Resistencia de diseño: fc = 0.8 * 25 = 20 MPa (requisito NCh430)
    - Módulo elástico: Ec = 4700 * √25 = 23500 MPa
    
    Armadura requerida:
    As = 200000000 / (0.9 * 420 * 0.85 * 0.5) = 1240 mm²
    Adoptado: 4φ20 (As = 1257 mm²)
    
    Resultados de verificación:
    - Ductilidad: CUMPLE (NCh430 Sección 5.2)
    - Fisuración: CUMPLE (NCh430 Sección 5.3)
    - Armadura mínima: CUMPLE (NCh430 Sección 5.4)
    
    Please analyze this calculation memorandum for regulatory compliance.
    """
    
    try:
        response = await call_agent_async(test_query)
        print(f"✅ Analysis Response: {response[:500]}...")
        
        # Check for regulatory analysis indicators
        if "nch430" in response.lower() or "regulation" in response.lower():
            print("✅ Regulatory analysis detected")
        else:
            print("⚠️ Response may not include regulatory analysis")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_pdf_processing_capabilities())
    asyncio.run(test_pdf_with_sample_content()) 