class Node:
    def __init__(self, info, level):
        self.info = info
        self.left = None
        self.right = None
        self.level = level

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, info):
        level = 0
        if self.root is None:
            self.root = Node(info, level)
            return

        node = self.root
        while node:
            if node.info < info:
                if node.right is None:
                    level += 1
                    node.right = Node(info, level)
                    return
                node = node.right
            else:
                if node.left is None:
                    level += 1
                    node.left = Node(info, level)
                    return
                node = node.left
            level += 1


def height_subtree(root):
    if root.left is None and root.right is None:
        level = root.level
        return level
    if root.left:
        level = height_subtree(root.left)
    if root.right:
        level = height_subtree(root.right)
    return level


def height(root):
    current = root
    level = root.level
    subtree_right_level = 0
    subtree_left_level = 0

    if current.left:
        subtree_left_level = height_subtree(current.left)
    if current.right:
        subtree_right_level = height_subtree(current.right)
    return max(level, subtree_right_level, subtree_left_level)


if __name__ == "__main__":
    tree = BinarySearchTree()
    arr = [3, 2, 5, 6, 4, 1, 7]

    for i in arr:
        tree.create(i)

    print(height(tree.root))
