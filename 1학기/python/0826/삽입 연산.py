class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#
#
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


def preorade(node):
    if node:
        print(node.data, end=' ')
        preorade(node.left)
        preorade(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def posteroder(node):
    posteroder(node.left)
    posteroder(node.right)
    print(node.data, end=' ')