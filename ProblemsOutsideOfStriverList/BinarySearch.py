# Binary Search in python: To find an item in sorted array.
def binarySearch(array, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        # If found at mid, then return it
        if array[mid] == x:
            return mid
        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, low, mid-1, x) #mid is already checked so we'll not include that in the further array partitions.
            # Here return is important as otherwise suppose we have 4 inner levels of recursive function calls and the fourth function is returning mid or -1 now that would be received to function 3, but that'd be about it. We'd want to further make a return from 3rd to 2nd and 2nd to 1st, from where ultimately we'll exit out of the function and the result variable in the driver code will receive the final value
        # Search the right half
        else:
            return binarySearch(array, mid+1, high, x)
    else:
        return -1


# Driver Code
arr = [3, 4, 5, 6, 7, 8, 9]
x = 3
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
# TimeComplexity:O(logn). Explaination: Array keeps getting divided in half; when this is the scenario, in worst case we'll find elem at lognth attempt. For Eg: 8 items are there, for first time we'll divide array in 2 halves and say in the right half we go further due to elem'sValue>mid. In right half 4 values will be there, we divide them and have to go in further right half. In there, 2 elems are there. So we can still divide into two halves. Thus in total 3 iterations would be made which is= log8base2. BY default 2 is considered as base and so we can write above thing as log8. And this can be generalized as logn.
# SpaceComplexity:O(1)
