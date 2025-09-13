import logging
import uvicorn
from app.main import app
from clean_logs import clean_old_logs
from pathlib import Path


def _quiet_watchfiles():
    """Lower the verbosity of the watchfiles logger (used by uvicorn reload).

    This prevents repeated lines like:
    "2025-08-18 23:18:00,223 INFO watchfiles.main 1 change detected"
    when the reloader is active.
    """
    try:
        logging.getLogger("watchfiles").setLevel(logging.WARNING)
    except Exception:
        # If watchfiles isn't present or can't be configured, ignore.
        pass


if __name__ == "__main__":
    # Clean old log entries before starting
    log_file_path = Path(__file__).parent.parent / "logs" / "system.log"
    clean_old_logs(log_file_path, days=3)

    # Disable the auto-reloader which uses watchfiles (causes repeated INFO logs)
    # If you need auto-reload during development, set reload=True but be aware
    # of the watchfiles INFO messages; in that case the _quiet_watchfiles() call
    # will attempt to silence the logger.
    _quiet_watchfiles()

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=6060,
        reload=False,
        log_level="info",
    )
