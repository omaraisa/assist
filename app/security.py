import re

def sanitize_output(text: str) -> str:
    """
    Sanitizes the output to prevent leaking sensitive information.
    """
    # Redact file paths (e.g., /path/to/file, C:\\path\\to\\file)
    text = re.sub(r'([a-zA-Z]:\\[\\\S|*\S]?\S*)|(/[a-zA-Z0-9_.-]+)+/?', '[REDACTED FILE PATH]', text)

    # Redact API keys (common patterns)
    text = re.sub(r'(sk-[a-zA-Z0-9]{20,})', '[REDACTED API KEY]', text)
    text = re.sub(r'(AIza[a-zA-Z0-9_-]{35})', '[REDACTED API KEY]', text)

    # A simple check for source code. This is not foolproof and might have false positives.
    # It looks for common programming keywords.
    code_keywords = ['def ', 'class ', 'import ', 'from ', 'async def ']
    if any(keyword in text for keyword in code_keywords):
        # A more sophisticated approach would be to use a parser,
        # but for now, we will just redact the whole message if it looks like code.
        # This is a trade-off between security and functionality.
        # A better approach would be to allow code, but only in a sandboxed environment.
        # For now, we will be strict.
        if len(text.splitlines()) > 3: # If it has more than 3 lines and contains keywords, redact it.
            return "[REDACTED SOURCE CODE]"

    return text
