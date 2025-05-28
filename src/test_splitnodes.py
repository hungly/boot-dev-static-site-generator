import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter

class TestSplitNods(unittest.TestCase):
    def test_simple_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[1].type, TextType.CODE)
        self.assertEqual(new_nodes[2].type, TextType.TEXT)

    def test_no_delimiter(self):
        node = TextNode("This is text without a delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is text without a delimiter")
        self.assertEqual(new_nodes[0].type, TextType.TEXT)

    def test_multiple_delimiters(self):
        node = TextNode("This `is` text with `multiple` code blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This ")
        self.assertEqual(new_nodes[1].text, "is")
        self.assertEqual(new_nodes[2].text, " text with ")
        self.assertEqual(new_nodes[3].text, "multiple")
        self.assertEqual(new_nodes[4].text, " code blocks")
        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[1].type, TextType.CODE)
        self.assertEqual(new_nodes[2].type, TextType.TEXT)
        self.assertEqual(new_nodes[3].type, TextType.CODE)
        self.assertEqual(new_nodes[4].type, TextType.TEXT)

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "")
        self.assertEqual(new_nodes[0].type, TextType.TEXT)

    def test_split_with_empty_text(self):
        node = TextNode("This is text with a `code block` and an empty part `", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text, " and an empty part ")
        self.assertEqual(new_nodes[0].type, TextType.TEXT)
        self.assertEqual(new_nodes[1].type, TextType.CODE)
        self.assertEqual(new_nodes[2].type, TextType.TEXT)

    def test_split_with_only_delimiters(self):
        node = TextNode("`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 0)