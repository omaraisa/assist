import logging
import uvicorn
from app.main import app


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
