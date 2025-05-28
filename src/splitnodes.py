from textnode import TextNode, TextType

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
    