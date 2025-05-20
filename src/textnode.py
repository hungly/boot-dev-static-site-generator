from enum import Enum

class TextType(Enum):
    """
    Enum for text types.
    """
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    text = ""
    type = TextType.NORMAL
    url = ""

    def __init__(self, text: str, type: TextType = TextType.NORMAL, url: str = ""):
        """
        Initialize a TextNode with text, type, and optional URL.

        :param text: The text content of the node.
        :param type: The type of the text (e.g., normal, bold, italic, code, link, image).
        :param url: The URL for link or image types.
        """
        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, value):
        return self.text == value.text and self.type == value.type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"