"""
Tools module for the regulatory agent.
Contains all specialized tools for regulatory analysis and PDF processing.
"""

from .regulation_tools import (
    search_regulations,
    extract_formulas_from_regulations,
    verify_regulatory_compliance
)

from .calculation_tools import (
    calculate_specifications,
    analyze_calculation_memo,
    generate_technical_report
)

from .pdf_tools import (
    process_pdf_document,
    extract_regulatory_content_from_pdf,
    analyze_pdf_calculation_memo
)

__all__ = [
    # Regulation tools
    'search_regulations',
    'extract_formulas_from_regulations', 
    'verify_regulatory_compliance',
    
    # Calculation tools
    'calculate_specifications',
    'analyze_calculation_memo',
    'generate_technical_report',
    
    # PDF tools
    'process_pdf_document',
    'extract_regulatory_content_from_pdf',
    'analyze_pdf_calculation_memo'
] 