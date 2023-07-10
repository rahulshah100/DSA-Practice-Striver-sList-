# Next Permutation
# https://leetcode.com/problems/next-permutation/

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e. sorted in ascending order). The replacement must be in place and use only constant extra memory.

# Example: Input: nums = [1,2,3] Output: [1,3,2]
#          Input: nums = [3,2,1] Output: [1,2,3]
#          Input: nums = [1,1,5] Output: [1,5,1]
#          Input: nums = [1] Output: [1]

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# -----------------------------------------------------------------------------------------------------------------------------

# Approach 1: Consider for example 468732, the smallest bigger permutation is 472368. Break the given number i.e.468732 in 2 parts 46 and 8732; we can observe that in 8732 where from right to left numbers are constantly increasing and hence in that entire number no combination is possible to make it further greater in value. Therefore if we want to find a higher number, then while traversing in the number from right to left we must look for a digit which we can find smaller than the previously encountered one. In this example we find 6 to be smaller than 8 and before that while going from right to left no other digit could be found smaller than previously encountered one. Now that we found 6 we want to make the given number i.e.468732 just the smallest bigger value possible and hence we'll swap 6 with the farthest right digit which is bigger than 6 which here is 7. We did the last step keeping in mind that as we'll go farther from 6 the numbers are decreasing i.e.8 is greater than 7 is greater than 3 and so on... therefore, by swapping with farthest right bigger than 6 we know that the smallest possible number is what we'll get, or else we could get 6 swapped with 8 making the given number as 48.. which clearly isnt smallest bigger number as 47... are still possible from given value. After swap we have 478632. Also while swapping we know that from the right side we had increasing sequence and that's why only at 6, where the sequence broke we made a swap; anyhow, as we want to get a smallest higher number, now that the swapping is done, we have a increasing sequence to the right of swapped digit, like here to right of 7 we have 8632, and to make the overall number smaller we'll reverse this sequence which will give us 472368.
# Steps: Initial sequence 0125330
#        Find longest non increasing suffix 012[5330]   #Highlighted portions are tried to show in every step by new []
#        Identify pivot 01[2][5330]
#        Find rightmost successor to pivot in the suffix 01[2[[53[3]0]
#        Swap with pivot 01[3][5320]
#        Reverse the suffix 0130235

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Finding Pivot
        pivot = None
        pivotIndex = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = nums[i - 1]
                pivotIndex = i - 1
                break

        # Handling the case where no pivot is found, in which scenario we'll have to reverse the array
        if pivot == None:
            nums[:] = nums[::-1]  # See how instead of nums = nums[::-1], we are making a copy by writing nums[:]=nums[::-1]. This is important to remember that in python and most other languages we have assignment, deep and the shallow copy of variables, where in, for list,dict,set,tuple by writing oldvar=newvar both the variables start pointing to one same memory address and hence by making changes to one variable the other variable could get affected. Hence while assigning the whole array a new array variable i.e. making a variable equal to an another array variable, we should use the above syntax to avoid further problems. Mark that if only one item at an index has to be changed like arr[2]=2 has to be made or arr=[12,34,3] is to be written, it could be done as written; but only when we have to make the varibale equal to an another variable, we need to be cautious and make their copy like above.
        else:
            # Finding the rightmost successor to pivot in suffix & swapping it with pivot
            tempVar = None
            for i in range(len(nums) - 1, pivotIndex - 1, -1):
                if nums[i] > nums[pivotIndex]:
                    temp = nums[pivotIndex]
                    nums[pivotIndex] = nums[i]
                    nums[i] = temp
                    break

            # Reverse the suffix
            tempArray = nums[pivotIndex:len(nums)]
            revTempArray = tempArray[::-1]

            # Update the nums Array with reversed suffix:
            j = 0
            for i in range(pivotIndex + 1, len(nums)):
                nums[i] = revTempArray[j]
                j += 1

        print(nums)


S = Solution()
S.nextPermutation([0, 1, 2, 5, 3, 3, 0])
S.nextPermutation([1, 2, 3])
S.nextPermutation([3, 2, 1])
# Time Complexity: O(n) Considering nums has a length n. Explanation: Finding Pivot in worst case takes n iterations. If we go further into if then we've array reversal which we can assume in worst guess could take O(n) time complexity. If otherwise else is the case, we have one for loop, considering worst case it would have a time complexity of O(n), and further down in the else we encounter two O(n) for reverse suffix and a O(n) for updating the nums with reversed suffix. Hence in if and else, the else case will have worst time complexity in which we'll have in total like O(n)+O(n)+O(n)+O(n) which could be generalized as O(n).
# Space Complexity: O(n). Explaination: Starting from the begining of the code, we encounter pivot and pivotIndex variable with constant space complexity. Then we see tempArray, which in worst case would occupy n items; in effect, revTempArray would hold same n number of items. Space Complexity therefor is O(n)+O(n)=O(2n) which can be generalized as O(n)


# Approach 2:Improved Space complexity than approach1 as here instead of using temporary array for storing reversed arrays, we're doing that in the place in nums array.
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find longest non-increasing suffix
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)

        # find pivot
        pivot = right - 1
        successor = 0

        # find rightmost succesor
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break

        # swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # reverse suffix
        l = pivot + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        print(nums)
"""
# Time Complexity: O(n)
# Space Complexity: O(1)
