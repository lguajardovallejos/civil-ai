import os
import logging
from dotenv import load_dotenv
from pdf_processor.processor import PDFProcessor
from pdf_processor.vector_store import VectorStore

logging.basicConfig(filename='pdf_processing.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def load_pdfs_from_directory(pdf_directory: str):
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        logging.error('No se encontró GOOGLE_API_KEY en el entorno')
        print('No se encontró GOOGLE_API_KEY en el entorno')
        return
    
    vector_store = VectorStore()
    processed_count = 0
    error_count = 0
    
    for filename in os.listdir(pdf_directory):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)
            try:
                logging.info(f'Procesando: {filename}')
                processor = PDFProcessor(pdf_path)
                data = processor.process()
                vector_store.add_document(data, {'filename': filename, 'path': pdf_path})
                logging.info(f'Procesado y almacenado: {filename}')
                print(f'Procesado: {filename}')
                processed_count += 1
            except Exception as e:
                logging.error(f'Error en {filename}: {str(e)}')
                print(f'Error en {filename}: {str(e)}')
                error_count += 1
    
    print(f'\nResumen:')
    print(f'PDFs procesados exitosamente: {processed_count}')
    print(f'PDFs con error: {error_count}')

if __name__ == '__main__':
    pdf_directory = r"C:\Users\GH\Desktop\Normas"
    load_pdfs_from_directory(pdf_directory) 