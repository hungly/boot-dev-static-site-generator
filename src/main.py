from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from splitnodes import split_nodes_image

def main():
    node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev.jpg) and ![to youtube](https://www.youtube.com/bootdotdev.png)", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    print(f"New nodes after splitting images: {new_nodes}")

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