import uvicorn
from app.main import app
import logging
import coloredlogs

if __name__ == "__main__":
    # Configure logging
    coloredlogs.install(
        level='INFO',
        fmt='%(asctime)s,%(msecs)03d %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s'
    )

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000
    )
