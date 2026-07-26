from textnode import TextNode, TextType
from htmlnode import HTMLNode



def main():
    t = TextNode("teext", TextType.BOLD, None)
    h = HTMLNode(None, None, None, None)
    print(h)
    print(t)





if __name__ == "__main__":
    main()