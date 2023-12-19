# https://leetcode.com/problems/find-median-from-data-stream/

#  The median is the middle value in an ordered integer list.If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

#  For example, for arr =[2, 3, 4], the median is 3.
#  For example, for arr =[2, 3], the median is (2 + 3) / 2 = 2.5.

#  Implement the MedianFinder class:
#  MedianFinder() initializes the MedianFinder object.
#  void addNum(int num) adds the integer num from the data stream to the data structure.
#  double findMedian() returns the median of all elements so far.Answers within 10 - 5 of the actual answer will be accepted.

# Example 1:
# Input ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"] [[], [1], [2], [], [3], []] Output [null, null, null, 1.5, null, 2.0]
# Explanation MedianFinder medianFinder = new MedianFinder(); medianFinder.addNum(1); // arr = [1] medianFinder.addNum(2); // arr = [1, 2] medianFinder.findMedian(); // return 1.5(i.e., (1 + 2) / 2) medianFinder.addNum(3); // arr[1, 2, 3] medianFinder.findMedian(); // return 2.0

# Constraints:
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.

# Follow up: If all integer numbers from the stream are in the range[0, 100], how would you optimize your solution? If 99 % of all integer numbers from the stream are in the range[0, 100], how would you optimize your solution?
# --------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Simple sorting as we add item everytime in addNum function, and in findMedian finding average or returning middle items depending on whether array length is an odd or an even number
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()

    def findMedian(self) -> float:
        if len(self.data) % 2 != 0:
            return self.data[len(self.data) // 2]
        else:
            return ((self.data[len(self.data) // 2] + self.data[(len(self.data) // 2) - 1]) / 2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# TC: O(n(nlogn)) Explanation: If n instructions of addNum are given then in that worst case we'll take nlogn time for sorting every time, for n times
# SC: O(n) Explanation: To store n items in data array


# Approach 2: We can think of balancing the incoming data-stream in real-time as they arrive by using maxHeap and minHeap which will store first and second half of the array of incoming data, relatively. Consider total data as 1,17,16,18,9,3,4,2; it's sorted version is 1,2,3,4,9,16,17,18, where median is (4+9)/2. Reason for specifically storing the first half in maxHeap is that we'll have sort of (sort-of because heap just has fixed top but rest might not exactly be sorted) like [4,3,2,1] as our maxHeap, and second half which is minHeap will be sort of like [9,17,18,16]. Thus, at the end if we check length of both array, and we find them equal we can simply pop top items from both return their average as median. In case items are unequal, from the longer array we'll pop and return its top. As data keeps being received we keep balancing it between both heaps by essentially 3 conditions 1)At start when both arrays are empty we'll simply handle this case by adding the item in maxHeap (trivial idea to resolve situation, it could be the other way around too in which case 2nd point we'll read further would be adjusted accordingly). 2)If the incoming item is smaller than top of maxHeap, we'll add this item into maxHeap; else we'll add it into minHeap. This is especially important to add item in maxHeap if item is smaller than top of maxHeap coz say in array such as 19,1,1,9,3,4,2 if 19 gets added into maxHeap than by the virtue of the next point i.e. below given 3)rd point we'll shift it to minHeap as more items get added into maxHeap
# 3)In case the difference in length of both heaps is 2, we remove top item from corresponding longer heap and push it into the other heap thus ensuring balance in items
import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0:
            self.maxHeap.append(-num)
        elif num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) - len(self.minHeap) == 2:
            heapq.heappush(self.minHeap, -(heapq.heappop(self.maxHeap)))
        elif len(self.minHeap) - len(self.maxHeap) == 2:
            heapq.heappush(self.maxHeap, -(heapq.heappop(self.minHeap)))

    def findMedian(self) -> float:
        num1 = -self.maxHeap[0] if len(self.maxHeap) else 0.0 #if-condition used so we wont access 0th index of empty array which gives error
        num2 = self.minHeap[0] if len(self.minHeap) else 0.0
        if len(self.maxHeap) == len(self.minHeap):
            return (num1 + num2) / 2
        else:
            if len(self.maxHeap) > len(self.minHeap):
                return num1
            else:
                return num2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# TC: O(2nlogn) Explanation: for n operations we'd each time either heappush it in minHeap or maxHeap and in worst case for all n we'll also have to heappop them which means 2logn Time for n such iterations. Besides it, we dont utilize any more time.
# SC: O(n) Explanation: for n operations maxHeap or minHeap would either store the value and thus collectively the extra 2 arrays we used will occupy only n Space
