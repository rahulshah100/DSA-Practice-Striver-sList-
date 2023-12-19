# https://leetcode.com/problems/largest-rectangle-in-histogram/

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example1:
# Input: heights = [2, 1, 5, 6, 2, 3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1. The largest rectangle is shown in the red area, which has an area = 10 units.

# Example2:
# Input: heights = [2, 4]
# Output: 4

# Constraints:
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Use a nested for-loops. Outer for will point at item from givenArr and inner will count longest consecutive sequence viable for the item-pointed by outer for-loop. So with a count variable initialized as 0, in the inner for-loop we'll travel the givenArr comparing if the item being traversed is bigger or equal to the one pointed by outer for-loop in which case we increment count. In case we encounter a smaller item we'll store current counter value in a temp array and make count 0 again. As we end inner-for we'll compare max item from temp array and compare it with maxArea and maxArea is assigned the bigger value. Thus, after exhausting nested for-loops we return maxArea.
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        for i in range(len(heights)):
            ct = 0
            tempCt = []
            for j in range(len(heights)):
                if heights[j] < heights[i]:
                    tempCt.append(ct)
                    ct=0
                else:
                    ct+=1
            tempCt.append(ct)
            maxArea = max(maxArea, heights[i] * max(tempCt))
        return maxArea

S=Solution()
print(S.largestRectangleArea([2,1,5,6,2,3]))
"""
# TC: O(2n^2) #Explanation: 2 for-loops constituting to n^2 TC and in addition every time after inner for-loop exhausts we've to traverse a temp array to find max which will be another n, hence we've n(2n) TC
# SC: O(n) Explanation: For temp Array we'll use up n space


# Approach2: Optimised Approach1's tempCt array with a maxCt variable
"""class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        for i in range(len(heights)):
            ct = maxCt = 0
            for j in range(len(heights)):
                if heights[j] < heights[i]:
                    maxCt=max(maxCt,ct)
                    ct=0
                else:
                    ct+=1
            maxCt = max(maxCt,ct)
            maxArea = max(maxArea, heights[i] * maxCt)
        return maxArea
