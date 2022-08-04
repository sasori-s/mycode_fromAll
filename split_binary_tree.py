from lib2to3.pytree import Node
from tabnanny import check


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def size(root):
    return 1 + size(root.left) + size(root.right) if root else 0

def checkSize(root, n):
    if root is None:
        return False
    
    if 2 * size(root) == n:
        return True
    
    return checkSize(root.left, n) or checkSize(root.right, n)

def splitTree(root):
    n = size(root)

    return (n % 2 == 0) and checkSize(root, n)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    if splitTree(root):
        print('The binary tree can be split')
    else:
        print('The binary tree can not be split')