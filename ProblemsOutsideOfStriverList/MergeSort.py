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
# Time Complexity: O(nlogn), given that arr is represented as n. Explanation: Consider first getting an idea of logn time complexity by seeing BinarySearch.py which is in the same folder as this file. Seeing at the first step of our implementation, the array as we can see gets divided into being almost half. This will keep on being continued for each half i.e.they'll become n/2 then n/2/2 and so on. At each step log(n/2) then logn(n/2/2) time further division would happen before we have only one element array. So in total, in logn time, the entire given array would be broken down to being single item. Further down the implementation, we can see traversal happening through both halves for getting them merged. This traversal will happen at each level and will take corresponding n/2s time. We'd consider the worst traversal time which would happen at first step where L=n/2 and R=n/2; there, total n work would have to be done. Thsu we can say c1n (where c1 is a constant which'd be at max 1) work being done at each level, for merging and there being logn levels, we can write total work done as c1nlogn. Generalizing the worst c1 possible which would be 1 our time complexity = nlogn.
# Space Complexity: O(n). Explanation: At each step we'd have two new arrays created which are L and R which together would be taking n size for the first time, as such L at first would be n/2 and R would be n/2. In further steps the newly obtained L and R would always be smaller than n/2 as they're getting divided, and hence their total utilized space would be less than n as opposed to what it was in first step. However, as we're considering the worst case, which would be the first time the mergefunction runs and L and R are n/2 each, we in total use n/2+n/2=n space which makes our Space Complxity as O(n). Note: We are here not taking into account the stack space i.e. at L=n/8 we'll have total space used for that step as L=n/8 + R=n/8 i.e.in-total n/4, plus the L=n/4 space and L=n/2 space. In such case we'd have an additional logn space complexity, where still as O(n) dominates O(logn), the equation we mention for Space Complexity is O(n).
