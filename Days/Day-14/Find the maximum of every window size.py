# https://www.codingninjas.com/studio/problems/max-of-min_982935?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

# Maximum of minimum for every window size:

# You are given an array of ‘N’ integers, you need to find the maximum of minimum for every window size. The size of the window should vary from 1 to ‘N’ only.

# For example:
# ARR = [1,2,3,4]
# Minimums of window size 1 = min(1), min(2), min(3), min(4) = 1,2,3,4
# Maximum among (1,2,3,4)  is 4

# Minimums of window size 2 = min(1,2), min(2,3),   min(3,4) = 1,2,3
# Maximum among (1,2,3) is 3

# Minimums of window size 3 = min(1,2,3), min(2,3,4) = 1,2
# Maximum among (1,2) is 2

# Minimums of window size 4 = min(1,2,3,4) = 1
# Maximum among them is 1
# The output array should be [4,3,2,1].

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 10 ^ 4
# -10 ^ 9 <= ARR[i] <= 10 ^ 9
# Where ‘T’ is the number of test cases, ‘N’ is the size of the array and ‘ARR[i]’ is the size of the array elements.
# Time Limit: 1 sec

# Sample Input 1:
# 2
# 4
# 1 2 3 4
# 5
# 3 3 4 2 4

# Sample Output 1:
# 4 3 2 1
# 4 3 3 2 2

# Explanation for sample input 1:
# Test case 1:
# Already explained in the question.
# Test case 2:
# Minimums of window size 1 = min(3), min(3), min(4), min(2), min(4) = 3, 3, 4, 2, 4
# Maximum among (3, 3, 4, 2, 4) is 4
# Minimums of window size 2 = min(3,3), min(3,4), min(4,2), min(2,4) = 3, 3, 2, 2
# Maximum among (3, 3, 2, 2) is 3
# Minimums of window size 3 = min(3,3,4), min(3,4,2), min(4,2,4) = 3, 2, 2
# Maximum among (3, 2, 2) is 3
# Minimums of window size 4 = min(3,3,4,2), min(3,4,2,4) = 2, 2
# Maximum among (2, 2) is 2
# Minimums of window size 4 = min(3,3,4,2,4) = 2
# Maximum among them is 2
# The output array should be [4,3,3,2,2].

# Sample Input 2:
# 2
# 5
# 45 -2 42 5 -11
# 6
# -2 12 -1 1 20 1

# Sample Output 2:
#  45 5 -2 -2 -11
#  20 1  1 -1 -1 -2
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Compute all the subArrays and for each window size and find max of min which is stored in ansArr that gets returned at the end
import math

def maxMinWindow(arr, n):
    ansArr = []
    for i in range(n):
        globMax = -math.inf
        j = 0
        while j < n - i:
            currMin = math.inf
            for k in range(j, j + i + 1):
                currMin = min(arr[k], currMin)
            globMax = max(globMax, currMin)
            j += 1
        ansArr.append(globMax)
    return ansArr

# TC: O(n^3) Explanation: Outer for-loop runs for n time and the inner while alongside the inner for-loop will run collectively for n(n+1)/2 for each outer for-loop's iteration.
# SC: O(1)


# Approach2: Better TC at cost of compromised SC - in approach 1 we perform an optimisation of removing the bundle of nested while and for-loop which contributed to n^2 TC, and instead we utilise only n TC there by using a stack to store numbers only once and thus for any given window we won't have to iterate those numbers which have previously been in earlier window of same size. So we'll use a for loop that runs till len(n) which will represent the window size and inside this we maintain a stack to store items on after the other that'll represent the current window. Hence, first i items we'll store without any additional operations, which will serve as first window of i+1 size. But once we cross the traversal of i items we'll pop the older items to remove older windows items which are no more relevant, and so that we can identify that items are older we'll store items in form of their indexes in the stack. While traversing items as we get a smaller item than top, we keep removing stack items and then as we find a smaller item or an empty stack we'll append the new item. Conversely on finding a bigger item it is directly appended onto Stack. Thus stack bottom is continuously compared for globMax across all windows and thus found globMax is stored in ansArr.
import math

