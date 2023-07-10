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
#         for i in range(1, len(height)):
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
        prefix, suffix = {0: 0}, {len(height) - 1: 0}
        maxBar = 0
        for i in range(0, len(height)):
            prefix[i] = maxBar
            maxBar = max(maxBar, height[i])

        maxBar = 0
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = maxBar
            maxBar = max(maxBar, height[i])

        sum = 0
        for i in range(1, len(height) - 1):
            sum += max(min(prefix[i], suffix[i]) - height[i], 0)
        return sum
# S=Solution()
# S.trap([4, 2, 0, 3, 2, 5])
# S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# TC: O(3n) Explanation: n space for for-loop + n space for computing prefixLeftMax + n for prefixRightMax.
# SC: O(2n) Explanation: n extra space for both prefixLeftMax and prefixRightMax.

# Approach3: Removing extra space from Approach-2 as well as using just one iteration throughout the array. So of essence is at each point to know how long is wall on either of the side, whichever is minimum. So we'll start iteration with 2 pointers l and r which will originally be set to point at 1st and last elem of given array. As we iterate from left and right we'll keep a track of maxLeft, for which we'll make a maxLeft and maxRight; originally both of which will be 0. First off at every iteration we'll check that value pointed by left pointer is smaller than the one pointed by right. In which case we know deciding factor is left pointer and using difference of wall's current height from left pointer we'll get amount of water to be stored at that index. But when current item i.e. left is smaller than right, it still could be the biggest left uptill that point in which case no water could be held above it, so we'll just update maxLeft as this item. In both of the scenario under left's height being smaller than right i.e. whether current left is maxLeft or not, at the end we increment left as that is our current pointer. Now if left point's to a value higher than right then we know right is deciding factor and so we check if current right is equal to or greater than maxRight so far, then we'll update maxRight to this value. If it's not maxRight we'll add to total water the difference between maxRight and height of item at index r. Under the scenario where right is smaller than left, at end we'll decrement right pointer by 1.
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,maxLeft,maxRight,total=0,len(height)-1,0,0,0
        while l<=r: #As we would also want to calculate water stored at the index where l and r are equal, so we put l<=r as opposed to l<r.
            if height[l]<height[r]:
                if height[l]>=maxLeft:
                    maxLeft=height[l]
                else:
                    total+=maxLeft-height[l]
                l+=1
            else:
                if height[r]>=maxRight:
                    maxRight=height[r]
                else:
                    total+=maxRight-height[r]
                r-=1
        return total
S=Solution()
S.trap([4, 2, 0, 3, 2, 5])
S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# TC: O(N)
# SC: O(1)