"""
# TC: O(n^2)
# SC: O(1)


# Approach3: Improved TC compromised SC - using a stack and 2 prefix leftBound and rightBound arrays. We'll use a monotonous stack to build a prefix left array which represents the left bound of an item.
# So say givenArr is [2,1,5,6,2,3] then for 2 onto it's left we don't have a number and cant extend it beyond, so it could be at best extended to index 0 on left. We'll record this index in leftBound array and put the index in a stack too.
# Next as we are looking for 1's leftBound we'll use stack as a reference of comparing element. We know one thing that leftBound has to be a number smaller than current one coz say we want to extend 1 to left, then we cant do it if we encounter a block of height 0. So when comparing 1 with stack index's item we see at index 0 -> item 2 is not bigger than in which case we know going to right from here as 1 is smaller than 2 we have a leftBound for upcoming items before 2, and so we pop the index 0 from stack and as there are no more items, we put index 1 now in stack and in leftBased-index we append 0.
# Further, for 5, in stack at index 1 we have 1 which is smaller and hence cant be popped, so we put index 2 i.e. represents 5 in stack and 2 i.e. represents leftBound index in leftBound array.
# Now for 6, it is bigger than 5 so nothing popped and the index 3 is directly appended in stack and in leftBound array.
# For 2 index3=>6 is popped and so is then index2=>5, and we encounter index1=>1 in the stack and as 1 is smaller, it's not popped but index of 2 i.e. 4 is stored on top in stack.
# At last popped here was index2 we store index 2 in leftBound array. At last for 3 index4=>2 is first encountered and nothing is popped but index of 3 i.e. 6 is stored in stack and 6 is stored in leftBound
# Similarly for rightBound we'll generate an array using stack, for which we'll traverse the given array from right and after which we can find difference between indices stored for an item in rightBound and leftBound giving us the width multiplied with that item from heights array to get this item's area and highest area as is returned
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftBound = []
        stack = []
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                leftBound.append(0)
            else:
                leftBound.append(stack[-1] + 1)
            stack.append(i)

        rightBound = [-1 for i in heights]
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                rightBound[i] = len(heights) - 1
            else:
                rightBound[i] = stack[-1] - 1
            stack.append(i)

        maxArea = 0
        for i in range(len(heights)):
            area = heights[i] * (rightBound[i] + 1 - leftBound[i])
            maxArea = max(maxArea, area)

        return maxArea

S = Solution()
print(S.largestRectangleArea([2, 1, 5, 6, 2, 3, 1]))
print(S.largestRectangleArea([1, 2, 1, 1]))
# TC: O(6n) Explanation: creating leftBound array takes a for-loop in which for a total of n times the while would run in total, yielding a collective TC of these loops as 2n, same for rightBound array just that there we also had to create initially a rightBound array filled with -1 for n times, adding an n TC. At last the for iteration for counting area adds n TC more.
# SC: O(3n) Explanation: for left/rightBound arrays and stack n space each.


#Approach4: In approach3 - Combining process of finding both left and right bound i.e. essentially the whole girth together, as we iterate in givenArr. Consider givenArr to be [2, 1, 5, 6, 2, 3]. As we iterate, in a stack we'll store subLists 2 elements - leftBoundIndex for current item and the item itself. We have to store the item too here, because unlike in approach3, where we put indices in stack and then compared currentItem with items on those indices, here we're not storing item indices itself but leftBounds hence we cant trace the items and so we store them alongside
# For index0=>2 stack is empty and so leftBound is 0 and item is 2 is stored in stack i.e.[0,2]
# For index1=>1 we know item in stack i.e. 2 cant be extended further as height 1 doesn't support 2's extension for forming area, and hence we pop 2. As we do this we calculate its area once which is its rightBound that is the current iteration index which became it's rightBound and only so it's being popped which in this case is index1 -  it's leftBound as stored in the stack's subList i.e. 0 => 1-0 * item => 2. maxArea so far is 2. Now we push the subList for current item 1, where we see the popped item has been popped because current item is smaller meaning that current could surely be extended to leftBound of popped item which here is 0. So we store [leftBound, item] as [0,1] in stack
# Further for index2=>5, it's bigger than 1 and hence does support 1's extension, and so we store on top of stack as [leftBound, item] meaning [2,5].
# For index3=>6 it's bigger than 5 and is stored in stack as [3,6]
# For index4=>2 we pop 6 and count its area as indexOfCurrIteration-leftBoundOfTopOfStack * item => 4-3 * 6=> 6  and our maxArea becomes 6. Furthermore, 5 is also smaller and gets popped and means its area is counted which is 4-2 * 5 => 10 and maxArea becomes 10. Finally, 5's leftBound becomes current item i.e. index4=>2's leftBound and in stack we store [2, 2]
# At last we encounter 3 which is bigger than 2 and directly gets stored in stack as [5, 3]
# As we finish iterating over givenArr, we attend calculating areas for items yet not popped i.e.the ones still in stack. For this we understand they are still in stack because they didnt find a rightBound meaning, till end of stack they can be extended. So len(givenArr)-leftBoundOfItem * Item is how we find maxArea for these remaining items and keep comparing them with maxArea variable to update maxArea which is returned at last.
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            startInd = i
            while len(stack) != 0 and stack[-1][1] >= heights[i]:
                print(i, stack[-1][1], heights[i])
                startInd, item = stack.pop()
                maxArea = max(maxArea, (i - startInd) * item)
            stack.append([startInd, heights[i]])

        for i in range(len(stack)):
            maxArea = max(maxArea, (len(heights) - stack[i][0]) * stack[i][1])

S = Solution()
print(S.largestRectangleArea([2, 1, 5, 6, 2, 3]))
# TC: O(3n)
# SC: O(n)