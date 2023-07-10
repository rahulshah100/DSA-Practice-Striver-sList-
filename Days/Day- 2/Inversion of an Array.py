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


# Approach2: Decreased Time Complexity at the cost of increased space complexity. Using merge sort, we'll calculate the inversion we have to make while merging the elements.
from os import *
from sys import *
from collections import *
from math import *

myInversion = []

def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = merge(arr[:mid])
        R = merge(arr[mid:])
    else:
        return arr
    l = u = inv_count = 0
    for i in range(len(arr)):
        if l < len(L) and u >= len(R):
            arr[i] = L[l]
            l += 1
        elif l >= len(L) and u < len(R):
            arr[i] = R[u]
            u += 1
        elif L[l] <= R[u]:
            arr[i] = L[l]
            l += 1
        elif L[l] > R[u]:  # Remember only while having to swap elems we've to increment count of inverstions. Hence above arent the cases
            arr[i] = R[u]
            u += 1
            inv_count += len(L) - l  # We cant just do +=1, because if elem at l index in L array is bigger than R[u] then certainly all elem in L (as L is sorted) after l would be bigger too than R[u] and would be needed to be swapped. If we dont do it here, then after this iteration u is increased we wont be ever able to compare indexes from l onwards in L with R[u]
    myInversion.append(inv_count)  # Append inv_count to myInversion
    return arr


def getInversions(arr, n):
    merge(arr)
    return sum(myInversion)


# Taking input using fast I/O.
def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# Main.
arr, n = takeInput()
print(getInversions(arr, n))
# Time Complexity: O(nlogn+n). Explanation: nlogn from what merge sort takes + n from what sum should take in myInversion Array.
# Space Complexity: O(2n). Explanation: n space is what merge sort takes to temporarily hold the L i.e. Left and R i.e. Right Array. More n space for storing count of inversions in myInversion Array


# Approach 3: Better TC and SC then Approach2 - In Approach 2 instead of using a global variable as myInversion, making it a part of recursive function call itself to return and summarize all the Inversions.
from os import *
from sys import *
from collections import *
from math import *


def merge(arr):
    inv_ct = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L, left_inversion_ct = merge(arr[:mid])
        R, right_inversion_ct = merge(arr[mid:])
        inv_ct += left_inversion_ct + right_inversion_ct
    else:
        return arr, 0
    l = u = 0
    for i in range(len(arr)):
        if l < len(L) and u >= len(R):
            arr[i] = L[l]
            l += 1
        elif l >= len(L) and u < len(R):
            arr[i] = R[u]
            u += 1
        elif L[l] <= R[u]:
            arr[i] = L[l]
            l += 1
        elif L[l] > R[u]:
            arr[i] = R[u]
            u += 1
            inv_ct += len(L) - l  # We cant just do +=1, because if elem at l index in L array is bigger than R[u] then certainly all elem in L (as L is sorted) after l would be bigger too than R[u] and would be needed to be swapped. If we dont do it here, then after this iteration u is increased we wont be ever able to compare indexes from l onwards in L with R[u]
    return arr, inv_ct


def getInversions(arr, n):
    arr, inv_ct = merge(arr)
    return inv_ct


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
