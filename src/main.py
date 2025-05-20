from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = TextNode("Hello, World!", TextType.BOLD, "http://example.com")
    print(node)
    pass

if __name__ == "__main__":
    main()

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