def maxMinWindow(arr, n):
    ansArr = []
    for i in range(n):
        stack = []
        globMax = -math.inf
        for j in range(n):
            while stack and arr[stack[-1]] > arr[j]:
                stack.pop()
            stack.append(j)

            if j >= i:
                while stack and stack[0] < j - i:
                    stack.pop(0)
                globMax = max(globMax, arr[stack[0]])
        ansArr.append(globMax)
    return ansArr

print(maxMinWindow([45, -2, 42, 5, -11], 5))  # o/p:  45 5 -2 -2 -11
# TC: O(n^2)
# SC: O(n)


# Approach3: Create a leftMin and a rightMin array using a stack. Where for a given index in leftMin and rightMin, index of the closest smaller item to left of this item according to givenArr, and first smallest item found to right of this item from givenArr is written respectively. From the difference between items stored at same indices in both these arrays, we'll find a max window length where the item stored at this index in givenArr could be biggest amongst; let's make this into a diffArr. Thus obtained values in diffArr means that for window of that size and smaller ones, the item from givenArr corresponding to this index can participate to make the maximum window size. Now we'll start creating an ansArr according to the diffArr's items. As we traverse diffArr, diffArr's value which shows at max the givenArr's corresponding item can serve the window size of this value, we'll store in ansArr's index that is equal to diffArr's value, the givenArr's corresponding item. If in ansArr we already detect an item at the index equal to diffArr's value, we'll compare that pre-stored value with givenArr's corresponding value of currently traversed index and store the maximum one. This way we mapped diffArr's window size in ansArr with givenArr's value for those window size. Now as the item serving bigger window can also be max/relevant for smaller indexes we reverse traverse the ansArr and carry forward just the next index's value here and compare it with currently stored one in ansArr and keep stored the max one amongst two of them.
# YoutubeVidToRefer: https://www.youtube.com/watch?v=yRagSKdQgsc&ab_channel=BroCoders
import math

def maxMinWindow(arr, n):
    leftMin = []
    tempStack = []

    for i in range(n):
        while tempStack and arr[tempStack[-1]] >= arr[i]:
            tempStack.pop()
        leftMin.append(tempStack[-1]) if tempStack else leftMin.append(-1)
        tempStack.append(i)

    tempStack = []
    rightMin = ['_' for i in range(n)]
    for i in range(n - 1, -1, -1):
        while tempStack and arr[tempStack[-1]] >= arr[i]:
            tempStack.pop()
        if tempStack:
            rightMin[i] = tempStack[-1]
        else:
            rightMin[i] = n
        tempStack.append(i)

    diffArr = [rightMin[i] - leftMin[i] - 1 for i in range(n)]

    ansArr = ["_" for i in range(n)]
    for i in range(n):
        if ansArr[diffArr[i]-1] == "_":
            ansArr[diffArr[i]-1] = arr[i]
        else:
            ansArr[diffArr[i]-1] = max(arr[i], ansArr[diffArr[i]-1])

    for i in range(n - 2, -1, -1):
        if ansArr[i] == "_":
            ansArr[i] = ansArr[i + 1]
        else:
            ansArr[i] = max(ansArr[i], ansArr[i + 1])
    return ansArr

print(maxMinWindow([10, 20, 30, 50, 10, 70, 30], 7))
# TC: O(n) Explanation: Generalized or else it'll be 2n for creating leftArr and 3n for creating rightArr where n more is taken comparatively because of having to create a prefilled rightArr. On top, we'll have n time taken for computing diffArr and same for prefilled ansArr. And 2n collectively for last two for-loops, because n each.
# SC: O(n) Explanation: Generalized or it'll be close to 5n or so