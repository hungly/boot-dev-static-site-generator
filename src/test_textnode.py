import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        expected_repr = "TextNode(This is a text node, bold, http://example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_init(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.type, TextType.BOLD)
        self.assertEqual(node.url, "http://example.com")

    def test_eq_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_eq_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()