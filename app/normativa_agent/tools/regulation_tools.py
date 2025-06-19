"""
Regulation tools for searching and analyzing Chilean engineering regulations.
"""

import re
import chromadb
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def search_regulations(query: str) -> str:
    """
    Search for Chilean civil engineering regulations in the vector database.
    
    This tool searches through the ChromaDB collection containing Chilean
    engineering standards and regulations (NCh430, NCh1537, NCh2369, etc.)
    to find relevant information for the given query.
    
    Args:
        query (str): The search query describing the regulation or technical requirement
        
    Returns:
        str: Formatted results containing relevant regulation excerpts and metadata
        
    Example:
        >>> search_regulations("concrete strength requirements")
        "Document 1: NCh430 specifies minimum concrete strength...
         Source: NCh430 - Hormigón Armado"
    """
    try:
        client = chromadb.PersistentClient(path="chroma_db")
        collection = client.get_collection("pdf_documents")
        results = collection.query(query_texts=[query], n_results=5)
        
        if results['documents'] and results['documents'][0]:
            docs = []
            for i, doc in enumerate(results['documents'][0]):
                metadata = results['metadatas'][0][i] if results['metadatas'] else {}
                docs.append(f"Document {i+1}: {doc}\nSource: {metadata.get('source', 'N/A')}\nRegulation: {metadata.get('regulation', 'N/A')}")
            return "\n\n".join(docs)
        return "No relevant documents found."
    except Exception as e:
        return f"Search error: {str(e)}"

def extract_formulas_from_regulations(regulation_code: str, context: str) -> str:
    """
    Extract formulas and calculation criteria from specific regulations.
    
    This tool searches for mathematical formulas, calculation procedures,
    and verification criteria within the specified regulation documents.
    
    Args:
        regulation_code (str): The regulation code (e.g., 'NCh430', 'NCh1537')
        context (str): The specific context or element to search for
        
    Returns:
        str: Extracted formulas and calculation criteria from the regulation
        
    Example:
        >>> extract_formulas_from_regulations("NCh430", "concrete strength")
        "Formula: fc = 0.8 * f'c
         Verification: f'c ≥ 25 MPa for structural elements"
    """
    try:
        client = chromadb.PersistentClient(path="chroma_db")
        collection = client.get_collection("pdf_documents")
        
        # Search for the specific regulation and context
        search_query = f"{regulation_code} {context} formula calculation criteria"
        results = collection.query(
            query_texts=[search_query], 
            n_results=3,
            where={"regulation": regulation_code} if regulation_code else None
        )
        
        if results['documents'] and results['documents'][0]:
            formulas = []
            for i, doc in enumerate(results['documents'][0]):
                # Extract mathematical expressions and formulas
                math_expressions = re.findall(r'[A-Za-z]+\s*=\s*[0-9.+\-*/√()²³]+', doc)
                verification_criteria = re.findall(r'[A-Za-z]+\s*[≥≤=]\s*[0-9.]+', doc)
                
                if math_expressions or verification_criteria:
                    formulas.append(f"From Document {i+1}:\n")
                    if math_expressions:
                        formulas.append("Formulas found:")
                        for expr in math_expressions[:3]:  # Limit to 3 formulas
                            formulas.append(f"- {expr}")
                    if verification_criteria:
                        formulas.append("Verification criteria:")
                        for crit in verification_criteria[:3]:  # Limit to 3 criteria
                            formulas.append(f"- {crit}")
                    formulas.append("")
            
            if formulas:
                return "\n".join(formulas)
            else:
                return f"No specific formulas found in {regulation_code} for {context}"
        return f"No documents found for {regulation_code} regulation"
    except Exception as e:
        return f"Formula extraction error: {str(e)}"

def verify_regulatory_compliance(document: str, regulation: str) -> str:
    """
    Verify compliance with specific Chilean engineering regulations.
    
    This tool checks if a technical document complies with specified
    Chilean engineering standards by extracting verification criteria
    directly from regulation documents and applying them to the document.
    
    Args:
        document (str): The technical document content to verify
        regulation (str): The regulation code to check against (e.g., 'NCh430')
        
    Returns:
        str: Compliance verification report with findings and status
        
    Example:
        >>> verify_regulatory_compliance("Concrete strength 25MPa...", "NCh430")
        "VERIFICATION COMPLIANCE NCh430:
         - References found: 2
         - Critical elements verified: 3/4"
    """
    try:
        # Search for regulation references in document
        refs_regulation = re.findall(rf'{regulation}[^0-9]*([0-9]+)', document, re.IGNORECASE)
        
        # Extract verification criteria from regulation documents
        client = chromadb.PersistentClient(path="chroma_db")
        collection = client.get_collection("pdf_documents")
        
        # Search for verification criteria in the regulation
        verification_query = f"{regulation} verification criteria requirements"
        results = collection.query(
            query_texts=[verification_query], 
            n_results=3,
            where={"regulation": regulation} if regulation else None
        )
        
        verification_criteria = []
        if results['documents'] and results['documents'][0]:
            for doc in results['documents'][0]:
                # Extract verification requirements from regulation text
                criteria = re.findall(r'[A-Za-z\s]+\s*[≥≤=]\s*[0-9.]+', doc)
                verification_criteria.extend(criteria)
        
        # Check document against extracted criteria
        compliance_results = []
        for criterion in verification_criteria[:5]:  # Check first 5 criteria
            if re.search(criterion.split()[0], document, re.IGNORECASE):
                compliance_results.append(f"✓ {criterion}")
            else:
                compliance_results.append(f"✗ {criterion} - NOT FOUND")
        
        report = f"VERIFICATION COMPLIANCE {regulation.upper()}:\n"
        report += f"- References found: {len(refs_regulation)}\n"
        report += f"- Verification criteria checked: {len(compliance_results)}\n\n"
        
        if compliance_results:
            report += "COMPLIANCE CHECK RESULTS:\n"
            for result in compliance_results:
                report += f"{result}\n"
        
        return report
    except Exception as e:
        return f"Verification error: {str(e)}" 