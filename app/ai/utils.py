import logging
logger = logging.getLogger(__name__)

class AIUtils:
    @staticmethod
    def test_ollama_server():
        """Test if Ollama server is running and accessible"""
        try:
            import requests
            from ..config import settings

            # Test if Ollama server is running
            response = requests.get(f"{settings.OLLAMA_BASE_URL}/api/tags", timeout=5)
            return response.status_code == 200
        except Exception as e:
            logger.info(f"Ollama server test failed: {e}")
            return False

# Service availability flags and service classes
OLLAMA_AVAILABLE = False
RAG_AVAILABLE = False
OllamaService = None
RAGService = None

# Test Ollama server first
if AIUtils.test_ollama_server():
    try:
        from ..ollama_service import OllamaService
        OLLAMA_AVAILABLE = True
        logger.info("Ollama service imported successfully - server is accessible")
    except ImportError as e:
        logger.warning(f"Ollama service import failed: {e}")
        OllamaService = None
else:
    logger.info("Ollama server not accessible - skipping Ollama service import")
    OllamaService = None

try:
    from ..rag_service import RAGService
    RAG_AVAILABLE = True
    logger.info("RAG service imported successfully")
except ImportError as e:
    logger.warning(f"RAG service not available: {e}")
    RAGService = None

logger.info(f"Services available - Ollama: {OLLAMA_AVAILABLE}, RAG: {RAG_AVAILABLE}")