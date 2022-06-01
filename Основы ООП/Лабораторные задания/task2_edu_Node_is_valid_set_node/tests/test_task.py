import unittest

from task import Node


class TestCase(unittest.TestCase):
    def test_is_valid(self):
        node = Node(None)
        node.is_valid(None)
        node.is_valid(node)

        msg = "Метод is_valid должен возвращать ошибку TypeError, если тип проверяемого значения не None или Node"
        with self.assertRaises(TypeError, msg=msg):
            node.is_valid("invalid_type")
