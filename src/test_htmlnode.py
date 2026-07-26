import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None, None, None, None)
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("lmth", None, None, None)
        node2 = HTMLNode(None, None, None, None)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode(None, None, None, None)
        node2 = HTMLNode(None, None, None, {})
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = HTMLNode(None, None, None, {"a": "b"})
        node2 = HTMLNode(None, None, None, {"a": "b"})
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = HTMLNode(None, "lmth", None, None)
        node2 = HTMLNode(None, None, "lmth", None)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode(
            None,
            None,
            None,
            None
        )
        assert repr(node) == "HTMLNode(tag=None, value=None, children=None, props=None)"


if __name__ == "__main__":
    unittest.main()