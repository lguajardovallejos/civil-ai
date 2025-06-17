import os
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import uuid

class VectorStore:
    def __init__(self, persist_directory: str = "chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name="pdf_documents")
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def add_document(self, document: Dict[str, Any], metadata: Dict[str, str]):
        # Procesar texto
        if document.get('text'):
            chunks = self.text_splitter.split_text(document['text'])
            for i, chunk in enumerate(chunks):
                chunk_id = str(uuid.uuid4())
                self.collection.add(
                    ids=[chunk_id],
                    documents=[chunk],
                    metadatas=[{**metadata, 'type': 'text', 'chunk_index': i}]
                )

        # Procesar imágenes
        if document.get('images'):
            for i, img in enumerate(document['images']):
                img_id = str(uuid.uuid4())
                self.collection.add(
                    ids=[img_id],
                    documents=[img['data']],
                    metadatas=[{**metadata, 'type': 'image', 'page': img['page'], 'index': i}]
                )

        # Procesar tablas
        if document.get('tables'):
            for i, table in enumerate(document['tables']):
                table_id = str(uuid.uuid4())
                self.collection.add(
                    ids=[table_id],
                    documents=[str(table)],
                    metadatas=[{**metadata, 'type': 'table', 'index': i}]
                )

    def search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results 