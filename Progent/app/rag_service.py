"""
RAG (Retrieval-Augmented Generation) Service for ArcGIS Pro Smart Assistant
Handles knowledge base operations for initial instructions and software state
"""

import os
import json
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

logger = logging.getLogger(__name__)

class RAGService:
    """Service for managing RAG operations with ChromaDB and sentence transformers"""
    
    def __init__(self, persist_directory: str = "rag_db"):
        self.persist_directory = persist_directory
        self.client = None
        self.collection = None
        self.embedder = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
    async def initialize(self):
        """Initialize RAG service components"""
        try:
            # Initialize ChromaDB
            self.client = chromadb.PersistentClient(path=self.persist_directory)
            self.collection = self.client.get_or_create_collection(
                name="arcgis_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            
            # Initialize sentence transformer for embeddings
            self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
            
            logger.info("RAG service initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize RAG service: {e}")
            raise
    
    def initialize_knowledge_base(self):
        """Initialize knowledge base with ArcGIS and application documentation"""
        try:
            # Create knowledge base directory if it doesn't exist
            knowledge_dir = Path("knowledge_base")
            knowledge_dir.mkdir(exist_ok=True)
            
            # Create default knowledge documents
            self._create_default_knowledge_docs(knowledge_dir)
            
            # Load and process documents
            documents = self._load_documents(knowledge_dir)
            
            if documents:
                self._add_documents_to_collection(documents)
                logger.info(f"Knowledge base initialized with {len(documents)} documents")
            
        except Exception as e:
            logger.error(f"Failed to initialize knowledge base: {e}")
            raise
    
    def _create_default_knowledge_docs(self, knowledge_dir: Path):
        """Create default knowledge documents for ArcGIS Pro"""
        
        # ArcGIS Pro basics
        arcgis_basics = """
        # ArcGIS Pro Basics
        
        ArcGIS Pro is a powerful desktop GIS application for creating maps, performing spatial analysis, and managing geographic data.
        
        ## Key Components:
        - **Project**: Container for maps, layouts, tools, and data
        - **Map**: Interactive display of geographic data
        - **Layers**: Datasets displayed on a map
        - **Geodatabase**: Database for storing and managing geographic data
        - **Toolbox**: Collection of geoprocessing tools
        
        ## Common Tasks:
        - Adding data to maps
        - Symbolizing layers
        - Performing spatial analysis
        - Creating layouts and maps
        - Managing geodatabases
        
        ## Spatial Analysis Functions:
        - Buffer analysis
        - Overlay operations (intersect, union, clip)
        - Proximity analysis
        - Statistical analysis
        - Attribute queries
        - Spatial queries
        """
        
        # Smart Assistant capabilities
        assistant_capabilities = """
        # ArcGIS Pro Smart Assistant Capabilities
        
        The Smart Assistant can help you with various GIS tasks and analysis.
        
        ## Available Functions:
        - **Layer Analysis**: Get summaries, statistics, and field information
        - **Spatial Selection**: Select features by attribute or location
        - **Geometry Calculations**: Calculate area, length, centroids
        - **Buffer Operations**: Create buffers around features
        - **Statistical Analysis**: Get field statistics and unique value counts
        - **Data Queries**: Query and filter data based on criteria
        
        ## How to Use:
        1. Ask questions about your data in natural language
        2. Request specific analysis or calculations
        3. Get help with spatial operations
        4. Receive data-driven insights and summaries
        
        ## Supported AI Models:
        - Gemini 1.5 Flash/Pro
        - GPT-4
        - Claude 3.5 Sonnet
        - Ollama (Local LLMs)
        """
        
        # Spatial analysis concepts
        spatial_concepts = """
        # Spatial Analysis Concepts
        
        ## Buffer Analysis
        Buffer analysis creates zones of specified distances around features. Useful for:
        - Finding features within a certain distance
        - Creating service areas
        - Analyzing proximity relationships
        
        ## Overlay Operations
        - **Intersect**: Finds areas where features overlap
        - **Union**: Combines features from multiple layers
        - **Clip**: Cuts features using another layer as a boundary
        
        ## Attribute Queries
        Select features based on attribute values using SQL expressions:
        - Equality: field_name = 'value'
        - Comparison: field_name > 100
        - Pattern matching: field_name LIKE '%pattern%'
        
        ## Spatial Queries
        Select features based on spatial relationships:
        - Contains
        - Intersects
        - Within distance
        - Touches
        """
        
        # Write knowledge documents
        with open(knowledge_dir / "arcgis_basics.md", "w", encoding="utf-8") as f:
            f.write(arcgis_basics)
            
        with open(knowledge_dir / "assistant_capabilities.md", "w", encoding="utf-8") as f:
            f.write(progent_capabilities)
            
        with open(knowledge_dir / "spatial_concepts.md", "w", encoding="utf-8") as f:
            f.write(spatial_concepts)
    
    def _load_documents(self, knowledge_dir: Path) -> List[Document]:
        """Load documents from knowledge directory"""
        documents = []
        
        for file_path in knowledge_dir.glob("*.md"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                doc = Document(
                    page_content=content,
                    metadata={
                        "source": str(file_path),
                        "filename": file_path.name,
                        "type": "knowledge_base"
                    }
                )
                documents.append(doc)
                
            except Exception as e:
                logger.error(f"Error loading document {file_path}: {e}")
        
        return documents
    
    def _add_documents_to_collection(self, documents: List[Document]):
        """Add documents to ChromaDB collection"""
        try:
            if not self.embedder:
                self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
            
            # Split documents into chunks
            chunks = []
            for doc in documents:
                doc_chunks = self.text_splitter.split_documents([doc])
                chunks.extend(doc_chunks)
            
            # Prepare data for ChromaDB
            texts = [chunk.page_content for chunk in chunks]
            metadatas = [chunk.metadata for chunk in chunks]
            ids = [f"doc_{i}" for i in range(len(chunks))]
            
            # Generate embeddings
            embeddings = self.embedder.encode(texts).tolist()
            
            # Add to collection
            self.collection.add(
                documents=texts,
                metadatas=metadatas,
                ids=ids,
                embeddings=embeddings
            )
            
            logger.info(f"Added {len(chunks)} document chunks to knowledge base")
            
        except Exception as e:
            logger.error(f"Error adding documents to collection: {e}")
            raise
    
    async def query_knowledge_base(self, query: str, n_results: int = 3) -> List[Dict[str, Any]]:
        """Query the knowledge base for relevant information"""
        try:
            if not self.collection or not self.embedder:
                await self.initialize()
            
            # Generate query embedding
            query_embedding = self.embedder.encode([query]).tolist()[0]
            
            # Query the collection
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results,
                include=["documents", "metadatas", "distances"]
            )
            
            # Format results
            formatted_results = []
            if results["documents"] and len(results["documents"]) > 0:
                for i, doc in enumerate(results["documents"][0]):
                    formatted_results.append({
                        "content": doc,
                        "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                        "score": 1 - results["distances"][0][i] if results["distances"] else 0
                    })
            
            return formatted_results
            
        except Exception as e:
            logger.error(f"Error querying knowledge base: {e}")
            return []
    
    def add_arcgis_state_to_knowledge(self, arcgis_state: Dict[str, Any]):
        """Add current ArcGIS state to knowledge base for future reference"""
        try:
            if not arcgis_state:
                return
            
            # Create document from ArcGIS state
            state_content = f"""
            # Current ArcGIS Pro State
            
            ## Project Information
            Workspace: {arcgis_state.get('workspace', 'N/A')}
            Default GDB: {arcgis_state.get('default_gdb', 'N/A')}
            Basemap: {arcgis_state.get('basemap', 'N/A')}
            
            ## Available Layers
            """
            
            if "layers_info" in arcgis_state:
                for layer_name, layer_info in arcgis_state["layers_info"].items():
                    state_content += f"""
                    ### {layer_name}
                    - Type: {layer_info.get('type', 'Unknown')}
                    - Feature Count: {layer_info.get('feature_count', 'Unknown')}
                    - Fields: {', '.join(layer_info.get('fields', []))}
                    """
            
            # Add to knowledge base (this could be used for context in future sessions)
            # For now, we'll just log it - you might want to implement persistent state storage
            logger.info("ArcGIS state added to knowledge context")
            
        except Exception as e:
            logger.error(f"Error adding ArcGIS state to knowledge: {e}")
    
    async def get_relevant_context(self, user_message: str, arcgis_state: Dict[str, Any]) -> str:
        """Get relevant context from knowledge base for user message"""
        try:
            # Query knowledge base for relevant information
            knowledge_results = await self.query_knowledge_base(user_message, n_results=2)
            
            context = ""
            
            # Add knowledge base context
            if knowledge_results:
                context += "## Relevant Knowledge:\n"
                for result in knowledge_results:
                    if result["score"] > 0.5:  # Only include highly relevant results
                        context += f"{result['content']}\n\n"
            
            # Add current ArcGIS state context (always included)
            if arcgis_state:
                context += "## Current ArcGIS Pro State:\n"
                context += json.dumps(arcgis_state, indent=2)
            
            return context
            
        except Exception as e:
            logger.error(f"Error getting relevant context: {e}")
            return json.dumps(arcgis_state, indent=2) if arcgis_state else ""
