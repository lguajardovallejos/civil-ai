"""
Specialized agents for regulatory analysis and PDF processing.
"""

from google.adk import Agent
from .config import MODEL_GEMINI_2_0_FLASH
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

def create_structural_agent() -> Agent:
    """Create the structural analysis agent."""
    return Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="structural_agent",
        description="Specialist in structural analysis, reinforced concrete and structural element verification",
        instruction="Analyze structural elements using formulas and criteria extracted from NCh430 regulation documents. Process PDF documents and verify calculations against actual regulation requirements."
    )

def create_geotechnical_agent() -> Agent:
    """Create the geotechnical analysis agent."""
    return Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="geotechnical_agent", 
        description="Specialist in geotechnics, foundations and soil analysis",
        instruction="Analyze soil studies and foundation calculations using criteria extracted from NCh1537 regulation documents. Process PDF documents and verify against actual regulation requirements."
    )

def create_facilities_agent() -> Agent:
    """Create the facilities analysis agent."""
    return Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="facilities_agent",
        description="Specialist in sanitary, electrical and mechanical facilities",
        instruction="Review facilities using criteria from relevant Chilean facility regulations. Process PDF documents and extract verification requirements from regulation documents."
    )

def create_review_agent() -> Agent:
    """Create the document review agent."""
    return Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="review_agent",
        description="Specialist in reviewing calculation memorandums and technical documents",
        instruction="Analyze calculation memorandums by comparing them against formulas and criteria extracted from regulation documents. Process PDF documents and identify discrepancies with actual regulation requirements."
    )

def create_pdf_processor_agent() -> Agent:
    """Create the PDF processing agent."""
    return Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="pdf_processor_agent",
        description="Specialist in processing PDF documents and extracting regulatory content",
        instruction="Process PDF documents to extract text, images, tables, and regulatory content. Focus on calculation memorandums, technical specifications, and regulatory compliance documents."
    )

def create_root_agent(tools) -> Agent:
    """Create the main regulatory agent with all sub-agents."""
    return Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="main_regulatory_agent",
        instruction="""You are a specialized agent in Chilean civil engineering regulations. 
        You can review calculation memorandums, technical documents and verify regulatory compliance.
        
        IMPORTANT: Always base your verifications on actual regulation documents, not generic knowledge.
        Use the available tools to:
        1. Search for relevant regulations in the document database
        2. Extract formulas and calculation criteria directly from regulation documents
        3. Analyze calculation memorandums against extracted regulation requirements
        4. Verify regulatory compliance using criteria from official documents
        5. Generate technical reports with regulation-based calculations
        6. Calculate material specifications using formulas from regulation documents
        7. Process PDF documents and extract their content for analysis
        8. Extract regulatory content from PDF documents for specific analysis
        9. Analyze PDF calculation memorandums for regulatory compliance
        
        When processing PDF documents:
        - Use process_pdf_document() to extract text, images, and tables from PDFs
        - Use extract_regulatory_content_from_pdf() to focus on regulatory content
        - Use analyze_pdf_calculation_memo() for detailed analysis of calculation memorandums
        - Always verify extracted content against regulation requirements
        
        When verifying compliance:
        - First search for the specific regulation in the database
        - Extract verification criteria and formulas from regulation documents
        - Compare the technical document against these extracted criteria
        - Provide specific references to regulation sections and formulas used
        
        Always cite regulations with format [Regulation]of[Year] and provide precise technical responses
        based on actual regulation content, not general knowledge.""",
        tools=tools,
        sub_agents=[
            create_structural_agent(),
            create_geotechnical_agent(),
            create_facilities_agent(),
            create_review_agent(),
            create_pdf_processor_agent()
        ]
    ) 