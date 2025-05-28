import re

def extract_markdown_images(text: str):
    """
    Extracts markdown image links from a given text.

    :param text: The input text containing markdown image links.
    :return: A tuple containing the extracted image links and the modified text with images replaced by placeholders.
    """

    # Regular expression to match markdown image syntax
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    # Find all matches
    matches = re.findall(pattern, text)
    
    return matches

def extract_markdown_links(text: str):
    """
    Extracts markdown links from a given text.

    :param text: The input text containing markdown links.
    :return: A tuple containing the extracted links and the modified text with links replaced by placeholders.
    """

    # Regular expression to match markdown link syntax
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    # Find all matches
    matches = re.findall(pattern, text)
    
    return matches