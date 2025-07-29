def markdown_to_blocks(markdown):
    """
    Converts markdown text into a list of blocks, extracting images and links.

    :param markdown: The input markdown text.
    :return: A list of blocks containing the extracted images and links.
    """
    
    # Create blocks for images and links
    blocks = []
    
    for paragraph in markdown.split('\n\n'):
        p = paragraph.strip()
        if p != "":
            blocks.append(p)

    return blocks