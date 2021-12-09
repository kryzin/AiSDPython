def show(self) -> None:  # left is above right
    t = binarytree.tree()  # implement in imported library
    t = binarytree.Node(self.root.value)

    def add(node: 'BinaryNode') -> None:  # function to input children of current node
        if node.right_child is not None:
            t.right = binarytree.Node(node.right_child.value)
        if node.left_child is not None:
            t.left = binarytree.Node(node.left_child.value)

    self.traverse_pre_order(add)  # input children of all nodes
    print(t)