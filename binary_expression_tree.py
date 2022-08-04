class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isLeaf(node):
    return node.left is None and node.right is None

def process(op, x, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y


def evaluate(root):
    if root is None:
        return 0
    
    if isLeaf(root):
        return float(root.val)

    x = evaluate(root.left)
    y = evaluate(root.right)

    return process(root.val, x, y)


if __name__ == "__main__":
    root = Node('+')
    root.left = Node('*')
    root.right = Node('/')
    root.left.left = Node('-')
    root.left.right = Node('5')
    root.right.left = Node('21')
    root.right.right = Node('7')
    root.left.left.left = Node('10')
    root.left.left.right = Node('5')

    print('The value of the expression tree is ', evaluate(root))
