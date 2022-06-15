from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    # TODO Сделать методом класса и унаследовать.
    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):  # TODO Node = DoubleNde. Их можно унаследовать.
        self.is_valid(next_)
        self._next = next_


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

    def is_valid(self, prev_node: Any) -> None:
        if not isinstance(prev_node, (type(None), DoubleLinkedNode)):
            raise TypeError
    # TODO __repr__ надо будет перегрузить, чтобы он показывал  PrevNode
    # TODO __str__ не перегружаем, его надо наследовать?
    # TODO is_valid перегрузить, чтобы использовалась PrevNode
    # TODO сделать prev по методу и подобию next_


if __name__ == '__main__':
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)

    # first_node = Node(1)  # отработал setter в init
    # second_node = Node(2)  # отработал setter в init
    # one_more_node = Node(3)
    # first_node.next = second_node
    # second_node.next = one_more_node
    # print(repr(first_node), repr(first_node.next), repr(second_node.next))
    #
    # third_node = DoubleLinkedNode(1)
    #
    # fourth_node = DoubleLinkedNode(2)
    # fourth_node.prev = third_node
    #
    # five_node = DoubleLinkedNode(3)
    # five_node.prev = fourth_node
    #
    # print(repr(five_node))
    # print(repr(fourth_node.prev))
    # print(repr(five_node.prev))
