from turtle import pos


def search(arr, search_element):
    # defining index positions 
    left = 0 
    length = len(arr)
    right = length - 1
    position = -1

    # using a loop and two conditions to find the element from both left and right side to optimize search

    for left in range(0, right, 1):
        # If item is found from left side
        if(arr[left] == search_element):
            position = left
            print("Element found in Array at ", position + 1, " Position with ", left + 1, " Attempt and from left side")
            break
        
        if(arr[right] == search_element):
            # if item found from right side
            position = right
            print("Element found in Array at ", position+1, " Poistion with ", length - right, " Attempt and from right side")
            break

        left += 1
        right += 1

    # if element not found
    if(position == -1):
        print("Not found inn Array with ", left, " Attempt")



arr = [1, 2, 3, 4, 5]
search_element = 5
search(arr, search_element)