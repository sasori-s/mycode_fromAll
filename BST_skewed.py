def isSkewed(pre):
    n = len(pre)
    
    if n <= 2:
        return 1
    
    min_so_far = min(pre[n - 1], pre[n - 2])
    max_so_far = max(pre[n - 1], pre[n - 2])

    for i in reversed(range(0, n - 2)):
        if pre[i] < min_so_far:
            min_so_far = pre[i]
        elif pre[i] > max_so_far:
            max_so_far = pre[i]
        else:
            return 0

    return 1


if __name__ == "__main__":
    pre = [13, 30, 25, 18, 20]
    if isSkewed(pre):
        print('BST is skewed')
    else:
        print('BST is not skewed')