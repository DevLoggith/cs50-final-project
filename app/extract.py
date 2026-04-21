from keywords import keywords_set
import re


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

def extract_total_keywords(descriptions_list):
    total_keywords = {}
    if not descriptions_list:
        return {}
    else:
        for description in descriptions_list:
            found_keywords = find_keywords(keywords_set, description)
            for keyword in found_keywords:
                total_keywords[keyword] = total_keywords.get(keyword, 0) + 1

        return total_keywords
