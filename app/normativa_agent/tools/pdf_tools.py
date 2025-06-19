"""
PDF processing tools for extracting and analyzing document content.
"""

import re
import os
import sys
from typing import Optional
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pdf_processor.processor import PDFProcessor

def process_pdf_document(pdf_path: str) -> str:
    """
    Process a PDF document and extract its content for analysis.
    
    This tool processes PDF documents to extract text, images, and tables,
    making them available for regulatory analysis and verification.
    
    Args:
        pdf_path (str): Path to the PDF file to process
        
    Returns:
        str: Structured content extracted from the PDF with metadata
        
    Example:
        >>> process_pdf_document("memoria_calculo.pdf")
        "PDF PROCESSED:
         - Text extracted: 2500 characters
         - Images found: 5
         - Tables found: 3
         Content: [extracted text content]"
    """
    try:
        if not os.path.exists(pdf_path):
            return f"Error: PDF file not found at {pdf_path}"
        
        processor = PDFProcessor(pdf_path)
        result = processor.process()
        
        # Extract text content
        text_content = result.get('text', '')
        images = result.get('images', [])
        tables = result.get('tables', [])
        
        # Create structured response
        response = f"PDF PROCESSED: {os.path.basename(pdf_path)}\n"
        response += f"- Text extracted: {len(text_content)} characters\n"
        response += f"- Images found: {len(images)}\n"
        response += f"- Tables found: {len(tables)}\n\n"
        
        # Add text content (truncated if too long)
        if text_content:
            if len(text_content) > 2000:
                response += f"TEXT CONTENT (first 2000 chars):\n{text_content[:2000]}...\n\n"
            else:
                response += f"TEXT CONTENT:\n{text_content}\n\n"
        
        # Add table information
        if tables:
            response += "TABLES DETECTED:\n"
            for i, table in enumerate(tables[:3], 1):  # Limit to 3 tables
                response += f"Table {i} (Page {table['page']}):\n"
                for row in table['data'][:5]:  # Limit to 5 rows per table
                    response += f"  {row}\n"
                response += "\n"
        
        # Add image information
        if images:
            response += f"IMAGES DETECTED: {len(images)} images across {len(set(img['page'] for img in images))} pages\n"
        
        return response
        
    except Exception as e:
        return f"Error processing PDF: {str(e)}"

def extract_regulatory_content_from_pdf(pdf_path: str, regulation_code: Optional[str] = None) -> str:
    """
    Extract regulatory content from a PDF document for specific analysis.
    
    This tool processes PDF documents and extracts content relevant to
    regulatory compliance, focusing on calculations, specifications,
    and verification criteria.
    
    Args:
        pdf_path (str): Path to the PDF file to process
        regulation_code (str): Optional regulation code to filter content (e.g., 'NCh430')
        
    Returns:
        str: Extracted regulatory content with analysis
        
    Example:
        >>> extract_regulatory_content_from_pdf("memoria.pdf", "NCh430")
        "REGULATORY CONTENT EXTRACTED:
         - NCh430 references: 5
         - Calculations found: 12
         - Verification statements: 3"
    """
    try:
        if not os.path.exists(pdf_path):
            return f"Error: PDF file not found at {pdf_path}"
        
        processor = PDFProcessor(pdf_path)
        result = processor.process()
        text_content = result.get('text', '')
        
        # Extract regulatory references
        regulation_refs = re.findall(r'NCh[0-9]+', text_content)
        
        # Extract calculations
        calculations = re.findall(r'[0-9]+\s*[+\-*/]\s*[0-9]+', text_content)
        
        # Extract verification statements
        verifications = re.findall(r'verifica|comprueba|revisa|cumple|cumplimiento', text_content, re.IGNORECASE)
        
        # Extract formulas
        formulas = re.findall(r'[A-Za-z]+\s*=\s*[0-9.+\-*/√()²³]+', text_content)
        
        # Filter by specific regulation if provided
        if regulation_code:
            filtered_content = []
            lines = text_content.split('\n')
            for line in lines:
                if regulation_code.lower() in line.lower():
                    filtered_content.append(line)
            text_content = '\n'.join(filtered_content)
        
        response = f"REGULATORY CONTENT EXTRACTED: {os.path.basename(pdf_path)}\n"
        response += f"- Regulation references: {len(set(regulation_refs))}\n"
        response += f"- Calculations found: {len(calculations)}\n"
        response += f"- Verification statements: {len(verifications)}\n"
        response += f"- Formulas identified: {len(formulas)}\n\n"
        
        if regulation_refs:
            response += f"REGULATIONS REFERENCED: {', '.join(set(regulation_refs))}\n\n"
        
        if calculations:
            response += "CALCULATIONS DETECTED:\n"
            for i, calc in enumerate(calculations[:10], 1):  # Limit to 10 calculations
                response += f"{i}. {calc}\n"
            response += "\n"
        
        if formulas:
            response += "FORMULAS IDENTIFIED:\n"
            for i, formula in enumerate(formulas[:10], 1):  # Limit to 10 formulas
                response += f"{i}. {formula}\n"
            response += "\n"
        
        # Add relevant text content
        if text_content and len(text_content) > 100:
            if len(text_content) > 1500:
                response += f"RELEVANT CONTENT (first 1500 chars):\n{text_content[:1500]}...\n"
            else:
                response += f"RELEVANT CONTENT:\n{text_content}\n"
        
        return response
        
    except Exception as e:
        return f"Error extracting regulatory content: {str(e)}"

