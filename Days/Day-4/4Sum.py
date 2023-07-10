# https://leetcode.com/problems/4sum/

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# Example 2:
# Input: nums = [2, 2, 2, 2, 2], target = 8
# Output: [[2, 2, 2, 2]]

# Constraints:
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# -------------------------------------------------------------------------------------------------------------------------
# Approach1: Using 4 for loops to check all the combinations, and see if the target is achieved from the addition from values of respective for loops. If so, we'll insert all such combinations into a Set. We use set here as only unique combinations should be printed and also, the order of the items dont matter. Further, as we have to return an array, we'll make a list of lists from set.
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ansArr = set()  # Set is like: (), just as tuple is. But to define an empty Set syntax is Set = set(). Defining tuple would be like tup = (). Here we use set so same sub-items won't be repeated stored such as [[2,2,2,2],[ 2,2,2,2]]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            # Sort the tuple before adding it to the set
                            ansArr.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))  # sub-items such as [1,0,-1,2] are considered different than [-1,2,1,0] and as only arrays can be sorted, we first make an array of new item and sort it. Now array being mutable cant be stored in set which is immutable data type. So we convert it into tuple
        return [list(i) for i in ansArr]


# S=Solution()
# S.fourSum([1, 0, -1, 0, -2, 2],0)
# S.fourSum([2, 2, 2, 2, 2],8)
# Time Complexity: O(n^5logn + n). Explanation: 4 for loops taking n^4 time to fill the set. Inside innermost for, we sort elems which takes nlogn. Further 1 for loop to convert set into array while returning.
# Space Complexity: O(n). Explanation: Extra space for set, to store n elements.


# Approach2: Better Time Complexity - Reducing 1 of 4 for Loops by using a dictionary hashmap to store elems as we did in 2-Pointers. Also instead of sorting all the quadrepels, we can just for once sort the given array itself. This'll help in reducing many sorting attempts otherwise with quadrepels.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() #just sort given array. Now our quadrepels could repeat but not like [1,0,-1,2] and [-1,2,1,0], but instead like [1,0,-1,2] and [1,0,-1,2] in case of which set will automatically discard
        ansArr = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                hashmap = {}  # So with every new iteration of j, previously stored k value's are gone
                for k in range(j + 1, len(nums)):
                    fourthElem = target - (nums[i] + nums[j] + nums[k])
                    if fourthElem in hashmap:  # lookup in dictionary keys take O(1)
                        ansArr.add(tuple((nums[i], nums[j], nums[k], fourthElem)))
                    else:
                        hashmap[nums[k]] = True
        return [list(i) for i in ansArr]


# S = Solution()
# S.fourSum([1, 0, -1, 0, -2, 2], 0)
# S.fourSum([2, 2, 2, 2, 2], 8)
# Time Complexity: O(n^3 + n + nlogn) Explaination: nlogn for sorting given array (from using merge sort). Plus n^3 from using three nested for loops: n^3. Later n time to convert set into list for returning
# Space Complexity: O(2n) Explanation: n space for set and n for hashmap i.e. 2n => Generalized as n


# Approach3: Reducing 2 of 4 for loops by using 2 extra pointers. Sort the array. In sorted array, we use 2 for loops and in the range later than what is pointed by second loop, we'll use one pointer at starting and one at ending. We'll look for target element and see if the sum of elems pointed by two for loops and elems pointed by two pointers is equal to the target. If sum is equal to target, we'll add corresponding values in output list. If not and if target is higher than sum, then as array is sorted, we'll shift startPointer to right by one and we'll check again if target is now equal to the new sum. On the other hand if we find target being smaller than sum, we'll shift ending pointer to left by one. We'll keep on shifting pointer's till start<end.
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        helperVar = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, u = j + 1, len(nums) - 1
                reqSum = target - nums[i] - nums[j]
                while l < u:
                    if nums[l] + nums[u] == reqSum:
                        helperVar.add(tuple((nums[i], nums[j], nums[l], nums[u])))
                        l+=1
                    elif nums[l] + nums[u] < reqSum:
                        l += 1
                    else:
                        u -= 1
        return [list(i) for i in helperVar]


S = Solution()
print(S.fourSum([1, 0, -1, 0, -2, 2], 0))
# Time Complexity: O(n^3+nlogn+n) Explanation: nlogn for sorting given array (from using merge sort). Two nested for loops take n^2 time in total. In second for loop, we have a while loop, which will traverse the rest-of the portion from what's pointed by 2nd for loop. This while loop should be check ofcourse less than n elements in any given iterations, but for worst case and taking the bigger round figure we can say while takes n time. Therefor inside each iteration of n^2, we are taking n time more. Later n time to convert set into list for returning
# Space Complexity: O(n) Explanation: only set variable consumes extra n space
