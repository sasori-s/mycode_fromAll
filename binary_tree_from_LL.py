from collections import deque


class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def convertListToBinaryTree(head):
    if head is None:
        return None
    
    root = TreeNode(head.data)
    head = head.next
    
    q = deque()
    q.append(root)

    while head:
        front = q.popleft()
        front.left = TreeNode(head.data)
        q.append(front.left)

        head = head.next    

        if head:
            front.right = TreeNode(head.data)
            q.append(front.right)
            head = head.next
    
    return root


if __name__ == "__main__":
    head = None
    n = 6

    for i in reversed(range(1, n + 1)):
        head = ListNode(i, head)

    root = convertListToBinaryTree(head)
    preorder(root)