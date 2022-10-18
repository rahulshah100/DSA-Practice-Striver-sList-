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
# Approach 1: My Original Idea. Use a pointer at starting of both the arrays. Compare values of these array for their respective pointer position. As per the comparison of values, perform some appropriate operations to fill nums1 in sorted fashion. Till all the elements of nums2 are not traversed through, keep on repeating the process of filling nums1.
from typing import List

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            nums1[:] = nums1[:m]
        elif m == 0:
            nums1[:] = nums2
        else:
            lowerPointerAt = 0
            higherPointerAt = 0
            count = 0
            while higherPointerAt <= n-1:
                if lowerPointerAt >= m + count:
                    nums1[:] = nums1[:lowerPointerAt]
                    for i in nums2[higherPointerAt:n]:
                        nums1.append(i)
                    print(nums1)
                    return nums1
                elif nums1[lowerPointerAt] < nums2[higherPointerAt]:
                    lowerPointerAt += 1
                elif nums1[lowerPointerAt] >= nums2[higherPointerAt]:
                    nums1.insert(lowerPointerAt, nums2[higherPointerAt])
                    higherPointerAt += 1
                    lowerPointerAt += 1
                    count += 1
        nums1[:] = nums1[:m + n] #We continue to have trailing zeros as were in the given array. To remove them we do the array slicing.
        # print(nums1)
        return nums1


# S = Solution()
# S.merge([0, 0], 0, [21, 23], 2)
# S.merge([21, 23], 2, [0], 0)
# S.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# S.merge([2, 0], 1, [1], 1)"""
# Time Complexity: O(2(m+n)). Given the worst case scenario, we'll neither have n==0 or m==0. If those were cases our time complexities would have been O(m+m+n) or O(n+m+n) respectively as we have to copy nums1 from nums1[:m] snd nums2; further after which we also copy into nums1 the nums1[:m+n], hence we had that complexity. Here we go into the last else. Due to the two inner elifs, while will run for m+n in worst case like [12,13,14,20,0,0,0] and [17,18,19]. The if inside while run for O(m) to copy nums[1:lowerPointerAt] to nums1, and +O(n) for the for loop traversing the nums2.
# Space Complexity:O(1)

# Approach2: Better than Approach1.
# We have 3 pointers. Starting from back of array M i.e. at the M+Nth index, we'll start storing the bigger value as is evaluated by comparison of pointers a & b, both of which are at M and Nth index respectively. Amongst a or b, any pointer's value is chose, that pointer is decreased. We'll keep on doing this till b is greater than or equal to 0th index. If b decrease than that, then that'll mean array has been sorted. If b>=0 but a<0 then we'll copy remaining elements pointed by b one by one by decreasing the pointer.
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