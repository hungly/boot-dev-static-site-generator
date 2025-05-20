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
    
class LeafNode(HTMLNode):
        """
        A class representing a leaf node in an HTML document.
        """

        def __init__(self, tag: str, value: str, props: dict = None):
            super().__init__(tag, value, None, props)

        def to_html(self) -> str:
            """
            Convert the LeafNode to an HTML string.

            :return: The HTML string representation of the node.
            """
            if self.value is None:
                raise ValueError("LeafNode must have a value")
            elif self.tag is None:
                return self.value
            else:
                props_str = self.props_to_html()
                if props_str:
                    return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
                else:
                    return f"<{self.tag}>{self.value}</{self.tag}>"
                
class ParentNode(HTMLNode):
    """
    A class representing a parent node in an HTML document.
    """

    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        """
        Convert the ParentNode to an HTML string.

        :return: The HTML string representation of the node.
        """
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        elif self.children is None:
            raise ValueError("ParentNode must have children")
        else:
            props_str = self.props_to_html()
            children_str = "".join([child.to_html() for child in self.children])
            if props_str:
                return f"<{self.tag} {props_str}>{children_str}</{self.tag}>"
            else:
                return f"<{self.tag}>{children_str}</{self.tag}>"