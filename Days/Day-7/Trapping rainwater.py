# https://leetcode.com/problems/trapping-rain-water/

# Trapping Rain Water
# Given n non - negative integers representing n elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Explanation: The above elevation map(black section) is represented by array[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1].In this case, 6 units of rain water(blue section) are being trapped.

# Example2:
# Input: height = [4, 2, 0, 3, 2, 5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# ----------------------------------------------------------------------------------------------------------------------
# Approach1: Brute Force. In a for loop, we'll compute for each bar how much water get stored at that particular index. We'll sum the total water of all indexes and return total. To compute how much water a particular index can hold, it's dependant on the highest walls on both the side from that index i.e Left and Right. Say if to left a wall is 3 high and Right one is 2. Then min(Left,Right) i.e. 2 is how much could be held b/n both these walls as the rest will go from above height 2, and hence wont be maintained in b/n these walls. Further if that index is also having a height say 0.5 then only on top of 0.5 at that index could water be stored, which here makes total water for that index=2-0.5=min(Left,Right)-height[currIndex].
from typing import List
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         sum = 0
#         for i in range(len(height)):
#             l, u, maxL, maxU = i - 1, i + 1, 0, 0
#             while l >= 0:
#                 maxL = max(height[l], maxL)
#                 l -= 1
#             while u < len(height):
#                 maxU = max(height[u], maxU)
#                 u += 1
#             sum += max(min(maxU, maxL) - height[i], 0) #min water will be atleast 0
#         return sum
# S=Solution()
# S.trap([4, 2, 0, 3, 2, 5])
# S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# TC:O(n^2) Explanation: Inside the for loop, together both inner while loop takes almost n iterations. So here we have an n inside n Time complexity.
# SC:O(1)


# Approach2: In approach 1, we'll reduce the T.C. at cost of space complexity, by calculating a prefixLeftMax and suffixRightMax. As prefixLeftMax, we'll calculate just for once, an array of n items from left to right, at each index showing the leftMax till that point. For suffixRightMax we'll start from right to left of given array here and put them at those indexes in suffixRightMax. Now in for loop, we can just refer to these arrays.
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = {}
        maxHeight = 0
        for i in range(len(height)):
            prefix[i] = maxHeight
            maxHeight = max(maxHeight, height[i])

        suffix = {}
        maxHeight = 0
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = maxHeight
            maxHeight = max(maxHeight, height[i])

        totWater = 0
        for i in range(len(height)):
            totWater += max(min(prefix[i], suffix[i]) - height[i], 0)

        return totWater
# S=Solution()
# S.trap([4, 2, 0, 3, 2, 5])
# S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# TC: O(3n) Explanation: n space for for-loop + n space for computing prefixLeftMax + n for prefixRightMax.
# SC: O(2n) Explanation: n extra space for both prefixLeftMax and prefixRightMax.


# Approach3: Removing extra space from Approach-2 as well as using just one iteration throughout the array. So the intuition is that for a block of importance is its leftMaxWall or rightMaxWall, whichever one is shorter coz between two of them i.e. leftMaxWall and rightMaxWall, that much is only what could be stored. With that in mind we'll traverse the given array with 4 pointers l,r which are current left and right indexes, assigned at the start as 0 and len(arr)-1; and leftMax,rightMax which are uptill l the highest block height and in reverse order after r the highest wall found, both assigned to 0 at start. Mainly we'll only increment l uptill l is less than or equal to r. As we start our arrangement of code has been made such that we check if arr[l]<=arr[r] and if so we'll stay ensured the left wall is determining how much water could be stored for this block. This is where 2 cases arise: 1) If further arr[l]<leftMax then leftMax bounds the amount of water we can store at this block which is equal to leftmax-arr[l]  2) If not then arr is either equal to leftMax or greater than leftMax, so this is where current block becomes leftMax and hence no water could be stored on top. In both these case we increment l. This was all if arr[l]<=arr[r] and if this condition was not true it means the right wall is determining factor to how much water could be stored at this block. Under this scenario we are posed with further 2 cases 1) arr[r]<rightMax which if the case rightMax is binding parameter, and we add rightMax-arr[r] to the totalWater stored. 2) If arr is equal to right rightMax or greater than arr[r] is the rightMax and so no water will be stored on top here, hence we just reassign rightMax to arr[r]. Under both these scenarios we decrement r.
class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = rightmax = totWater = 0
        l, r = 0, len(height) - 1
        while l <= r:  # As we would also want to calculate water stored at the index where l and r are equal, so we put l<=r as opposed to l<r.
            if height[l] <= height[r]:
                if height[l] < leftmax:
                    totWater += leftmax - height[l]
                else:
                    leftmax = height[l]
                l += 1
            else:
                if height[r] < rightmax:
                    totWater += rightmax - height[r]
                else:
                    rightmax = height[r]
                r -= 1
        return totWater

S=Solution()
S.trap([4, 2, 0, 3, 2, 5])
S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# TC: O(N)
# SC: O(1)