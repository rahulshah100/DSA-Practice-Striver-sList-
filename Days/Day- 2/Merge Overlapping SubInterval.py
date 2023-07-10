# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non - overlapping intervals that cover all the intervals in the input.

# Example 1: Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]] Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals[1, 3] and [2, 6] overlap, merge them into[1, 6].

# Example 2: Input: intervals = [[1, 4], [4, 5]] Output: [[1, 5]]
# Explanation: Intervals[1, 4] and [4, 5] are considered overlapping.

# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Brute Force - Use 2 for loops, first for pointing at one item at a time and second to compare the value of item selected by first for loop with every item after it. If merge conditions are met then we'll change 0th and 1st index of item where j is pointing and we'll make the item pointed by i as None. Skipping further operations for that i we'll increment i. After completing one such traversal, we'll return an array of items from our obtained array, which are not None, by using:  return [a for a in intervals if a].
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i]==None:
                    break
                elif intervals[j]!= None and intervals[j][0] <= intervals[i][1]:
                    intervals[i][1] = max(intervals[j][1], intervals[i][1])
                    intervals[j] = None
        print([i for i in intervals if i])
        return [i for i in intervals if i]
"""
# Time Complexity: O(n^2). Explanation: Array traversal to merge and mark None takes n(n+1)/2 i.e.n^2 and then for returning only not None, we'll again traverse the array, hence n time there. Considering bigger term we can write time complexity as O(n^2).
# Space Complexity: O(1)


# Approach2: Merge sort to sort all items based on their starting values. Further we will use 2 pointers lower, and higher pointing at first two consecutive items in the sorted array. If 1st item's 1st index is greater than 2nd item's 0th index and if 2nd item's 1st index is greater than 1st item's 0th index, then we'll make 1st item's 1st index equals to 2nd item's 1st index and delete 2nd item, increasing both lower and higher pointer by 1. If 1st item's 1st index is greater than 2nd item's 0th index but not less than 2nd's 1st index than we'll delete the 2nd item. If 1st item's 1st index is not greater than 2nd item's 0th index, then we'll just increase lower, higher. We'll keep on repeating the process till higherPointer is pointing to last item or is somewhere before that.
from typing import List

"""class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting on the basis of starting value of each item:
        # Consider we used MergeSort for sorting. We'll see how merge sort could be used for sorting in Inversion of Array.py which is in this same Folder. Hence for now, we just accept that the below .sort is MergeSort and that it took nlogn time from us with no extra space requirements, as that is how merge sort works.
        intervals.sort(key=lambda x: x[0])

        # Checking overlapping and merging intervals
        lowerPointerIndex=0
        higherPointerIndex=1
        while higherPointerIndex<len(intervals):
            if intervals[lowerPointerIndex][1]>=intervals[higherPointerIndex][0]:
                if intervals[lowerPointerIndex][1]<=intervals[higherPointerIndex][1]:
                    intervals[lowerPointerIndex][1]=intervals[higherPointerIndex][1]
                    del intervals[higherPointerIndex] #Here we could have written higherPointerIndex+=1 and then use a new array say arrNew,& here, write arrNew.append(intervals[lowerPointerIndex]). But that'll increase the Space Complexity.
                else:
                    del intervals[higherPointerIndex]
            else:
                lowerPointerIndex+=1
                higherPointerIndex+=1
        print('intervals', intervals)
        return intervals

S=Solution()
# S.merge([[1,3],[2,6],[8,10],[15,18]])
# S.merge([[1,4],[4,5]])
# S.merge([[1,4],[0,4]])
# S.merge([[1,4],[2,3]])
S.merge([[1,4],[2,3],[1,5]])"""
# Time Complexity: O(nlogn). Explaination: nlogn for sort and n for checking overlapping and merging, so considering greater time complexity, we can generalize here and write Time complexity to be nlogn.
# Space Complexity: O(1)


# Approach2: Just more decent Representation than Approach1, otherwise same concept and time, space complexities
"""class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i-1][1]>=intervals[i][0]: #Here = is important
                intervals[i][0]=intervals[i-1][0]
                intervals[i][1]=max(intervals[i-1][1], intervals[i][1])
                intervals[i-1]=None
        print([i for i in intervals if i])
        return [i for i in intervals if i]

S=Solution() 
print(S.merge([[1,3],[2,6],[8,10],[15,18]]))"""