import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_differentProps(self):
        node3 = TextNode("This is third text node", TextType.BOLD)
        node4 = TextNode("This is third text node", TextType.ITALIC)
        self.assertNotEqual(node3, node4)

    def test_none_url(self):
        node = TextNode("This is a textnode without url", TextType.ITALIC)
        self.assertIsInstance(node, TextNode)

 
    

if __name__ == "__main__":
    unittest.main()