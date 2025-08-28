import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# The path to the config.py file
CONFIG_FILE_PATH = Path(__file__).parent / "config.py"

def update_api_key_in_config(api_key_env_var: str, new_api_key: str) -> bool:
    """
    Updates a specific API key in the config.py file.

    Args:
        api_key_env_var (str): The name of the environment variable for the API key
                               (e.g., "GEMINI_API_KEY"). This must match the
                               variable name in config.py.
        new_api_key (str): The new API key to save.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    if not CONFIG_FILE_PATH.exists():
        logger.error(f"Config file not found at: {CONFIG_FILE_PATH}")
        return False

    try:
        content = CONFIG_FILE_PATH.read_text(encoding="utf-8")

        # Regex to find the API key assignment line.
        # It looks for a line starting with the key name, followed by an equals sign,
        # and captures the current value in quotes.
        # Example: GEMINI_API_KEY: str = "some_value"
        pattern = re.compile(rf'({api_key_env_var}\s*:\s*str\s*=\s*)".*?"')

        # The replacement string includes the matched group 1 (the variable name part)
        # and the new key in quotes.
        replacement = rf'\1"{new_api_key}"'

        # Perform the substitution
        new_content, num_replacements = pattern.subn(replacement, content)

        if num_replacements > 0:
            CONFIG_FILE_PATH.write_text(new_content, encoding="utf-8")
            logger.info(f"Successfully updated {api_key_env_var} in {CONFIG_FILE_PATH}")
            return True
        else:
            logger.error(f"Could not find the setting for {api_key_env_var} in {CONFIG_FILE_PATH}. No changes made.")
            return False

    except Exception as e:
        logger.error(f"Failed to update API key in config.py: {e}", exc_info=True)
        return False
