def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = mergeSort(arr[:mid])
        R = mergeSort(arr[mid:])
    else:
        return arr
    l, u = 0, 0
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
        elif R[u] < L[l]:
            arr[i] = R[u]
            u += 1
    return arr


print(mergeSort([12, 11, 13, 5, 6, 7]))
# Recursion Tree for                                                                   12,11,13,17,5,6,7,9
#        lvl1                                     12,11,13,17                                                                    5,6,7,9
#        lvl2                            12,11                   13,17                                                        5,6        7,9
#        lvl3                        12       11              13       17                                                   5     6     7    9
# TC: O(nlogn). Explanation: Alright so how the flow works is that first only L calls will take place before recursion encounters the base case. That is because in code starting from top towards the down at first recursive call for L is wrote. However proceeding in that way for above example of 12,11,13,17,5,6,7,9 as we hit base of 12 we'll be returned to 12,11 with a value of 12 where now we make Right recursive on 12,11 and hit the base case of 11. So being returned 11, we'll be now at stage where our array is 12,11. At this point in the code we'll go to the next line from right recurion's call-line i.e. onto line after, and will merge only 2 elems i.e. 12,11. Further we'll head up to parent call where arr=12,11,13,17. Here we'll enter into right recursive call and get 13,17. In the current function a left recursion call happens that will fetch back 13 after which right recursion fetches us a 17. Again 2 elem i.e. 13 and 17 will be merged. As this happens we'll be back to having given array i.e. 12,11,13,17,5,6,7,9 as our current array and similar to this whole left part now we'll do for right half. With flow understood we can say a thing to notice is at any level of recursion total merge time is n i.e. for lvl2: 12,11 and 13,17 will merge usign n/2 time in total and so will 5,6 and 7,9 take totalling to n time at lvl2. There being logn such levels, nlogn time is consumed for merging. In addition to merging we have recursion calls taking extra time to form the whole recusive tree i.e. for all recursive calls to take place which will roughly be (nlogn/2). This is because n/2 recursive calls at worst on a level could be made (in this case lvl3) and there being logn such levels we get (nlogn/2). So totalling TC for diving and merging they're nlogn+(nlogn/2). Generalized as O(nlogn).
# Note: With recursion, the worst case TC just for doing the recursive calls can be found by visualizing the Recursion Tree and multiplying it's depth and width.
# SC: O(n) or O(n+logn). logn for stack space to store recursive calls and in worst case where length of L + R == original arr's length we use n space to store L and R collecitvely. n Dominating in equation we can say O(n) is SC although more appropriately O(n+logn) is SC
