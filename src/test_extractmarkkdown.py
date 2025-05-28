import unittest

from extractmarkkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 2)
        self.assertEqual(images[0], ("rick roll", "https://i.imgur.com/aKaOqIh.gif"))
        self.assertEqual(images[1], ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"))

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0], ("to boot dev", "https://www.boot.dev"))
        self.assertEqual(links[1], ("to youtube", "https://www.youtube.com/@bootdotdev"))

    def test_no_markdown_images(self):
        text = "This is text without any images."
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_no_markdown_links(self):  
        text = "This is text without any links."
        links = extract_markdown_links(text)
        self.assertEqual(links, [])