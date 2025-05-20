class HTMLNode:
    """
    A class representing a node in an HTML document.
    """

    tag = None
    value = None
    children = None
    props = None

    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        """
        Initialize the HTMLNode with a tag, attributes, and text.

        :param tag: The HTML tag of the node.
        :param attributes: A dictionary of attributes for the node.
        :param text: The text content of the node.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self) -> str:
        """
        Convert the HTMLNode to an HTML string.

        :return: The HTML string representation of the node.
        """
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        """
        Convert the properties of the node to an HTML string.

        :return: The HTML string representation of the properties.
        """
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])