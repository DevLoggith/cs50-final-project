import re

def clean_job_description(text):
    """Helper function to clean scraped job descriptions"""
    text_lower = text.lower()
    # remove all punctuation that would not be used in a tech keyword
    remove_chars = re.sub(r'''[,;:'"()\[\]{}*|?!/\\]''', ' ', text_lower)
    # remove extra whitespaces and newlines, rejoin with a single space
    clean_text = " ".join(remove_chars.strip().split())

    return clean_text
