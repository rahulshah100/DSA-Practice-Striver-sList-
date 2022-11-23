def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

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

print(mergeSort([12, 11, 13, 5, 6, 7]))
# Time Complexity: O(nlogn) given that arr is represented as n. Explanation: Consider first getting an idea of logn time complexity by seeing BinarySearch.py which is in the same folder as this file. Seeing the first step of our implementation, the array as we can see gets divided into being almost half. This will keep on happening for each half i.e. they'll become n/2 then n/2/2 and so on. So in logn time, we will get our first single element that should be 12 in this case. Further for getting 11 we are not having to do entire logn traversal but just one or two more step from 12 i.e.logn+2 will give reach us to 11. Similarly for all the other elems too they all wont take O(logn). This time taken is therefore accurately not described as logn or nlogn but 2T(n/2) i.e.twice the time of it's half (this is a common practice to denote time complexity like this in algos which are using recursion). Further down the implementation, we can see traversal happening through both halves for getting them merged. This traversal will happen at each level and will take corresponding n elem's time. For Eg: at first level we have n elem array so merging will take O(n) time. Thus in total we can write time taken by algorithm is 2T(n/2)+O(n). By Master's theorem this is equated as O(nlogn).
# Space Complexity: O(n). Explanation: At each step we'd have two new arrays created which are L and R which together would be taking n size for the first time, as such L at first would be n/2 and R would be n/2. In further steps the newly obtained L and R would always be smaller than n/2 as they're getting divided, and hence their total utilized space would be less than n as opposed to what it was in first step. However, as we're considering the worst case, which would be the first time the mergefunction runs and L and R are n/2 each, we in total use n/2+n/2=n space which makes our Space Complxity as O(n). On top of this space, we have the stack space i.e. at L=n/8 we'll have total space used for that step as L=n/8 and all the functions above would be staying in memory too so that the functions could be traced to their call. That will add n space for n calls, as only in entire function call chain, only last function will be in execution and remaining all will be collapsed taking not much but O(1) space per level/functionCall. In such case we'd have an additional logn space complexity, where still as O(n) dominates O(logn), the equation we mention for Space Complexity is O(n).