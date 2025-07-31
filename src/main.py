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
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.type == TextType.IMAGE:
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
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

def list_item_wrapper(node: HTMLNode) -> HTMLNode:
    """
    Wrap a given HTMLNode in a list item.

    :param node: The HTMLNode to wrap.
    :return: An HTMLNode wrapped in a list item.
    """
    
    return ParentNode("li", [node]) if isinstance(node, LeafNode) else ParentNode("li", node.children)
    
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
            nodes.append(ParentNode("ul", [ParentNode('li', text_to_children(item)) for item in format_block.split("\n")]))
        elif block_type == BlockType.ORDERED_LIST:
            nodes.append(ParentNode("ol", [ParentNode('li', text_to_children(item)) for item in format_block.split("\n")]))
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
            
def extract_title(markdown: str) -> str:
    """
    Extract the title from a markdown string.

    :param markdown: The markdown string to extract the title from.
    :return: The extracted title.
    """
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled Document"

def generate_page(from_path, template_path, dest_path):
    """
    Generate a page from a markdown file using a template.

    :param from_path: Path to the markdown file.
    :param template_path: Path to the HTML template.
    :param dest_path: Destination path for the generated HTML file.
    """
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    
    md_content = open(from_path, "r").read()
    template_file = open(template_path, "r").read()
    html_content = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)
    file = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # print(f"=" * 45)
    # print(f"Template content:\n{html_content}")
    
    # print(f"=" * 45)
    # print(f"Generated HTML content:\n{file}")
    
    directory = dest_path.rsplit('/', 1)[0]
    if not exists(directory):
        makedirs(directory)
    with open(dest_path, "w") as f:
        f.write(file)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generate pages from markdown files in a directory.

    :param dir_path_content: Path to the directory containing markdown files.
    :param template_path: Path to the HTML template.
    :param dest_dir_path: Destination directory for the generated HTML files.
    """
    
    for item in listdir(dir_path_content):
        item_path = join(dir_path_content, item)
        if isfile(item_path) and item.endswith(".md"):
            dest_path = join(dest_dir_path, item.replace(".md", ".html"))
            generate_page(item_path, template_path, dest_path)
        elif not isfile(item_path):
            new_dest_dir = join(dest_dir_path, item)
            if not exists(new_dest_dir):
                makedirs(new_dest_dir)
            generate_pages_recursive(item_path, template_path, new_dest_dir)

def main():
    if exists("./public"):
        rmtree("./public")

    copy_files("./static", "./public")
    
    generate_pages_recursive("./content", "./template.html", "./public")

    pass

if __name__ == "__main__":
    main()