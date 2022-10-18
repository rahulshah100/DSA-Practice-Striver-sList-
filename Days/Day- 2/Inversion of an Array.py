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
arr=[52244275,123047899,493394237,922363607,378906890,188674257,222477309,902683641,860884025,339100162]
# arr=[36343342,658445766,281323766,703538013,437455363,900766801,84401391,159903601,626186515,127519304,222484765,609828661,190927389,152625748,358752776,522920848,494568773,977351598,782415711,966011559]
n = len(arr)
print(getInvCount(arr, n))

# Time Complexity: O(n(n+1))/2
# Space Complexity: O(1)

# Approach2 (Implementation Not Working): Decreased Time Complexity at the cost of increased space complexity. Using merge sort, we'll calculate the inversion we have to make while merging the elements.
myInversion=[]

def getInvCount(Givenarr, n):
    mergeSort(Givenarr)
    return sum(myInversion)

def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        InversionCount=0

        # Sorting the first and the second half
        L=mergeSort(L)
        R=mergeSort(R)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                InversionCount = len(L)-i
                myInversion.append(InversionCount)
            k += 1

        # Checking and appending to main array if any element was left in either left or right array.
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr
    else:
        return arr


# Driver Code
# arr = [8, 2, 1, 4]
# arr = [52244275,123047899,493394237,922363607,378906890,188674257,222477309,902683641,860884025,339100162] #0 3 2 0 0
# arr=[36343342,658445766,281323766,703538013,437455363,900766801,84401391,159903601,626186515,127519304,222484765,609828661,190927389,152625748,358752776,522920848,494568773,977351598,782415711,966011559]
arr=[289837621,687176338,941575810,783231857,462056296,172999051,971906113,684533604,75682691,685306490,23633765,964542384,343752255,157473882,520596748,781207617,58240683,604998138,941111217,536943549,585033793,16112334,146772209,628477534,168738081,358041337,3914733,663306853,335392934,786330443]
n = len(arr)
print(getInvCount(arr, n))
# Time Complexity: O(nlogn+n). Explanation: nlogm from what merge sort takes + n from what sum should take in myInversion Array.
# Space Complexity: O(n). Explanation: That's what merge sort takes.
