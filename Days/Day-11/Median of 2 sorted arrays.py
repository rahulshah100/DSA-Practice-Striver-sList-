# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log(m + n)).

# Example1:
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000
# Explanation: merged
# array = [1, 2, 3] and median is 2.

# Example2: Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: 2.50000
# Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Make one separate array that combines given two, and sort it. If length of given array is odd return mid element or return (sum of mid, mid+1th item)/2
# TC: O(m+n+mnlogmn)
# SC: O(m+n)


# Approach2: Given that arrays are sorted, in approach 1 we can avoid sorting. While making one array we can use 2 pointers - one on each given array to compare smaller value and push that into our new array. If one array exhausts then that's from where we push the rest of remaining items in the other array. This spares us from sorting the newly generated array.
# TC: O(m+n)
# SC: O(m+n)


# Approach3: In approach2 instead of storing all items in array and then finding median, here we just maintain two variables called lastPointedItem and secondLastPointed item which keeps getting overwritten with recently updated pointer amongst pointer1, and pointer2, where pointers are collectively incremented for (len(n)+len(m))//2 times. Thus when exhausted, lastPointedItem variable will have median element from both arrays in case len(n)+len(m) is odd Eg: len(n)+len(m)=9.In case where len(n)+len(m) is even like 8 we use average of lastPointedItem and secondLastPointedItem.
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pt1 = pt2 = 0

        counter = (len(nums1) + len(nums2)) // 2

        lastPointedItem = secondLast = None
        while counter >= 0:
            secondLast = lastPointedItem
            if pt1 < len(nums1) and (pt2 >= len(nums2) or nums1[pt1] <= nums2[pt2]): #Ordering of condition is important that if pt1 is equal or greater than len(nums1) we'll not calculate nums1[pt1] to check the condition nums1[pt1] <= nums2[pt2] or that will give error. Similarly in the case where 2nd arr is empty or has been exhausted then pt2>=len(nums) will turn true and so too we'll not check nums2[pt2] which'd give error
                lastPointedItem = nums1[pt1]
                pt1 += 1
            else:
                lastPointedItem = nums2[pt2]
                pt2 += 1
            counter -= 1

        if (len(nums1) + len(nums2))  % 2 == 0:
            return (lastPointedItem + secondLast) / 2
        else:
            return lastPointedItem


S = Solution()
print(S.findMedianSortedArrays([1, 3], [2]))
print(S.findMedianSortedArrays([1, 2], [3, 4]))
# TC:O(m+n) Explanation: collectively pointer1 and pointer will be run for n+m//2 which gives TC of n+m
# SC:O(1)


# Approach4: Binary Search - Given that arrays are sorted we think to use binary search. We could use Binary sort to figure the split in any one array while the second array's split would be adjusted accordingly in a way that collectively both splits are first half of combined arrays. As in if totItems from both arrays are 10 and len(arr1)=4, then in first go we will have 2 items from array 1, adjusting to which 10//2 - 2 => 3 more are taken from arr2. To understand if cut is appropriate the left half being formed should have all items lesser than right half. Hence, item just before cut1 should be smaller than item just after cut2, and vice versa i.e. item just before cut2 should be lesser than item just before cut1. If item before cut1 is bigger than item after cut2, we reduce item by going left in our sorted array arr1, by reducing upper pointer to cut1-1. Conversely, having item before cut2 bigger than item after cut1 then we increment lower pointer to cut1+1. Thus, after finding the cuts, if totItems is odd we return the maximum amongst item just before cut1 and item just before cut2. On the other hand if totItems is even we know not just left half but also from right half an item has to be picked and averaged out with last item from left half of array. For finding this right half item we will pick minimum amongst item just after cut1 and cut2. There are two edge case here tho - (1) when cut is at 0 item right before it (say l1) would be none and comparing it with item after cut will yield error, so that's when we assign l1 as -math.inf. (2) when cut1 is at len(arr) just the next item say r1 is None, and when is compared with item before cut2 would yield Error, so that's when we assign r1 as math.inf.
from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1) #Ensuring additional optimization that we'll only traverse for shorter array length

        totItems = len(nums1) + len(nums2)
        low, up = 0, len(nums1) #Reason we take 'up' as len(nums) and not lens(nums)-1 is because to find median, possibly we might have to take first whole array in which case we would require cut at last i.e. after last item so l1 could be included as last item from nums1

        while low<=up:
            cut1 = (low + up) // 2
            cut2 = (totItems + 1) // 2 - cut1 #In case len(nums1)=2 and len(nums2)=3, cut1=1 and nums1 will yield only one item at that time totItems=5 and we must get 2 more elems from nums2 so we have a total of 3 elem which is median. totItems//2 - cut1 here gives 5//2 - 1=>1, hence we've done totItems+1 to calculate cut2.

            l1 = -math.inf if cut1 == 0 else nums1[cut1 - 1]
            l2 = -math.inf if cut2 == 0 else nums2[cut2 - 1]
            r1 = math.inf if cut1 == len(nums1) else nums1[cut1]
            r2 = math.inf if cut2 == len(nums2) else nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if totItems % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                up = cut1 - 1
            else:
                low = cut1 + 1

S = Solution()
print(S.findMedianSortedArrays([1, 3], [2]))
# TC: log(min(m,n))
# SC: O(1)