import asyncio
import logging
from agent import call_agent_async

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_calculation_memos():
    # Example calculation memorandum
    calculation_memo = """
    CALCULATION MEMORANDUM - MAIN BEAM
    
    Input data:
    - Dead load: 25 kN/m
    - Live load: 15 kN/m
    - Span: 6.0 m
    - Concrete: H25 (f'c = 25 MPa)
    - Steel: A630-420H (fy = 420 MPa)
    
    Calculations:
    Total load = 25 + 15 = 40 kN/m
    Maximum moment = 40 * 6² / 8 = 180 kN·m
    Required strength = 180 / 0.9 = 200 kN·m
    
    Verification according to NCh430:2008
    - Design strength: fc = 0.8 * 25 = 20 MPa
    - Elastic modulus: Ec = 4700 * √25 = 23500 MPa
    
    Required reinforcement:
    As = 200000000 / (0.9 * 420 * 0.85 * 0.5) = 1240 mm²
    Adopted: 4φ20 (As = 1257 mm²)
    
    Ductility verification: COMPLIES
    Cracking verification: COMPLIES
    """
    
    test_queries = [
        {
            "type": "Calculation Memo Analysis",
            "query": f"Analyze this calculation memorandum and verify if it complies with Chilean regulations:\n\n{calculation_memo}"
        },
        {
            "type": "Regulatory Compliance",
            "query": "Verify compliance with NCh430 in the following reinforced concrete calculation memorandum"
        },
        {
            "type": "Material Specifications",
            "query": "Calculate specifications for H30 concrete and A630-420H steel according to Chilean standards"
        },
        {
            "type": "Technical Report",
            "query": "Generate a structural technical report for an 8-story building project with H25 concrete"
        },
        {
            "type": "Complete Review",
            "query": "Review this calculation memorandum and generate a complete regulatory compliance report"
        }
    ]
    
    print("🧪 TESTING CALCULATION MEMORANDUM REVIEW SYSTEM")
    print("=" * 60)
    
    for i, test_query in enumerate(test_queries, 1):
        print(f"\n📋 TEST {i}: {test_query['type']}")
        print("-" * 40)
        print(f"Query: {test_query['query'][:100]}...")
        
        try:
            response = await call_agent_async(test_query['query'])
            print(f"✅ Response: {response[:200]}...")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(test_calculation_memos()) 