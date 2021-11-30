from typing import Any, List, Callable
from lab4.TreeNode import TreeNode
import treelib as tr


class Tree:
    root: TreeNode

    def add(self, value: Any, parent_name: 'TreeNode') -> None:

        is_present: List[bool] = [False]

        def search_nodes(node: 'TreeNode') -> None:
            if node == parent_name:
                is_present[0] = True

        self.root.for_each_level_order(search_nodes)

        if is_present[0]:
            parent_name.add(value)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self) -> None:
        drz = tr.Tree()

        drz.create_node(str(self.root.value), str(self.root.value))

        def add_edge(node: 'TreeNode') -> None:
            for i in node.children:
                drz.create_node(str(i.value), str(i.value), parent=str(node.value))

        self.for_each_level_order(add_edge)
        drz.show()

    def __init__(self, value=None):
        self.root = TreeNode(value)

    def __len__(self):
        count: List[int] = [0]

        def counter() -> None:
            count[0] += 1

        self.for_each_level_order(counter)

        return counter
