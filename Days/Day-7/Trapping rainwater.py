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
# Approach1: Brute Force. In a for loop, we'll compute for each bar how much water get stored at that particular index. We'll sum the total water of all indexes and return total. To compute how much water a particular index can hold, it's dependant on the highest walls on both the side from that index i.e Left and Right. Say if to left a wall is 3 high and Right one is 2. Than min(Left,Right) i.e.2 is how much could be hold b/n both these walls as the rest will go from above height 2, and hence wont be maintained in b/n these walls. Further if that index is also having a height say 0.5 then only on top of 0.5 at that index could water be stored, which here makes total water for that index=2-0.5=min(Left,Right)-height[currIndex].
from typing import List
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         total=0
#         for i in range(1,len(height)-1): #As first bar is having open Left side and last bar is having open Right side, so no water can be trapped at this two index, hence we skip them here.
#             maxLeft=-1
#             maxRight=-1
#             j=k=i
#             while j>=0: #Calculating maxLeft at that index
#                 if maxLeft<height[j]: maxLeft=height[j]
#                 j -= 1
#             while k<len(height):
#                 if maxRight<height[k]:  maxRight=height[k]
#                 k+=1
#             total+=min(maxLeft,maxRight)-height[i]
#         print(total)
#         return total
# S=Solution()
# S.trap([4, 2, 0, 3, 2, 5])
# S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# TC:O(n^2) Explanation: Inside the for loop, together both inner while loop takes almost n iterations. So here we have an n inside n Time complexity.
# SC:O(1)

# Approach2: In approach 1, we'll reduce the T.C. at cost of space complexity, by calculating a prefixLeftMax and suffixRightMax. As prefixLeftMax, we'll calculate just for once, an array of n items from left to right, at each index showing the leftMax till that point. For suffixRightMax we'll start from right to left of given array here and put them at those indexes in suffixRightMax. Now in for loop, we can just refer to these arrays.
class Solution:
    def trap(self, height: List[int]) -> int:
        prefixLeftMax, suffixRightMax, total = [height[0]], [height[-1]], 0

        for i in range(1,len(height)):
            prefixLeftMax.append(max(prefixLeftMax[i-1], height[i])) #I've observed Arr.insert(pos,item) is working fine for inserting at starting of list but for inserting at the ending, it is causing problem. So we are using append here and not insert(-1,item).

        for i in range(len(height)-1,-1,-1):
            suffixRightMax.insert(0, max(suffixRightMax[0],height[i]))

        for i in range(1,len(height)-1): #As first bar is having open Left side and last bar is having open Right side, so no water can be trapped at this two index, hence we skip them here.
            maxLeft=prefixLeftMax[i]
            maxRight=suffixRightMax[i]
            total+=min(maxLeft,maxRight)-height[i]
        print(total)
        return total
# S=Solution()
# S.trap([4, 2, 0, 3, 2, 5])
# S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# TC: O(3n) Explanation: n space for for-loop + n space for computing prefixLeftMax + n for prefixRightMax.
# SC: O(2n) Explanation: n extra space for both prefixLeftMax and prefixRightMax.

# Approach3: Removing extra space from Approach2 by using Two Pointer Method. Using two pointers l and r and we'll keep traversing from left and right of the given array. We'll compare the height of left and right items. If height of left item is lesser than right one, then there are no chances that due to atleast this iteration we'd need to reassign maxRight, as up until this iteration we have a rightMax in-place till r pointer, and new value of height[l] is lesser than height of r, so height[l] ofcourse have to be smaller than maxRight too. In this case, we'll use maxLeft as our basis to calculate how much water could be stored and would check whether with this new iteration maxLeft has to be reassigned. Similarly we compute with maxRight if height[l] is not lesser than height[r].
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,maxLeft,maxRight,total=0,len(height)-1,0,0,0
        while l<=r: #As we would also want to calculate water stored at the index where l and r are equal,we have put l<=r and not l<r.
            if height[l]<height[r]:
                if height[l]>=maxLeft:maxLeft=height[l] #In this case, at this point we've found biggest leftside wall till this point. Due to this there wont be anything to left of this bar, which can act as a higher wall to maintain water on top of this one. So we dont add anything to total.
                else: total+=maxLeft-height[l] #In this case we have a precise maxLeft uptill this point and have found a rightMax not necessarily the bigges one but atleast taller than maxLeft. Hence on basis of maxLeft height regardless of how big maxRight, we'll subtract the height of bar at the current index to get water stored at this index.
                l+=1
            else:
                if height[r]>=maxRight:maxRight=height[r]
                else: total+=maxRight-height[r]
                r-=1
        print(total)
        return total
S=Solution()
S.trap([4, 2, 0, 3, 2, 5])
S.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# TC: O(N)
# SC: O(1)