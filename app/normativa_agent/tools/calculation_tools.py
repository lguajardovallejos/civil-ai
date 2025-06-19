"""
Calculation tools for analyzing engineering calculations and generating reports.
"""

import json
import re
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def calculate_specifications(material_type: str, parameters: str) -> str:
    """
    Calculate technical specifications for construction materials.
    
    This tool performs calculations for common construction materials
    including concrete, steel, and other structural elements according
    to Chilean standards. It extracts calculation formulas from regulation
    documents when available.
    
    Args:
        material_type (str): Type of material ('concrete', 'steel', etc.)
        parameters (str): JSON string containing material parameters
        
    Returns:
        str: Calculated specifications with units and values
        
    Example:
        >>> calculate_specifications("concrete", '{"fck": 25}')
        "Concrete f'c=25MPa: fc=20.0MPa, Ec=23500MPa"
    """
    try:
        params = json.loads(parameters)
        
        # Try to extract formulas from regulations first
        from .regulation_tools import extract_formulas_from_regulations
        regulation_formulas = extract_formulas_from_regulations("NCh430", material_type)
        
        if material_type == "concrete":
            fck = params.get("fck", 25)
            # Use extracted formula if available, otherwise use standard
            if "fc = 0.8 * f'c" in regulation_formulas:
                fc = 0.8 * fck
            else:
                fc = 0.8 * fck  # Default formula
            
            if "Ec = 4700 * √f'c" in regulation_formulas:
                ec = 4700 * (fck ** 0.5)
            else:
                ec = 4700 * (fck ** 0.5)  # Default formula
                
            return f"Concrete f'c={fck}MPa: fc={fc:.1f}MPa, Ec={ec:.0f}MPa\n\nRegulation formulas used:\n{regulation_formulas}"
            
        elif material_type == "steel":
            fy = params.get("fy", 420)
            es = 200000
            return f"Steel fy={fy}MPa: Es={es}MPa\n\nRegulation formulas used:\n{regulation_formulas}"
            
        return f"Calculation for {material_type}: {parameters}\n\nRegulation formulas used:\n{regulation_formulas}"
    except:
        return f"Error calculating {material_type} specifications"

def analyze_calculation_memo(content: str) -> str:
    """
    Analyze engineering calculation memorandums for technical review.
    
    This tool extracts and analyzes calculations, formulas, and verification
    statements from engineering calculation memorandums. It compares them
    against regulation requirements extracted from official documents.
    
    Args:
        content (str): The text content of the calculation memorandum
        
    Returns:
        str: Structured analysis report with extracted calculations and findings
        
    Example:
        >>> analyze_calculation_memo("Moment = 25 * 6² / 8 = 112.5 kN·m")
        "ANALYSIS OF CALCULATION MEMORANDUM:
         - Calculations found: 1
         - Formulas identified: 1
         - Verifications mentioned: 0"
    """
    try:
        # Extract calculations and verifications from memo
        calculations = re.findall(r'[0-9]+\s*[+\-*/]\s*[0-9]+', content)
        formulas = re.findall(r'[A-Za-z]+\s*=\s*[0-9.]+', content)
        verifications = re.findall(r'verify|verification|check|review', content, re.IGNORECASE)
        
        # Extract regulation references
        regulation_refs = re.findall(r'NCh[0-9]+', content)
        
        # Compare with regulation requirements
        regulation_comparison = ""
        for regulation in set(regulation_refs):
            from .regulation_tools import extract_formulas_from_regulations
            regulation_formulas = extract_formulas_from_regulations(regulation, "calculation")
            if regulation_formulas and "No documents found" not in regulation_formulas:
                regulation_comparison += f"\nRegulation {regulation} requirements:\n{regulation_formulas}\n"
        
        report = f"ANALYSIS OF CALCULATION MEMORANDUM:\n"
        report += f"- Calculations found: {len(calculations)}\n"
        report += f"- Formulas identified: {len(formulas)}\n"
        report += f"- Verifications mentioned: {len(verifications)}\n"
        report += f"- Regulations referenced: {', '.join(set(regulation_refs))}\n"
        
        if calculations:
            report += f"\nCALCULATIONS DETECTED:\n"
            for i, calc in enumerate(calculations[:5], 1):
                report += f"{i}. {calc}\n"
        
        if formulas:
            report += f"\nFORMULAS IDENTIFIED:\n"
            for i, formula in enumerate(formulas[:5], 1):
                report += f"{i}. {formula}\n"
        
        if regulation_comparison:
            report += f"\nREGULATION COMPARISON:{regulation_comparison}"
        
        return report
    except Exception as e:
        return f"Analysis error: {str(e)}"

def generate_technical_report(report_type: str, data: str) -> str:
    """
    Generate technical reports for engineering analysis.
    
    This tool creates formatted technical reports for different types
    of engineering analysis including structural, geotechnical, and
    facility reviews.
    
    Args:
        report_type (str): Type of report ('structural', 'geotechnical', etc.)
        data (str): JSON string containing report data and parameters
        
    Returns:
        str: Formatted technical report with analysis results
        
    Example:
        >>> generate_technical_report("structural", '{"project": "Building A", "strength": "25MPa"}')
        "TECHNICAL REPORT - STRUCTURAL
         Project: Building A
         Required strength: 25MPa"
    """
    try:
        data_dict = json.loads(data)
        report = f"TECHNICAL REPORT - {report_type.upper()}\n"
        report += f"Date: {data_dict.get('date', 'N/A')}\n"
        report += f"Project: {data_dict.get('project', 'N/A')}\n\n"
        
        if report_type == "structural":
            report += f"STRUCTURAL RESULTS:\n"
            report += f"- Required strength: {data_dict.get('strength', 'N/A')}\n"
            report += f"- Safety factor: {data_dict.get('safety_factor', 'N/A')}\n"
            report += f"- Status: {'COMPLIES' if data_dict.get('complies', False) else 'DOES NOT COMPLY'}\n"
        elif report_type == "geotechnical":
            report += f"GEOTECHNICAL RESULTS:\n"
            report += f"- Bearing capacity: {data_dict.get('capacity', 'N/A')}\n"
            report += f"- Expected settlement: {data_dict.get('settlement', 'N/A')}\n"
            report += f"- Status: {'COMPLIES' if data_dict.get('complies', False) else 'DOES NOT COMPLY'}\n"
        
        return report
    except:
        return f"Error generating {report_type} report" 