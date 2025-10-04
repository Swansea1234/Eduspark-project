# utils.py
import re

def get_valid_filename(s):
    """
    Strips invalid characters from a string to create a valid filename.
    Returns a cleaned string.
    """
    s = str(s).strip().replace(' ', '_')
    # Use a regex to remove characters that aren't letters, numbers, hyphens, or dots
    return re.sub(r'(?u)[^-\w.]', '', s)