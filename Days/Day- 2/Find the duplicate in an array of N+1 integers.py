# https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of integers nums containing n + 1 integers where each integer is in the range[1, n] inclusive. There is only one repeated number in nums, return this repeated number. You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1: Input: nums = [1, 3, 4, 2, 2] Output: 2

# Example 2: Input: nums = [3, 1, 3, 4, 2] Output: 3

# Constraints:
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
# -------------------------------------------------------------------------------------------------------------------------------------------

# Approach1: My Original Idea - Find max number in the array and make a hashmap of that size with all 0s. Traverse the given array and for each item of array, at that index in hashmap, store a count of 1, initially. Now as count is again detected on that index return that element as repeated.
from typing import List

"""class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap=[0]*(max(nums)+1) # We have to do +1 in hashmap as even that could be a value and so we might have to store a count there as well.
        for i in (nums):
            if hashmap[i]==0:
                hashmap[i]=1
            elif hashmap[i]==1:
                print(i)
                return i

S=Solution()
S.findDuplicate([1,3,4,2,2])
S.findDuplicate([3,1,3,4,2])"""


# Time Complexity:O(2n). Explanation: n time to find max, n time to store 0s in hashmap and traverse the nums.
# Alternate for decreasing Time Complexity: Instead of finding max, as constraint says if size of array is n+1, then max element could be only n, hence we can directly make a hashmap of [0]*[len(arr)-1]. This would give us total Time Complexity of the approach as O(n).
# Space Complexity:O(n). Explanation: for creating a hashmap we took n+1 0s. Considering +1 as constant, Space Complexity=O(n).
# Note: Here in constraints if 1 <= nums[i] <= n was not given but if it instead was 1<=nums[i]<n^2, then we'll use not an array but perhaps a dictionary as hashmap and in that case too the space complexity would become O(n), which otherwise could become O(n^2).

# Approach2:Use 2 for loop and check all possibility. With first for loop on one item, use 2nd for loop to traverse through all the items after that. If any item matches with the selected item of first for loop, return the item.
# Time Complexity: O(n(n+1)/2).
# Space Complexity: O(1).

# Approach3: Merge sort the array. Traverse and check with just the previous index's item, if they match return them.
# Time Complexity: O(nlogn+n). Explanation: nlogn time for merge sort and then n time to traverse the sorted array.
# Space Complexity: O(1).

# Approach4: Better Time and Space Complexity
# Tortoise hayer algorithm: For the given constraints that an array is of size n+1 and the possible values at each index are from 1 to n, we can safely say that atleast one element has to repeat, becuse say if array is of size 6 then all possible value could be just 1,2,3,4,5 & so to make up for 6 items one value would've to be repeated. In this approach we will use the concept of building a linked list. By starting from the value of elem at 0th index, we'll start the traversal by moving to that index and checking it's value, and further moving to that index. We'll take two pointer Slow(tortoise) and fast(hayer), which'll move for one and two elements respectively at each step. We'll keep traversing in the array until fast and slow pointer meets. As that happens, we'll shift fast pointer to the starting and will now move slow and fast pointer by one position each, on every step, untill they coincide again. This point where they coincide will be the repeating element.
# Note: Observe how all the elements are lesser than length of array and that zero is not a possible value here. If 0 was also said as a possible elem then our algo could fail as: we could start from 0th index and if a zero is present there, then that'll make a loop from 0 to 0, thereby preventing visit to any other array items and thus failing our algo. On contrary consider 2 to be present at index 2, then starting the traversal from 0th index, to visit the index 2 there should be a 2 value stored at some other index too or else we'll never happen to hop to index 2. Thus that'll not prevent us from visiting no other element except itself, as was the case with 0. Also see how from constraints it is apparent that there can not be a case where [1,2,6] could be the given array, where if we reach to value 6 and try looking for an element at that index, we cant find anything.
# This algo also works because, only one element is given as would be repeating (in question). Basically as we are bound to have a repeating number for this question, and all the given numbers are between 1 and n for an array of size n+1, we can say that in the linkedlist representation showing array items by following index traversal, our array will form a loop as the repeating number would be stored at atleast 2 different indices and hence while traversal, from two places we'll get the same element. As this loop is formed, the starting point of loop is the repeating number, because that is being pointed from atleast 2 different indices. For eg: for [3,4,1,4,2], we can see that 4 is present at index 3 and 1 and so by forming a linked list, we will get 4 pointed twice. Now all the struggle is to find the starting point of loop. The tortoise hayer has proof to be able to find it which can be found here https://www.youtube.com/watch?v=PvrxZaH_eZ4&ab_channel=Insidecode. Hence by tortoise hayer we're just finding the starting point of the loop in our linked list.
# 3->4->2 ->1
#    |      |
#    <--- <---
class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow


S = Solution()
print(S.findDuplicate([4, 1, 4, 3, 2, 4]))
# Time Complexity: O(n). Explaination: May be in first while it could take 2 times the n iterations i.e.twice after traversing the loop/array, our pointers meet. So we can represent the first while loop's time complexity as ln where l could be a constant. The second while is executed after completion of first one. The second one will at max take n iterations. So in total time complexity could be generalized and represented in terms of O(n).
# Space Complexity: O(1). Explaination: IN total, there are only 2 variables which are used here. At any given time both of them: fast and slow will only hold single value. Hence we can consider there space usage as constant.
