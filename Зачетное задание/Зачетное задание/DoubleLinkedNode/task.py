from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.is_valid(next_node)
        self.__next = next_node

    @classmethod
    def is_valid(cls, node):
        if not isinstance(node, (cls, type(None))):
            raise TypeError("Не правильный тип ноды")

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)


class DoubleLinkedNode(Node):
    def __init__(self, value, next_=None, prev=None):
        super().__init__(value, next_)
        self._prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = value

    def __repr__(self):
        next_repr: str = str(None) if self.next is None else f'DoubleLinkedNode({self.next.value}, {None}, {None})'
        prev_repr: str = str(None) if self._prev is None else f'DoubleLinkedNode({self._prev.value}, {None}, {None})'
        return f'DoubleLinkedNode({self.value}, {next_repr}, {prev_repr})'

    @classmethod
    def is_valid(cls, prev_node: Any) -> None:
        if not isinstance(prev_node, (type(None), cls)):
            raise TypeError("У ноды неверный тип данных")


if __name__ == "__main__":
    ...
