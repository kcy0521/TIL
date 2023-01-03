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
        inorder(node.data)
        print(node.data, end=" ")
        inorder(node.right)


def posteroder(node):
    posteroder(node.left)
    posteroder(node.right)
    print(node.data, end=' ')

#
# preorade(root)
# print()
# inorder(root)
# print()
# posteroder()
# 13
# 1 2 1 3 2 4 ...

v = int(input())
# x = []
tree = [Node(i) for i in range(v + 1)]
edge_list = list(map(int, input().split()))
# 입력을 두개씩 잘라서 확인
# 앞 => 부모 p
# 뒤 => 자식 c
while edge_list:
    p = edge_list.pop(0) # 부모
    c = edge_list.pop(0) # 자식
    # 부모를 기준으로 왼쪽이 있는 경우
    if tree[p].left:
        tree[p].right = tree[c]
    # 부모를 기준으로 왼쪽이 없는 경우
    else:
        tree[p].left = tree[c]

    def preorder(node):
        if node:
            print(node.data, end=" ")
            preorder(node.left)
            preorder(node.right)
    # 전위순회 시작
preorder(tree[1])
print()


# for i in range(0, len(li), 2):
#     if li[i] not in x:
#         x.append(li[i])
#     print(x)
# 왼쪽이 없는 경우
# if tree[p].left:
#     왼쪽에 저장한다.
# if tree[p].right:
#     오른쪽에 저장한다.
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13