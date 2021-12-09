from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    # noinspection PyTypeChecker
    def __init__(self, value) -> None:  # types are fine, outputs error
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_left_child(self, value: Any) -> None:  # add a child on left
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:  # add a child on roght
        self.right_child = BinaryNode(value)

    def is_leaf(self) -> bool:  # leaf == no children/last node
        if self.right_child is None and self.left_child is None:
            return True  # no children on either side == is leaf
        else:
            return False  # a child somewhere == not leaf

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:  # bottom left through parents to bottom right
        if self.left_child is not None:  # if there is a left child start at child
            self.left_child.traverse_in_order(visit)
        visit(self)  # no more left children = visit current
        if self.right_child is not None:  # if there is a right child start at child
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:  # by side and by level/bottom left to top
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)  # visit if no more unvisited children

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:  # from top by left to bottom right
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):  # show value
        return str(self.value)
