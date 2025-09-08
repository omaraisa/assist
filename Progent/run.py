import logging
import uvicorn
from app.main import app
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
    # Auto-reloading is now enabled. The _quiet_watchfiles() call will attempt
    # to silence the verbose logging from the watchfiles library.
    _quiet_watchfiles()

    # Get the app directory for the reloader. This ensures that changes to
    # files within the 'app' directory (like config.py) trigger a reload.
    app_dir = str(Path(__file__).parent / "app")

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=[app_dir],
        log_level="info",
    )
