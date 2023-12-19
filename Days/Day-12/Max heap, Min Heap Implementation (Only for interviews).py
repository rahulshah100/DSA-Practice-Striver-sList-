# https://www.codingninjas.com/studio/problems/min-heap_4691801?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

# Implement the Min Heap data structure. You will be given 2 types of queries:-
# 0 X
# Insert X in the heap.
# 1
# Print the minimum element from the heap and remove it.

# Input Format: The first line will contain the integer 'T', denoting the number of test cases.
# For each test case, the first line will contain a single integer 'N', the number of queries.
# Then, each of the next ‘N’ lines contains two types of query either 0 ‘X’ or 1.

# Output format :
# For each test case, output the answer for query of type 1.

# Note: You don't need to print anything. It has already been taken care of. Just implement the given function.

# Constraints :
# 1 <= T <= 5
# 1 <= N <= 10^5
# 1 <= X <= 50
# Time Limit: 1 sec

# Sample Input 1 :
# 2
# 3
# 0 2
# 0 1
# 1
# 2
# 0 1
# 1

# Sample Output 1 :
# 1
# 1

# Explanation Of Sample Input 1 :
# For the first test case:- Insert 2 in the heap and currently, 2 is the smallest element in the heap. Insert 1 in the heap and now the smallest element is 1. Return and remove the smallest element which is 1.

# For the second test case:- Insert 1 in the heap and currently, 1 is the smallest element in the heap. Return the smallest element from the heap which is 1 and remove it.

# Sample Input 2:
# 2
# 5
# 0 5
# 1
# 0 43
# 0 15
# 0 5
# 2
# 0 4
# 1

# Sample Output 2 :
# 5
# 4
# ----------------------------------------------------------------------------------------------------------------------------------
# Bit Info on Heap Data Structure: In python, Heap data structure is an array itself just with its elements arranged in a certain order. Heap has 2 properties 1). It is a complete binary tree i.e. if we visualize an array as tree then it will be filled from top to bottom and in each level left to right. Therefor last level might not be completely filled if we fall short on items to form a tree but nowhere in between we'll have breakage of childNodes. 2) Heap follows either max or min Heap property. Meaning, parent is always bigger or smaller than it's childNodes, respectively. Now that won't matter if minHeap is like:
#        4                     or                       4
#     6     8                                        8     6
# i.e. right child necessarily doesn't have to be bigger or smaller than left one or vice versa. So if given array is [8,4,6,9] it's minHeap will be [4,6,8,9] or [4,8,6,9] both being valid ones. From [4,6,8,9] we can see left child of 6 i.e.node at index 1 is found at index 3 i.e. 2i+1. Similarly, for 8 it is right child of 4. 4 is present at 0 and 8 is at 2, so we can deduce 2i+2. These are equations to find left and right child of currentNode. If we observe for parent's index, we can see similar arrangement where (currIndex-1)//2 always gives index of currNode's parent Node.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: We'll make helper functions that return left child, right child and parent Node index. Further 2 operations have to be done Inserting an elem, and extracting the min item and storing it in array and further popping it from heap. 1). To insert item, we'll append it in heap array. Hereby as given is minHeap, if the appended item is smaller than it's parent then we swap them. Further if it's still smaller, we swap it with its parent. This goes on up-till the new item comes at the top i.e. index 0, and becomes root or if before that we find it to not be smaller than its parent. 2). For extractingMin we heapPop we return the value at root, in the Heap. Further, as it needs to go and the Heap would have to be re-heapified we approach this task by storing root item in a variable at first, and then overwriting this index with item present at last one in the Heap. We pop the last item now as it's been shifted to root. Further in re-heapifying this tree, we'll get the newly arranged heap after which we return the original root item that had been stored in a variable. To re-heapify, we take top-down approach where we identify the smallest item amongst parent, and it's first two child Nodes i.e. left and right Child. In case parent is not identified as smallest item, we swap it with the smallest amongst two (left, right) child. Further, this where parent shifts to is the index we compare with its first two child Nodes. This happens up-till either the node shift to last level and no child are left, or in between if parent is smaller than both child.
def leftChild(currNodeInd):
    return (2 * currNodeInd) + 1

def rightChild(currNodeInd):
    return (2 * currNodeInd) + 2

def parentNode(currNodeInd):
    return (currNodeInd - 1) // 2


