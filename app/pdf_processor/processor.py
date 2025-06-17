import os
import logging
from typing import List, Dict, Any
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import io
import base64

class PDFProcessor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.reader = PdfReader(pdf_path)
        
        # Configurar Poppler
        self.poppler_path = os.getenv('POPPLER_PATH')
        if not self.poppler_path:
            # Intentar encontrar Poppler en ubicaciones comunes
            common_paths = [
                r"C:\Program Files\poppler-24.02.0\Library\bin",
                r"C:\Program Files\poppler-23.11.0\Library\bin",
                r"C:\Program Files\poppler\Library\bin",
                r"C:\poppler-24.02.0\Library\bin",
                r"C:\poppler\Library\bin"
            ]
            for path in common_paths:
                if os.path.exists(path):
                    self.poppler_path = path
                    logging.info(f"Poppler encontrado en: {path}")
                    break
            
            if not self.poppler_path:
                logging.warning("Poppler no encontrado. La extracción de imágenes puede fallar.")
                logging.warning("Por favor, instala Poppler y configura POPPLER_PATH en el archivo .env")
                logging.warning("Descarga Poppler desde: https://github.com/oschwartz10612/poppler-windows/releases/")
                logging.warning("Extrae en C:\\Program Files\\poppler-24.02.0 y configura la ruta en .env")
        
    def extract_text(self) -> str:
        text = ""
        for page in self.reader.pages:
            text += page.extract_text() + "\n"
        return text
    
    def extract_images(self) -> List[Dict[str, Any]]:
        images = []
        try:
            for page_num in range(len(self.reader.pages)):
                try:
                    page = self.reader.pages[page_num]
                    if '/Resources' in page and '/XObject' in page['/Resources']:
                        xObject = page['/Resources']['/XObject'].get_object()
                        for obj in xObject:
                            if xObject[obj]['/Subtype'] == '/Image':
                                try:
                                    data = xObject[obj].get_data()
                                    image = Image.open(io.BytesIO(data))
                                    buffered = io.BytesIO()
                                    image.save(buffered, format="PNG")
                                    img_str = base64.b64encode(buffered.getvalue()).decode()
                                    images.append({
                                        'page': page_num + 1,
                                        'data': img_str,
                                        'size': image.size
                                    })
                                except Exception as e:
                                    logging.warning(f"Error procesando imagen en página {page_num + 1}: {str(e)}")
                                    # Intentar convertir la página completa a imagen
                                    try:
                                        if self.poppler_path:
                                            page_images = convert_from_path(
                                                self.pdf_path,
                                                first_page=page_num + 1,
                                                last_page=page_num + 1,
                                                poppler_path=self.poppler_path
                                            )
                                        else:
                                            page_images = convert_from_path(
                                                self.pdf_path,
                                                first_page=page_num + 1,
                                                last_page=page_num + 1
                                            )
                                        if page_images:
                                            img = page_images[0]
                                            buffered = io.BytesIO()
                                            img.save(buffered, format="PNG")
                                            img_str = base64.b64encode(buffered.getvalue()).decode()
                                            images.append({
                                                'page': page_num + 1,
                                                'data': img_str,
                                                'size': img.size
                                            })
                                    except Exception as e2:
                                        logging.error(f"Error al convertir página {page_num + 1} a imagen: {str(e2)}")
                except Exception as e:
                    logging.error(f"Error procesando página {page_num + 1}: {str(e)}")
        except Exception as e:
            logging.error(f"Error general en extract_images: {str(e)}")
        return images
    
    def extract_tables(self) -> List[Dict[str, Any]]:
        tables = []
        for page_num in range(len(self.reader.pages)):
            page = self.reader.pages[page_num]
            text = page.extract_text()
            lines = text.split('\n')
            current_table = []
            for line in lines:
                if '|' in line or '\t' in line:
                    current_table.append(line)
                elif current_table:
                    tables.append({
                        'page': page_num + 1,
                        'data': current_table
                    })
                    current_table = []
            if current_table:
                tables.append({
                    'page': page_num + 1,
                    'data': current_table
                })
        return tables
    
    def process(self) -> Dict[str, Any]:
        return {
            'text': self.extract_text(),
            'images': self.extract_images(),
            'tables': self.extract_tables()
        } 