from typing import Any, List, Callable, Union
from project1 import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def is_leaf(self) -> bool:  # is this node a leaf (has no children)
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:  # add a new child
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:  # go through deep first
        visit(self)

        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:  # go through by level order
        visit(self)
        queue: 'Queue' = Queue()

        for i in self.children:
            queue.enqueue(i)

        while len(queue) != 0:
            x = queue.dequeue()
            visit(x)
            for i in x.children:
                queue.enqueue(i)

    def search(self, value: Any) -> Union['TreeNode', None]:  # look for given value
        result: List[TreeNode] = []

        def search_foo(node: 'TreeNode'):
            if node.value == value:
                result.append(node)

        self.for_each_level_order(search_foo)

        if len(result) == 0:
            return None
        else:
            return result[0]

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)
