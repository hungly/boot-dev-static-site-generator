from textnode import TextNode, TextType

def main():
    node = TextNode("Hello, World!", TextType.BOLD, "http://example.com")
    print(node)
    pass

if __name__ == "__main__":
    main()
