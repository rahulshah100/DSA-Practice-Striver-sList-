# https://leetcode.com/problems/reverse-pairs/
# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

# Example 1:
# Input: nums = [1, 3, 2, 3, 1]
# Output: 2

# Example 2:
# Input: nums = [2, 4, 3, 5, 1]
# Output: 3

# Constraints:
# 1 <= nums.length <= 5 * 104
# -231 <= nums[i] <= 231 - 1
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Two for loops. First for loop pointing at one element, second for pointing at all the element after it, one by one. If condition of nums[i] > 2 * nums[j] matches then use a counter variable, and keep on increasing it's value.
# Time Complexity: O(n^2). Explaination: It will take n(n+1)/2 iterations in total for the both the for loops to traverse the entire array.
# Space Complexity: O(1). Explaination: We'll just use one extra variable i.e. count, which will hold only an integer value. So we use constant space i.e.O(1).

# Approach2: Better time, compromised space Complexity. We'll use Merge sort and in there at the stage when elements would be merged, we'll check for nums[i] > 2 * nums[j]. If so, we'll increase a counter variable.
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int: #1
        def recursiveFunction(lowerIndex=0, upperIndex=len(nums) - 1):
            if lowerIndex >= upperIndex:
                return 0

            midIndex = (lowerIndex + upperIndex) // 2
            count = recursiveFunction(lowerIndex, midIndex) + recursiveFunction(midIndex + 1, upperIndex)

            index_i = lowerIndex
            for rightNumber in nums[midIndex+1: upperIndex+1]:  # For all right array elems...
                while index_i < midIndex and nums[index_i] <= rightNumber * 2:  # ...we'll compare each of them, one at a time, with left array elems starting from index_i index, to see if that left arr elem is lesser than or equals to the twice of that right arr elem...
                    index_i += 1  # ...If so we increase the left arr pointer and again compare the given right arr elem with the next left arr elem.
                count += midIndex + 1 - index_i #Now note: Above we calculated those index upto which the left arr items were less or equal to that right arr elem. So from where the index_i got stopped, after that uptill (mid+1) i.e. starting of right arr, we are having those elems which are equal to or higher than twice of right arr elem; this is because left arr is sorted in it's self so all number from where left_arr_elem isnt less than or equal to twice the right arr elem, from then all left arr elem shouldn't be meeting that condition. Also note how i is not reset in while loop, but it's value will persist accross all the while loop's iterations. So for the current right elem as such, till index_i the elems in left arr were not big enough to be or double the size of right arr elem, and as such right arr is sorted and next right arr elem will be bigger than the prev one, hence left arr elem till index_i will also not be bigger for the next right arr elem. This makes this snippet to hold O(n) time complexity.

            nums[lowerIndex: upperIndex + 1] = sorted(nums[lowerIndex: upperIndex + 1]) #See the below code line which is returning our recursion function; there we're just returning count variable and not the sorted nums, but yet as nums is being referred from #1 which makes nums as not a local variable to the recursive functions, but a common variable, and so only one copy of the nums declared at #1 is maintained throught out all the recursive calls. Hence at every level of recursion we'll be getting sorted nums from lower levels without having to return them from each level.
            return count
        return recursiveFunction()

S=Solution()
print(S.reversePairs([23,12,34,1,232,63]))
# Time Complexity: O(nlogn) Explaination: Total time taken here is ((N)(Time taken for reversePairsCount) + (N)(Time taken for merging))*log(N)=>(N+N)logN=>O(2NlogN)=>O(NlogN)
# Space Complexity: O(n) Explaination: Apart from what mergesort uses, here we are using couple of more variables with constant space allocation like count, index_i. Hence O(n)+o(1)=O(n).