from lib2to3.pytree import Node
from xml.etree.ElementPath import find

from numpy import size


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findHeight(root, size=0):
    if root is None:
        return 0, size
    
    size += 1
    left, size = findHeight(root.left, size)
    right, size = findHeight(root.right, size)

    return 1 + max(left, right), size
        

def isSkewed(root):
    height, size = findHeight(root)
    return height == size

if __name__ == '__main__':
    root = Node(15)
    root.right = Node(30)
    root.right.left = Node(25)
    root.right.left.left = Node(18)
    root.right.left.left.right = Node(20)

    if isSkewed(root):
        print('Binary tree is skewed')
    else:
        print('Binary tree is not skewed')