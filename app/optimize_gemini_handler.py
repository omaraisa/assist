"""
A script to optimize the Gemini handler in the AI response handler class.
This makes specific changes to the file to improve performance.
"""

import os
import re

def optimize_gemini_handler():
    """
    Apply performance optimizations to the Gemini handler in ai_response_handler.py
    """
    filepath = os.path.join('app', 'ai', 'ai_response_handler.py')
    
    # Make sure the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return False
    
    # Read the current file content
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Define the pattern to match the large JSON logging line
    log_pattern = r"logger\.info\(f\"Gemini conversation with function calls: \{json\.dumps\(contents, indent=2\)\}\"\)"
    
    # Replace with a more efficient version
    replacement = 'logger.debug(f"Gemini conversation prepared with {len(contents)} messages and {len(function_response_parts)} function responses")'
    
    # Perform the replacement
    new_content = re.sub(log_pattern, replacement, content)
    
    # Check if any replacement occurred
    if new_content == content:
        print("Warning: No replacements made. The log pattern might have changed.")
        return False
    
    # Write the optimized content back
    with open(filepath, 'w') as file:
        file.write(new_content)
    
    print(f"Successfully optimized Gemini handler in {filepath}")
    print("Changed excessive JSON logging to more efficient metrics reporting")
    
    return True

if __name__ == "__main__":
    optimize_gemini_handler()
