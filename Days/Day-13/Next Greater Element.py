#https://leetcode.com/problems/next-greater-element-i/

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0 - indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example1:
# Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
# Output: [-1, 3, -1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1, 3, 4, 2].There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1, 3, 4, 2].The next greater element is 3.
# - 2 is underlined in nums2 = [1, 3, 4, 2].There is no next greater element, so the answer is -1.

# Example 2:
# Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
# Output: [3, -1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1, 2, 3, 4].The next greater element is 3.
# - 4 is underlined in nums2 = [1, 2, 3, 4].There is no next greater element, so the answer is -1.

# Constraints:
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 10^4
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.

# Follow up: Could you find an O(nums1.length + nums2.length) solution?
# ---------------------------------------------------------------------------------------------------------------------------------------
# Approach1: a nested for loops in which the outer one iterates over nums1 and inner for-loop iterates through nums2. We'll use an array of -1 by default filled to the length as nums1, to return the answer. Once we find the current item of nums1 in nums2, from there on the first bigger number we'll encounter would be stored at outer for-loop's current index in ansArr and we'll break the loop to avoid the number being overwritten by further bigger number.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ansArr=[-1 for i in nums1]
        for i in range(len(nums1)):
            match = False
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    match=True
                if match and nums2[j]>nums1[i]:
                    ansArr[i]=nums2[j]
                    break
        return ansArr
# TC: O(m*n) considering nums1 and nums2 are of size n and m respectively
# SC: O(n)


# Approach2: Better Time worst Space Complexity using Stack and hashDict - if we traverse given array nums2 from right to left, for a given item, the last encountered greater item is preferred over a farther placed greater item hence this becomes a LIFO problem where we use stack. We'll iterate through nums2 in reverse order while storing these items in a sorted order in a stack. As we iterate through nums2, we'll check from top, if stack has a greater item and if not we keep popping from stack till we encounter a greater item, or stack becomes empty. After this we append the currently iterated item from nums2 in the stack. The logic behind this step is that because the current item has been encountered it is going to be big enough for it's left items to use it, and so the smaller ones from stack can be deleted. As we do this in case a greater item is found we store it as value across the current item from nums2 as the key in a hashDict because we have to answer according to nums1 and not nums2. Later as we reference nums1 we check for that key's value in the hashDict and store it in an ansArr. This ansArr is then returned.
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreaterElem = {}
        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums2[i]:
                stack.pop()

            if len(stack) != 0:
                nextGreaterElem[nums2[i]] = stack[-1]
            else:
                nextGreaterElem[nums2[i]] = -1
            stack.append(nums2[i])

        ansArr = []
        for i in range(len(nums1)):
            ansArr.append(nextGreaterElem[nums1[i]])
        return ansArr

S = Solution()
print(S.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
# TC: O(2m+n) considering nums1 and nums2 are of size n and m respectively Explanation: first for loop iterates over nums2 which will take m time, but in there we use a while loop which pop all stack elements stored from the m sized array, hence which for all of it's iterations in for-loop will collectively run for m time at max; in addition, the second for loop which iterates over nums1 will incur additional n time complexity
# SC: O(2m) Explanation: stack can at max have m items and nextGreaterElem too will every time have m pairs. Besides, ansArr will take space but it's the one expected to return answer and is excluded
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# We have a similar question which too we're solving here where just instead of nums1 and nums2, we sort-of only have nums2 but with a catch that is a circular array: https://leetcode.com/problems/next-greater-element-ii/description/

# Given a circular integer array nums(i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing - order next in the array, which means you could search circularly to find its next greater number.If it doesn 't exist, return -1 for this number.

# Example1:
# Input: nums = [1, 2, 1]
# Output: [2, -1, 2]
# Explanation: The first 1 's next greater number is 2; The number 2 can 't find next greater number. The second 1 's next greater number needs to search circularly, which is also 2.

# Example2:
# Input: nums = [1, 2, 3, 4, 3]
# Output: [2, 3, 4, -1, 4]

# Constraints:
# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Double the same given array, one after the other and make it into one array. This array we'll iterate for it's only left half, to check through-out the entire array starting from the next item of the currently iterated one for finding the next greatest item:
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        ansArr = []
        for i in range(len(nums) // 2):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ansArr.append(nums[j])
                    break
            if j == len(nums) - 1 and nums[j] <= nums[i]:
                ansArr.append(-1)
        return ansArr

S = Solution()
print(S.nextGreaterElements([1, 2, 1]))
# TC: O(n^2)
# SC: O(n) Explanation: nums is extended by nums i.e. n more items


# Approach2: Better SC - Using a for loop we traverse the given array, and inside which we use a while loop that starts form the next index of where for-loop points and helps in comparing all items on the right from for-loop pointed item. Say this while loop pointer is j. This pointer is used as its modulo with len(nums), thus ensuring that j can cross the arrays indices, and we can still go on accessing array items which is how a circular array is. Now this while loop stops as soon as j%len(nums) becomes equal to i which means the whole list has been traversed, and now infinite looping condition has to be avoided, or the while-loop ends when we find an item at j%len(nums) index which is greater than the one pointed by outer for-loop. In case while-loop terminated because of traversing the whole circle once, we append -1 in ansArr or else nums[j%len(nums)] and at the end this ansArr is returned
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ansArr = []
        for i in range(len(nums)):
            j = i + 1
            while j % len(nums) != i and nums[j % len(nums)] <= nums[i]:
                j+=1

            if i!=j%len(nums):
                ansArr.append(nums[j%len(nums)])
            else:
                ansArr.append(-1)
        return ansArr

S = Solution()
print(S.nextGreaterElements([1, 2, 1]))
# TC: O(n^2) Explanation: for-loop runs for n times and inside it while could be running for 1, 2, 3, ... n times; thus making total TC as n(n+1)/2 for both loops' all the collective iterations
# SC: O(1) Explanation: ansArr is filled and directly returned and hence is exempted space as it's expected to return the output


# Approach3: Improved TC worsened SC using Stack - If this wasn't circular array we could have iterated the given arr in reversed fashion, where we maintained a stack which pops the first greatest number found than the currently iterated one, or the whole stack will empty. Further, if we don't find a bigger number, then in an ansArr we need to put -1 which needs to stay at this index. If we'd ansArr empty and simply appended -1 at this place then as we move from right to left we want the currently pushed one to be at the right in ansArr but the next appended ones will go on there. That's why here we use a prefilled ansArr with -1s. In this ansArr if we find a number from stack bigger than currently iterated one we'll store that at the particular index, and then append the currently iterated item in the stack. With using this approach in this question, there's only one problem that we're not dealing with a linear but a circular array here. Hence, say for [1,2,1] where for the 1 at the end, as we had just started traversing the given array we'll find stack to be empty and because of which we'll not find its bigger number which is 2. But by the end of one whole iteration of given array our stack would retain appropriate items and so if we take another iteration over given array now using the same stack then we'll get the accurate answers.
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ansArr = [-1 for i in nums]
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i]:
                stack.pop()

            if len(stack) != 0:
                ansArr[i] = stack[-1]

            stack.append(nums[i])

        for i in range(len(nums) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i]:
                stack.pop()

            if len(stack) != 0:
                ansArr[i] = stack[-1]

            stack.append(nums[i])
        return ansArr

S = Solution()
print(S.nextGreaterElements([1, 2, 1]))
# TC: O(4n) Explanation: talking about first for-loop, it will run for n-times and inside it the stack can collectively for the course of all its iteration under this for-loop run for n times. Thus one for-loop gave 2n TC and we've 2 such for-loops.
# SC: O(2n) Explanation: Stack and ansArr taking n each
