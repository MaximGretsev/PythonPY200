import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)
        self.assertIsNone(node.next, msg="При инициализации значение по умолчанию следуюзего узла не None")

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        second_node = Node('second node')
        first_node = Node('first node', next_=second_node)

        expected_result = second_node
        actual_result = first_node.next
        self.assertIs(actual_result, expected_result, msg="Узлы не эквивалентны друг другу")

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node_value = 5
        node = Node(node_value)
        expected_result = f"Node({node_value}, None)"
        actual_result = repr(node)

        self.assertEqual(expected_result, actual_result, msg="Неврный вывод repr для ноды без следующего узла")

    @unittest.skip(reason="Не реализованный функционал")
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        expected_result = str(some_value)

        self.assertEqual(expected_result, str(node))
        self.assertEqual(expected_result, f"{node}")

    def test_is_valid(self):
        some_value = 5
        Node.is_valid(Node(some_value))
        Node.is_valid(None)

        with self.assertRaises(TypeError):
            invalid_node = "invalid_node"
            Node.is_valid(invalid_node)
