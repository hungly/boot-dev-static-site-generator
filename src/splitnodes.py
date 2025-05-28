from textnode import TextNode, TextType
from extractmarkkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter: str, text_type: TextType):
    """
    Split nodes by a delimiter and return a list of TextNode objects.

    :param old_nodes: List of TextNode objects to split.
    :param delimiter: The delimiter to split the text on.
    :param text_type: The type of the text nodes to create.
    :return: List of TextNode objects.
    """
    new_nodes = []

    for node in old_nodes:
        print("=" * 45)
        print(f"Splitting node:    {node}\nby delimiter:      {delimiter}\nof delimiter type: {text_type}")

        nodes = split_node(node, delimiter, node.type, text_type)

        print("=" * 45)
        print(f"Created {len(new_nodes)} new nodes")

        new_nodes.extend(nodes)

        print("=" * 45)
        print(f"Total nodes after split: {len(new_nodes)}")

    return new_nodes

def split_node(node: TextNode, delimiter: str, original_text_type: TextType, deli_text_type: TextType, is_delimiter: bool = False):
    """
    Split a single TextNode by a delimiter and return a list of TextNode objects.

    :param node: The TextNode to split.
    :param delimiter: The delimiter to split the text on.
    :param text_type: The type of the text nodes to create.
    :return: List of TextNode objects.
    """
    if not node.text:
        return [node]

    pos = node.text.find(delimiter)

    if not 0 <= pos < len(node.text):
        return [node]

    new_nodes = []

    left = node.text[:pos]
    right = node.text[pos + len(delimiter):]

    print("=" * 45)
    print(f"Left part:  '{left}'")
    print(f"Right part: '{right}'")
    
    if left:
        node = TextNode(left, node.type)
        new_nodes.append(node)
        print(f"Added left part: {node}")

    right_node = None

    if right:
        if is_delimiter:
            right_node = TextNode(right, original_text_type)
        else:
            right_node = TextNode(right, deli_text_type)
    else:
        return new_nodes

    print(f"Right part as new node: {right_node}")
    nodes = split_node(right_node, delimiter, original_text_type, deli_text_type, not is_delimiter)

    new_nodes.extend(nodes)

    return new_nodes
    
def split_nodes_link(old_nodes):
    """
    Split nodes by links and return a list of TextNode objects.
    :param old_nodes: List of TextNode objects to split.
    :return: List of TextNode objects.
    """
    new_nodes = []

    for node in old_nodes:
        text = node.text
        link_end_pos = 0

        links = extract_markdown_links(text)

        for link in links:
            link_end_pos = text.find(link[1]) + len(link[1])
            left_text = text[:text.find(link[0]) - 1]
            new_nodes.append(TextNode(left_text, node.type))
            new_nodes.append(TextNode(link[0], TextType.LINK, url=link[1]))
            text = text[link_end_pos + 1:]

    return new_nodes

def split_nodes_image(old_nodes):
    """
    Split nodes by images and return a list of TextNode objects.
    :param old_nodes: List of TextNode objects to split.
    :return: List of TextNode objects.
    """
    new_nodes = []

    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        for image in images:
            image_text = image[0]
            image_url = image[1]

            left_text = text[:text.find(image_text) - 2]
            if left_text:
                new_nodes.append(TextNode(left_text, node.type))

            new_nodes.append(TextNode(image_text, TextType.IMAGE, url=image_url))
            text = text[text.find(image_url) + len(image_url) + 1:]

        if text:
            new_nodes.append(TextNode(text, node.type))

    return new_nodes