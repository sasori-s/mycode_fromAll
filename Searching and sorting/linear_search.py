from re import X


def search(arr, to_find, length):
    for i in arr:
        if(i == to_find):
            return arr.index(i)
    return -1

arr = [8, 10, 4, 50, 13]
to_find = 10
length = len(arr)

result = search(arr, to_find, length)
if(result == -1):
    print("The element is not present in the array")
else:
    print("The element is present in index", result)