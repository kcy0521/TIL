class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.data)
        print(node.data, end=" ")
        inorder(node.right)


def posteroder(node):
    posteroder(node.left)
    posteroder(node.right)
    print(node.data, end=' ')

root = Node("+")
root.left = Node("*")
root.right = Node("E")
root.left.left = Node("*")
root.left.right = Node("D")
root.left.left.left = Node("/")
root.left.left.right = Node("C")
root.left.left.left.left = Node("A")
root.left.left.left.right = Node("B")

preorder(root)
print()
posteroder(root)
print()
inorder(root)
