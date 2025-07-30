from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from blocknode import BlockType, block_to_block_type, markdown_to_blocks, remove_block_markers
from splitnodes import text_to_textnodes
from shutil import rmtree, copy
from os.path import exists, join, isfile
from os import makedirs, listdir

def text_node_to_html_node(text_node: TextNode) -> HTMLNode: 
    """
    Convert a TextNode to an HTMLNode.

    :param text_node: The TextNode to convert.
    :return: An HTMLNode representing the TextNode.
    """
    if text_node.type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.link})
    elif text_node.type == TextType.IMAGE:
        return LeafNode("img", None, {"src": text_node.link, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown text type: {text_node.type}")
    
def text_to_children(text: str) -> list[HTMLNode]:
    """
    Convert a plain text string to a list of HTMLNode objects.

    :param text: The plain text string to convert.
    :return: List of HTMLNode objects.
    """
    
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in nodes]
    
def markdown_to_html_node(markdown: str) -> HTMLNode:
    """
    Convert a markdown string to an HTMLNode.

    :param markdown: The markdown string to convert.
    :return: An HTMLNode representing the markdown.
    """
    
    nodes = []

    for block in markdown_to_blocks(markdown):
        block_type = block_to_block_type(block)
        format_block = remove_block_markers(block, block_type)

        if block_type == BlockType.PARAGRAPH:
            nodes.append(ParentNode("p", text_to_children(format_block.replace("\n", " ").strip())))
        elif block_type == BlockType.HEADING:
            nodes.append(ParentNode("h1", text_to_children(format_block)))
        elif block_type == BlockType.CODE:
            nodes.append(LeafNode("pre", text_node_to_html_node(TextNode(format_block, TextType.CODE)).to_html()))
        elif block_type == BlockType.QUOTE:
            nodes.append(ParentNode("blockquote", text_to_children(format_block)))
        elif block_type == BlockType.UNORDERED_LIST:
            nodes.append(ParentNode("ul", text_to_children(format_block)))
        elif block_type == BlockType.ORDERED_LIST:
            nodes.append(ParentNode("ol", text_to_children(format_block)))
        else:
            raise ValueError(f"Unknown block type: {block_type}")

    return ParentNode("div", nodes)

def copy_files(src: str, dest: str):
    """
    Copy files from source to destination directory.

    :param src: Source directory.
    :param dest: Destination directory.
    """
    if not exists(dest):
        makedirs(dest)
    
    for item in listdir(src):
        s = join(src, item)
        d = join(dest, item)
        if isfile(s):
            copy(s, d)
        else:
            copy_files(s, d)

def main():
    if exists("./public"):
        rmtree("./public")

    copy_files("./static", "./public")

    pass

if __name__ == "__main__":
    main()