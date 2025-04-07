from keywords import keywords_set
import re
from typing import Any, List, Dict


def find_keywords(keywords, description):
    """Helper function to parse each description for keywords"""
    keywords_present = set()

    for keyword in keywords:
        # escapes special characters in keywords like 'c#' & '.net"
        escaped_keyword = re.escape(keyword)
        # targets any whitespace or specified punctuation at word boundaries
        pattern = fr'(?:^|[\s.]){escaped_keyword}(?:$|[\s.])'

        if re.search(pattern, description):
            keywords_present.add(keyword)

    return keywords_present

def extract_total_keywords(jobs_list: List[Dict[str, List[Dict[str, Any]]]]) -> Dict:
    total_keywords = {}
    for job in jobs_list[0]["descriptions"]:
        found_keywords = find_keywords(keywords_set, job["description"])
        for keyword in found_keywords:
            total_keywords[keyword] = total_keywords.get(keyword, 0) + 1

    return total_keywords
