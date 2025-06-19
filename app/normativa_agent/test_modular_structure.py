"""
Test the modular structure of the regulatory agent system.
"""

import asyncio
import logging
from agent_modular import call_agent_async, get_agent_info

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_modular_structure():
    """
    Test the modular structure and functionality of the regulatory agent.
    """
    
    print("🧪 TESTING MODULAR STRUCTURE")
    print("=" * 60)
    
    # Test 1: Check agent configuration
    print("\n📋 TEST 1: Agent Configuration")
    print("-" * 40)
    
    try:
        info = get_agent_info()
        print(f"✅ Agent name: {info['agent_name']}")
        print(f"✅ Model: {info['model']}")
        print(f"✅ Tools count: {info['tools_count']}")
        print(f"✅ Sub-agents count: {info['sub_agents_count']}")
        print(f"✅ Sub-agents: {', '.join(info['sub_agents'])}")
        print(f"✅ Tools: {', '.join(info['tools'])}")
    except Exception as e:
        print(f"❌ Error getting agent info: {str(e)}")
    
    # Test 2: Test basic functionality
    print("\n🔍 TEST 2: Basic Functionality")
    print("-" * 40)
    
    test_queries = [
        "Search for NCh430 regulations about concrete strength",
        "Calculate specifications for concrete with fck=30MPa",
        "Analyze this calculation: Moment = 25 * 6² / 8 = 112.5 kN·m"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\nQuery {i}: {query[:50]}...")
        try:
            response = await call_agent_async(query)
            print(f"✅ Response: {response[:100]}...")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    # Test 3: Test PDF processing tools
    print("\n📄 TEST 3: PDF Processing Tools")
    print("-" * 40)
    
    pdf_queries = [
        "Process a PDF document called 'memoria_calculo.pdf'",
        "Extract regulatory content from 'memoria.pdf' focusing on NCh430",
        "Analyze the PDF calculation memorandum 'memoria_calculo.pdf'"
    ]
    
    for i, query in enumerate(pdf_queries, 1):
        print(f"\nQuery {i}: {query[:50]}...")
        try:
            response = await call_agent_async(query)
            print(f"✅ Response: {response[:100]}...")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    # Test 4: Test regulation-based verification
    print("\n📋 TEST 4: Regulation-Based Verification")
    print("-" * 40)
    
    verification_queries = [
        "Extract formulas from NCh430 regulation for concrete strength",
        "Verify compliance with NCh430 in a concrete calculation document",
        "Search for Chilean engineering regulations about structural design"
    ]
    
    for i, query in enumerate(verification_queries, 1):
        print(f"\nQuery {i}: {query[:50]}...")
        try:
            response = await call_agent_async(query)
            print(f"✅ Response: {response[:100]}...")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

async def test_tool_imports():
    """
    Test that all tools can be imported correctly.
    """
    
    print("\n🔧 TEST 5: Tool Imports")
    print("-" * 40)
    
    try:
        from tools import (
            search_regulations,
            extract_formulas_from_regulations,
            verify_regulatory_compliance,
            calculate_specifications,
            analyze_calculation_memo,
            generate_technical_report,
            process_pdf_document,
            extract_regulatory_content_from_pdf,
            analyze_pdf_calculation_memo
        )
        print("✅ All tools imported successfully")
        
        # Test individual tool functions
        tools_to_test = [
            ("search_regulations", search_regulations),
            ("extract_formulas_from_regulations", extract_formulas_from_regulations),
            ("calculate_specifications", calculate_specifications),
            ("analyze_calculation_memo", analyze_calculation_memo),
            ("generate_technical_report", generate_technical_report)
        ]
        
        for tool_name, tool_func in tools_to_test:
            try:
                # Test with minimal input
                if tool_name == "search_regulations":
                    result = tool_func("test")
                elif tool_name == "extract_formulas_from_regulations":
                    result = tool_func("NCh430", "test")
                elif tool_name == "calculate_specifications":
                    result = tool_func("concrete", '{"fck": 25}')
                elif tool_name == "analyze_calculation_memo":
                    result = tool_func("test content")
                elif tool_name == "generate_technical_report":
                    result = tool_func("structural", '{"project": "test"}')
                
                print(f"✅ {tool_name}: Function call successful")
            except Exception as e:
                print(f"⚠️ {tool_name}: {str(e)}")
                
    except Exception as e:
        print(f"❌ Error importing tools: {str(e)}")

async def test_agent_creation():
    """
    Test that agents can be created correctly.
    """
    
    print("\n🤖 TEST 6: Agent Creation")
    print("-" * 40)
    
    try:
        from agents import (
            create_structural_agent,
            create_geotechnical_agent,
            create_facilities_agent,
            create_review_agent,
            create_pdf_processor_agent
        )
        print("✅ Agent creation functions imported successfully")
        
        # Test creating individual agents
        agents_to_test = [
            ("structural_agent", create_structural_agent),
            ("geotechnical_agent", create_geotechnical_agent),
            ("facilities_agent", create_facilities_agent),
            ("review_agent", create_review_agent),
            ("pdf_processor_agent", create_pdf_processor_agent)
        ]
        
        for agent_name, create_func in agents_to_test:
            try:
                agent = create_func()
                print(f"✅ {agent_name}: Created successfully")
                print(f"   - Name: {agent.name}")
                print(f"   - Model: {agent.model}")
            except Exception as e:
                print(f"❌ {agent_name}: {str(e)}")
                
    except Exception as e:
        print(f"❌ Error creating agents: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_modular_structure())
    asyncio.run(test_tool_imports())
    asyncio.run(test_agent_creation()) 