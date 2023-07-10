# Binary Search in python: To find an item in Sorted Array.
# Using Recursion:
def binarySearch(array, l, u, num):
    mid = (l + u) // 2
    if mid == l and array[mid] != num:
        return 'Elem not present'
    elif array[mid] == num:
        return mid
    elif array[mid] < num:
        return binarySearch(array, mid + 1, u, num) # +1 here is essential, the reason for which you can read down in below given approach
    elif array[mid] > num:
        return binarySearch(array, l, mid - 1, num)

# Driver Code
arr = [3, 4, 5, 6, 7, 8, 9]
x = 3
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
# TimeComplexity:O(logn). Explaination: Array keeps getting divided in half; when this is the scenario, in worst case we'll find elem at lognth attempt. For Eg: 8 items are there, for first time we'll divide array in 2 halves and say in the right half we go further due to elem'sValue>mid. In right half 4 values will be there, we divide them and have to go in further right half. In there, 2 elems are there. So we can still divide into two halves. Thus in total 3 iterations would be made which is= log8base2. BY default 2 is considered as base and so we can write above thing as log8. And this can be generalized as logn.
# SpaceComplexity:O(1); or O(logn) if we count stack space utilized because of recursive calls


# Using Iteration:
"""
import copy
from typing import List

class Solution:
    def binSort(self, array: List[int], num) -> List[int]:
        l, u = 0, len(array) - 1
        while l <= u:
            mid = (l + u) // 2
            if array[mid] == num:
                return mid
            elif num > array[mid]:
                l = mid + 1 # the +1 is of essence, coz 1)Essentially we've checked at m and item is not there 2)If the value is greater than greatest elem in arr then l will be 2nd last and u will be last elem eventually, and m using ceiling function it'll keep pointing towards smaller index amongst l and u i.e. l and again when elem is not there l will shift to where m has been pointing which is just where l already was
            else:
                u = mid
        return 'Not present'

S = Solution()
print(S.binSort([3, 4, 5, 6, 7, 8, 9], 7))
print(S.binSort([3, 4, 5, 6, 7, 8, 9], 11))
"""
# TC and SC same as above approach