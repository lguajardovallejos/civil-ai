"""
Main regulatory agent module.
This module orchestrates the regulatory analysis system using modular tools and agents.
"""

import asyncio
from google.adk import Runner, FunctionTool, types
from google.adk.services import InMemorySessionService
from typing import Optional

# Import modular components
from .config import APP_NAME, DEFAULT_USER_ID, DEFAULT_SESSION_ID
from .tools import (
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
from .agents import create_root_agent

# Session service configuration
session_service = InMemorySessionService()

# Create tools list
tools = [
    FunctionTool(search_regulations),
    FunctionTool(extract_formulas_from_regulations),
    FunctionTool(verify_regulatory_compliance),
    FunctionTool(calculate_specifications),
    FunctionTool(analyze_calculation_memo),
    FunctionTool(generate_technical_report),
    FunctionTool(process_pdf_document),
    FunctionTool(extract_regulatory_content_from_pdf),
    FunctionTool(analyze_pdf_calculation_memo)
]

# Create root agent with all tools and sub-agents
root_agent = create_root_agent(tools)

# Configure runner
runner = Runner(
    app_name=APP_NAME,
    agent=root_agent,
    session_service=session_service
)

async def call_agent_async(query: str, user_id: Optional[str] = None, session_id: Optional[str] = None):
    """
    Call the regulatory agent asynchronously.
    
    Args:
        query (str): The query to send to the agent
        user_id (str): Optional user ID (defaults to DEFAULT_USER_ID)
        session_id (str): Optional session ID (defaults to DEFAULT_SESSION_ID)
        
    Returns:
        str: The agent's response
    """
    try:
        # Use default values if not provided
        user_id = user_id or DEFAULT_USER_ID
        session_id = session_id or DEFAULT_SESSION_ID
        
        # Create session explicitly before execution
        try:
            await session_service.create_session(
                app_name=APP_NAME,
                user_id=user_id,
                session_id=session_id
            )
        except Exception:
            pass  # If already exists, ignore
        
        content = types.Content(role='user', parts=[types.Part(text=query)])
        final_response_text = "Agent did not produce a final response."
        
        async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
            if event.is_final_response():
                if event.content and event.content.parts:
                    final_response_text = event.content.parts[0].text
                break
        return final_response_text
    except Exception as e:
        return f"Error: {str(e)}"

def get_agent_info():
    """
    Get information about the configured agent and tools.
    
    Returns:
        dict: Information about the agent configuration
    """
    return {
        "agent_name": root_agent.name,
        "model": root_agent.model,
        "tools_count": len(tools),
        "sub_agents_count": len(root_agent.sub_agents),
        "sub_agents": [agent.name for agent in root_agent.sub_agents],
        "tools": [tool.name for tool in tools]
    }

if __name__ == "__main__":
    # Example usage
    async def main():
        print("🔧 REGULATORY AGENT SYSTEM")
        print("=" * 50)
        
        # Show agent information
        info = get_agent_info()
        print(f"Agent: {info['agent_name']}")
        print(f"Model: {info['model']}")
        print(f"Tools: {info['tools_count']}")
        print(f"Sub-agents: {info['sub_agents_count']}")
        print(f"Sub-agents: {', '.join(info['sub_agents'])}")
        print("=" * 50)
        
        # Test the agent
        test_query = "Can you review a reinforced concrete calculation memorandum?"
        print(f"Testing with query: {test_query}")
        
        response = await call_agent_async(test_query)
        print(f"Response: {response[:200]}...")
    
    asyncio.run(main()) 