def analyze_pdf_calculation_memo(pdf_path: str) -> str:
    """
    Analyze a PDF calculation memorandum for regulatory compliance.
    
    This tool processes PDF calculation memorandums and analyzes them
    for regulatory compliance, extracting calculations, formulas, and
    verification criteria for detailed review.
    
    Args:
        pdf_path (str): Path to the PDF calculation memorandum
        
    Returns:
        str: Detailed analysis of the calculation memorandum
        
    Example:
        >>> analyze_pdf_calculation_memo("memoria_calculo.pdf")
        "CALCULATION MEMORANDUM ANALYSIS:
         - Project: Office Building
         - Regulations: NCh430, NCh1537
         - Calculations verified: 15/18"
    """
    try:
        if not os.path.exists(pdf_path):
            return f"Error: PDF file not found at {pdf_path}"
        
        processor = PDFProcessor(pdf_path)
        result = processor.process()
        text_content = result.get('text', '')
        
        # Extract project information
        project_info = re.findall(r'proyecto|obra|edificio|construcción', text_content, re.IGNORECASE)
        
        # Extract regulation references
        regulation_refs = re.findall(r'NCh[0-9]+', text_content)
        
        # Extract calculations
        calculations = re.findall(r'[0-9]+\s*[+\-*/]\s*[0-9]+', text_content)
        
        # Extract formulas
        formulas = re.findall(r'[A-Za-z]+\s*=\s*[0-9.+\-*/√()²³]+', text_content)
        
        # Extract verification statements
        verifications = re.findall(r'verifica|comprueba|revisa|cumple|cumplimiento', text_content, re.IGNORECASE)
        
        # Extract material specifications
        materials = re.findall(r'H[0-9]+|A[0-9]+-[0-9]+H|concreto|hormigón|acero', text_content, re.IGNORECASE)
        
        response = f"CALCULATION MEMORANDUM ANALYSIS: {os.path.basename(pdf_path)}\n"
        response += f"- Project references: {len(project_info)}\n"
        response += f"- Regulations referenced: {len(set(regulation_refs))}\n"
        response += f"- Calculations found: {len(calculations)}\n"
        response += f"- Formulas identified: {len(formulas)}\n"
        response += f"- Verification statements: {len(verifications)}\n"
        response += f"- Material specifications: {len(set(materials))}\n\n"
        
        if regulation_refs:
            response += f"REGULATIONS: {', '.join(set(regulation_refs))}\n\n"
        
        if materials:
            response += f"MATERIALS: {', '.join(set(materials))}\n\n"
        
        # Add key calculations
        if calculations:
            response += "KEY CALCULATIONS:\n"
            for i, calc in enumerate(calculations[:8], 1):  # Limit to 8 calculations
                response += f"{i}. {calc}\n"
            response += "\n"
        
        # Add formulas
        if formulas:
            response += "FORMULAS USED:\n"
            for i, formula in enumerate(formulas[:8], 1):  # Limit to 8 formulas
                response += f"{i}. {formula}\n"
            response += "\n"
        
        # Add verification analysis
        if verifications:
            response += "VERIFICATION STATEMENTS:\n"
            for i, verif in enumerate(verifications[:5], 1):  # Limit to 5 verifications
                response += f"{i}. {verif}\n"
            response += "\n"
        
        return response
        
    except Exception as e:
        return f"Error analyzing calculation memorandum: {str(e)}" 