def heapPush(heap, val):
    heap.append(val)
    i = len(heap) - 1
    while i > 0 and heap[parentNode(i)] > heap[i]:
        heap[parentNode(i)], heap[i] = heap[i], heap[parentNode(i)]
        i = parentNode(i)


def heapifyDown(heap, currInd):
    l = leftChild(currInd)
    r = rightChild(currInd)
    smallest = currInd
    if l < len(heap) and heap[l] < heap[currInd]:
        smallest = l
    if r < len(heap) and heap[r] < heap[smallest]:
        smallest = r
    if smallest != currInd:
        heap[currInd], heap[smallest] = heap[smallest], heap[currInd]
        heapifyDown(heap, smallest)

def heapPop(heap):
    minItem = heap[0]
    heap[0] = heap[len(heap) - 1]
    heap.pop()
    heapifyDown(heap, 0)  # Reshuffling Heap, post Min having been Extracted out
    return minItem


def minHeap(N: int, Q: [[]]) -> []:
    heap, ans = [], []
    for i in range(N):
        if Q[i][0] == 0:
            heapPush(heap, Q[i][1])
        else:
            ans.append(heapPop(heap))
    return ans


print(minHeap(5, [[0, 5], [1], [0, 43], [0, 15], [0, 5]]))
print(minHeap(3, [[0, 2], [0, 1], [1]]))
print(minHeap(2, [[0, 1], [1]]))
# TC: O(nlogn) given that n is number of queries. Explanation: we have n queries, each of which could either be push or extract/pop the top query. For push, after appending in array, that item in worst case would be smaller than all the level of parents and in worst case in logn time operation is completed. In extract the top, we shift last item of array to first and re-heapify the heap. In re-heapify, in worst case the shifted item can be bigger than all child and is shifted through all levels before it comes to last level and settles, this operation will take logn. So ultimately both operation takes logn and there being n such queries, TC is nlogn.
# SC: O(n) Explanation: Because only ans is required array, and heap array is considered occupying extra space and in worst case if there are n operation, all could be of inserting an item and ultimately making heap array of n size.

# ----------------------------------------------------------------------------------------------------------
# Other General notes: In python we have heapq library which could be imported in order to use inbuilt heapify and extract Min operations. Their implementation is as below. By default, it works for minHeap.
import heapq

def minHeap(N: int, Q: [[]]) -> []:
    heap, ans = [], []
    for i in range(N):
        if Q[i][0] == 0:
            heap.append(Q[i][1])
            heapq.heapify(heap) #Can convert the whole array in min heap just by running once taking O(n) time, unlike the above heapifyDown that had to be iteratively ran for each new item inserted. Proof of TC found at https://www.youtube.com/watch?v=MiyLo8adrWw&ab_channel=AlgorithmswithAttitude
            #heapq.heappush(heap, Q[i][1]) #instead of above two lines we could directly use this function. Takes O(logn) time
        else:
            minItem=heapq.heappop(heap)  #Takes O(logn) time
            ans.append(minItem)
    return ans


# To use maxHeap we can negate the values, as in make them negatives. Eg: for [5, 2, 10, 8]------------------------------------
max_heap = []

# Insert elements into the max-heap
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -8)

# To get the maximum element from the max-heap, negate the value
max_element = -max_heap[0] #This wont alter the heap
# OR
max_element = -heapq.heappop(max_heap) #Pop will alter the heap, removing the top item

# -----------------------------------------------------------------------------------------------------------------------------------
# Importance of Heap DataStructure: Using Heap is a better trade off than sorting in particular cases as below
# For finding min or max in an array, while sorting (merge sort) takes nlogn Time and O(n) Space; heapify() doesn't exactly sort but arranges elements in a minHeap fashion which could still give the max or min while taking only O(n) Time and O(n) Space. (meaning for minHeap we can have either 4,5,6 or 4,6,5 as our array and hence apart from top we cant trust it to give us sorted items)
# heappush and heappop only takes logn; so in a sorted array if only item has to be appended, with sorting we can append this item in array and sort it which wll still take nlogn time, heappush can be used with only logn time
# In cases where in an n=1000 sized array where we want only top 3 items, we can use heapify once which takes n time and heappop thrice to get top 3 items costing us 3logn more time yet better than sorting's time complexity which is nlogn.
# Thus, with dynamic data or a big data where only a couple of times we need to access the top items heap is better than sorting
# On contrary if we want to not dabble with an extra data structure, sorting the given array itself is more fruitful because with heap not only we have one more variable to handle, but to fetch entries out of it we have to keep doing heappush/heappop
