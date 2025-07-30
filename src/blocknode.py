import re

from enum import Enum

class BlockType(Enum):
    """
    Enum for block types.
    """
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
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

def block_to_block_type(markdown_block: str) -> BlockType:
    """
    Determines the type of block based on the markdown content.

    :param markdown_block: The markdown block to analyze.
    :return: The BlockType of the block.
    """
    
    heading_pattern = r'^(#{1,6})\s'

    if re.match(heading_pattern, markdown_block):
        return BlockType.HEADING
    elif markdown_block.startswith('```') and markdown_block.endswith('```'):
        return BlockType.CODE
    elif is_quote_block(markdown_block):
        return BlockType.QUOTE
    elif is_unordered_list_block(markdown_block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list_block(markdown_block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def remove_block_markers(markdown_block: str, type: BlockType) -> str:
    """
    Removes block markers from a markdown block.

    :param markdown_block: The markdown block to process.
    :return: The markdown block without block markers.
    """
    
    if type == BlockType.HEADING:
        return re.sub(r'^(#{1,6})\s', '', markdown_block).strip()
    elif type == BlockType.CODE:
        return markdown_block.replace('```\n', '').replace('```', '')
    elif type == BlockType.QUOTE:
        return re.sub(r'^>', '', markdown_block, flags=re.MULTILINE).strip()
    elif type == BlockType.UNORDERED_LIST:
        return re.sub(r'^-\s', '', markdown_block, flags=re.MULTILINE).strip()
    elif type == BlockType.ORDERED_LIST:
        return re.sub(r'^\d+\.\s', '', markdown_block, flags=re.MULTILINE).strip()
    else:
        # For paragraphs, we just return the block as is
        # but we can also strip leading/trailing whitespace
        return markdown_block.replace('\n', ' ')
    
def is_quote_block(markdown_block):
    """
    Checks if a block is a quote block.

    :param markdown_block: The markdown block to check.
    :return: True if it is a quote block, False otherwise.
    """
    
    for line in markdown_block.split('\n'):
        if not line.startswith('>'):
            return False
    return True

def is_unordered_list_block(markdown_block):
    """
    Checks if a block is an unordered list block.

    :param markdown_block: The markdown block to check.
    :return: True if it is an unordered list block, False otherwise.
    """
    
    for line in markdown_block.split('\n'):
        if not re.match(r'^-\s.+', line):
            return False
    return True

def is_ordered_list_block(markdown_block):
    """
    Checks if a block is an ordered list block.

    :param markdown_block: The markdown block to check.
    :return: True if it is an ordered list block, False otherwise.
    """
    index = 1
    for line in markdown_block.split('\n'):
        if not re.match(r'^\d+\.\s.+', line) or not line.strip().startswith(f"{index}. "):
            return False
        index += 1
    return True
