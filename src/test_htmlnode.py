import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", {"class": "container"})
        node2 = HTMLNode("div", "This is a div", {"class": "container"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_repr(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        expected_repr = "HTMLNode(div, This is a div, None, {'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

    def test_init(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a div")
        self.assertEqual(node.props, {"class": "container"})

    def test_props_to_html(self):
        node = LeafNode("div", "This is a div", {"class": "container"})
        expected_html = 'class="container"'
        self.assertEqual(node.props_to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()