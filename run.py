import uvicorn
from app.main import app
from app.reduce_log import reduce_logging

if __name__ == "__main__":
    # Reduce logging level for better performance
    reduce_logging()
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
