from typing import Any, Callable, Optional
from projekt2.BinaryNode import BinaryNode
import treelib


class BinaryTree:
    root: BinaryNode

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self) -> None:  # left is above right
        t = treelib.Tree()  # implement in imported library
        t.create_node(str(self.root.value), str(self.root.value))  # input tree root into Tree class

        def add(node: 'BinaryNode') -> None:  # function to input children of current node
            if node.right_child is not None:
                t.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))
            if node.left_child is not None:
                t.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))

        self.traverse_pre_order(add)  # input children of all nodes
        t.show()

    def __init__(self, value: Optional = None, root: BinaryNode = None) -> None:
        if root is None:
            self.root = BinaryNode(value)
        else:
            self.root = root


def left_line(tree: BinaryTree):  # praca domowa output only left line
    lista = []
    current = tree.root
    while current is not None:
        lista.append(current.value)
        current = current.left_child
    return lista


# tree = BinaryTree(10)
# assert tree.root.value == 10
#
# tree.root.add_right_child(2)
# tree.root.right_child.add_right_child(3)
# assert tree.root.right_child.value == 2
# assert tree.root.right_child.is_leaf() is False
#
# tree.root.add_left_child(13)
# tree.root.left_child.add_left_child(1)
# assert tree.root.left_child.left_child.value == 1
# assert tree.root.left_child.left_child.is_leaf() is True

tree = BinaryTree(1)
tree.root.add_left_child(2)
tree.root.add_right_child(3)
tree.root.left_child.add_left_child(4)
tree.root.left_child.add_right_child(5)
tree.root.right_child.add_right_child(7)
tree.root.left_child.left_child.add_left_child(8)
tree.root.left_child.left_child.add_right_child(9)

tree.show()
print(left_line(tree))

