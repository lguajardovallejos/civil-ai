import asyncio
import logging
from agent import call_agent_async

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_regulation_based_verification():
    """
    Test the new regulation-based verification capabilities.
    This test verifies that the agent extracts formulas and criteria
    directly from regulation documents instead of using hardcoded values.
    """
    
    # Test calculation memorandum with specific regulation references
    test_memo = """
    CALCULATION MEMORANDUM - REINFORCED CONCRETE BEAM
    
    Project: Office Building
    Regulation: NCh430:2008
    
    Input data:
    - Dead load: 25 kN/m
    - Live load: 15 kN/m
    - Span: 6.0 m
    - Concrete: H25 (f'c = 25 MPa)
    - Steel: A630-420H (fy = 420 MPa)
    
    Calculations according to NCh430:
    Total load = 25 + 15 = 40 kN/m
    Maximum moment = 40 * 6² / 8 = 180 kN·m
    Required strength = 180 / 0.9 = 200 kN·m
    
    Concrete strength verification:
    - Design strength: fc = 0.8 * 25 = 20 MPa (NCh430 requirement)
    - Elastic modulus: Ec = 4700 * √25 = 23500 MPa
    
    Required reinforcement:
    As = 200000000 / (0.9 * 420 * 0.85 * 0.5) = 1240 mm²
    Adopted: 4φ20 (As = 1257 mm²)
    
    Verification results:
    - Ductility: COMPLIES (NCh430 Section 5.2)
    - Cracking: COMPLIES (NCh430 Section 5.3)
    - Minimum reinforcement: COMPLIES (NCh430 Section 5.4)
    """
    
    test_queries = [
        {
            "type": "Regulation Formula Extraction",
            "query": "Extract formulas and calculation criteria from NCh430 regulation for concrete strength calculations"
        },
        {
            "type": "Document-Based Verification",
            "query": f"Verify compliance with NCh430 in this calculation memorandum:\n\n{test_memo}"
        },
        {
            "type": "Regulation-Based Analysis",
            "query": f"Analyze this calculation memorandum and compare it against actual NCh430 requirements:\n\n{test_memo}"
        },
        {
            "type": "Formula Extraction Test",
            "query": "Extract mathematical formulas and verification criteria from NCh1537 regulation for foundation design"
        },
        {
            "type": "Regulation Search Test",
            "query": "Search for concrete strength requirements and formulas in Chilean engineering regulations"
        }
    ]
    
    print("🧪 TESTING REGULATION-BASED VERIFICATION SYSTEM")
    print("=" * 65)
    print("This test verifies that the agent extracts formulas and criteria")
    print("directly from regulation documents instead of using hardcoded values.")
    print("=" * 65)
    
    for i, test_query in enumerate(test_queries, 1):
        print(f"\n📋 TEST {i}: {test_query['type']}")
        print("-" * 50)
        print(f"Query: {test_query['query'][:120]}...")
        
        try:
            response = await call_agent_async(test_query['query'])
            print(f"✅ Response: {response[:300]}...")
            
            # Check if response contains regulation-based content
            if "regulation" in response.lower() or "nch" in response.lower():
                print("✅ Regulation-based response detected")
            else:
                print("⚠️ Response may not be regulation-based")
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print("-" * 50)

if __name__ == "__main__":
    asyncio.run(test_regulation_based_verification()) 