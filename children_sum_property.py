# A class to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#Function to check if a given binary tee holds children-sum property
def hashChildrenSumProperty(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return root.data
    
    left = hashChildrenSumProperty(root.left)
    right = hashChildrenSumProperty(root.right)

    if left != -float('inf') and right != -float('inf') and root.data == left + right:
        return root.data

    return -float('inf')    



if __name__ == "__main__":
    root = Node(25)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(7)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)