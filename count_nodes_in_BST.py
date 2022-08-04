#BST Node
from itertools import count


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Recursive function to insert a given key into BST
def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    
    else:
        root.right = insert(root.right, key)
    return root

#function to count nodes in a BST that lie within a given range
def countNodes(root, low, high):
    if root is None:
        return 0
    
    count = 0
    
    if low <= root.data <= high:
        count += 1
        
    count += countNodes(root.left, low, high)

    return count + countNodes(root.right, low, high) 
    


if __name__ == "__main__":
    #input range
    low, high = 12, 20
    keys = [15, 25, 20, 22, 30, 18, 10, 8, 9, 12, 6]

    #construct BST from above keys
    root = None
    for key in keys:
        root = insert(root, key)

    print('Total number of node is ', countNodes(root, low, high))