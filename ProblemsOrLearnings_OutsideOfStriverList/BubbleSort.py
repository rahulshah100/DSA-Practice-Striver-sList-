# Brute Force approach for Sorting: where 2 for loops are used and each item is compared to all the items to determine where does it sort

def BubbleSort(arr1):
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[j]<arr1[i]:
                arr1[i], arr1[j] = arr1[j], arr1[i]
    print(arr1)

BubbleSort([1,312,1,2,12,0,-323,14])
# TC: O(n^2)
# SC: O(1)