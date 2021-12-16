from lab5.BinaryNode import BinaryNode


class BinarySearchTree:
    root: BinaryNode

    def insert(root, key):
        if root is None:
            return BinaryNode(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = insert(root.right, key)
            else:
                root.left = insert(root.left, key)
        return root