# https://www.geeksforgeeks.org/counting-inversions/
# Count Inversions in an array | Set 1 (Using Merge Sort)

# Inversion Count for an array indicates – how far (or close) the array is from being sorted. If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order, the inversion count is the maximum.
# Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

# Example:
# Input: arr[] = {8, 4, 2, 1}
# Output: 6
# Explanation: Given array has six inversions:
# (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

# Example:
# Input: arr[] = {3, 1, 2}
# Output: 2
# Explanation: Given array has two inversions:
# (3, 1), (3, 2)
# -------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Brute Force: for each array item i, traverse to all its right items and keep increasing the swapCount if number on right is found smaller than ith number.
def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
    return inv_count


# Driver Code
# arr = [1, 20, 6, 4, 5]
arr = [52244275, 123047899, 493394237, 922363607, 378906890, 188674257, 222477309, 902683641, 860884025, 339100162]
# arr=[36343342,658445766,281323766,703538013,437455363,900766801,84401391,159903601,626186515,127519304,222484765,609828661,190927389,152625748,358752776,522920848,494568773,977351598,782415711,966011559]
n = len(arr)
print(getInvCount(arr, n))
# Time Complexity: O(n(n+1))/2
# Space Complexity: O(1)


# Approach2: Decreased Time Complexity at the cost of increased space complexity. Using a global variable we'll keep count of appropriate inversions taking place in merge sort
from os import *
from sys import *
from collections import *
from math import *

invCt = 0

def merge(arr):
    if len(arr) > 1:
        global invCt    #For accessing a global variable inside the function we declare that same variable with a global keyword in that function.
        mid = len(arr) // 2 #For altering the global variable in function we have to define it as global whereas for just reading global variable we're not required to
        L = merge(arr[:mid]) #The above comment holds because as we try to alter the variable inside a function it's (function's) local variables are what is checked and altered
        R = merge(arr[mid:]) #Which in this case as we dont have any we'll get an error of undefined variable
        i = j = ct = 0      #Thus here we used global keyword but not at #--1 while returning it from inside a different function
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[ct] = L[i]
                i += 1
            else:
                arr[ct] = R[j]
                invCt += len(L) - i
                j += 1
            ct += 1
        while i < len(L):
            arr[ct] = L[i]
            i += 1
            ct += 1
        while j < len(R):
            arr[ct] = R[j]
            j += 1
            ct += 1
        return arr
    else:
        return arr


def getInversions(arr, n):
    merge(arr)
    return invCt #--1


# Taking input using fast I/O.
def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# Main.
arr, n = takeInput()
print(getInversions(arr, n))
# Time Complexity: O(nlogn). Explanation: nlogn from what merge sort takes
# Space Complexity: O(n). Explanation: n space is what merge sort takes to temporarily hold the L i.e. Left and R i.e. Right Array.


# Approach 3: In Approach 2 instead of using a global variable as invCt, making it a part of recursive function call itself
from os import *
from sys import *
from collections import *
from math import *

def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, invCt1 = merge(arr[:mid]) #So by default if you return more than 1 item python makes it a tuple and send.
        R, invCt2 = merge(arr[mid:]) #Now to access all items of tuples we're using equal variables and assigning to tuple.
        i = j = ct = 0               #This is called tuple unpacking
        invCt = invCt1 + invCt2
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[ct] = L[i]
                i += 1
            else:
                arr[ct] = R[j]
                invCt += len(L) - i
                j += 1
            ct += 1
        while i < len(L):
            arr[ct] = L[i]
            i += 1
            ct += 1
        while j < len(R):
            arr[ct] = R[j]
            j += 1
            ct += 1
        return arr, invCt   #Sent as a tuple of 2 items
    else:
        return arr, 0


def getInversions(arr, n):
    sortedArr, invCt = merge(arr)
    return invCt


# Taking input using fast I/O.
def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# Main.
arr, n = takeInput()
print(getInversions(arr, n))
# TC: O(nlogn)
# SC: O(n)
