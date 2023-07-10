# https://leetcode.com/problems/merge-sorted-array/

# You are given two integer arrays nums1 and nums2, sorted in non - decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non - decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the array nums1.To accommodate this, nums1 has a length of  m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1: Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3 Output: [1, 2, 2, 3, 5, 6] Explanation: The arrays we are merging are[1, 2, 3] and [2, 5, 6]. The result of the merge is [1, 2, 2, 3, 5, 6] with the underlined elements coming from nums1.

# Example 2: Input: nums1 = [1], m = 1, nums2 = [], n = 0 Output: [1] Explanation: The arrays we are merging are[1] and []. The result of the merge is [1].

# Example 3: Input: nums1 = [0], m = 0, nums2 = [1], n = 1 Output: [1] Explanation: The arrays we are merging are [] and [1]. The result of the merge is [1]. Note that because m = 0, there are no elements in nums1.The 0 is only there to ensure the merge result can fit in nums1.

# Constraints: nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[j] <= 10^9
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach 1: My Original Idea. Given that arrays are sorted in themselves, we can use bubble sort and get array1 sorted on the collective basis. We can then again use buble sort on array 2. Later, we can merge arrays by substituting the trailing 0s in 1st array with all items from 2nd array.
from typing import List

"""
class Solution:
     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m):
            for j in range(n):
                if nums1[i]>nums2[j]:
                    nums1[i],nums2[j]=nums2[j],nums1[i]
        print(nums1,nums2)
        for i in range(len(nums2)): #as just in any fashion items are swapped and pushed inside nums2, nums2 might not be sorted
            for j in range(i+1,len(nums2)):
                if nums2[i]>nums2[j]:
                    nums2[i], nums2[j] = nums2[j], nums2[i]
            nums1[m+i]=nums2[i]
        print(nums1)


# S = Solution()
# S.merge([0, 0], 0, [21, 23], 2)
# S.merge([21, 23], 2, [0], 0)
# S.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# S.merge([2, 0], 1, [1], 1)"""
# Time Complexity: O(mn + n^2)
# Space Complexity:O(1)

# Approach2: Better than Approach1.
# 3 pointer method. Starting from back of array M i.e. at the M+Nth index, we'll start storing the bigger value as is evaluated by comparison of pointers a & b, both of which are at M and Nth index respectively. Amongst a and b, whichever pointer's value is chose that pointer is decreased. We'll keep on doing this till b is greater than or equal to 0th index. If b decrease than that, then that'll mean array has been sorted. If b>=0 but a<0 then we'll copy remaining elements pointed by b one by one by decreasing the pointer.
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        a, b, write_index = m - 1, n - 1, m + n - 1
        while b >= 0:
            if a >= 0 and A[a] > B[b]:
                A[write_index] = A[a]
                a -= 1
                print('n',A,B)
            else:
                A[write_index] = B[b]
                b -= 1
            print('m', A, B)
            write_index -= 1
        print(A)

S = Solution()
S.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# S.merge([2, 0], 1, [1], 1)
# TC: O(m+n)
# SC: O(1)