# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# -----------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using queue that is filled with one item i.e. root, we traverse till queue is emptied out. In the queue we register the length of queue so the existing level's size gets locked, say it is done using a variable queueSize. Also, here we declare a temp variable as an empty array. Now for this queueSize we run a for-loop to pop queue items from bottom and append it in temp array. Temp array will thus hold all the items of same level by the end of for-loop. queue is further appended with popped's left and right. Thus completing the for-loop we store the temp in resArr. resArr is returned at the end
from queue import Queue
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return #Note: Constraints of question says tree size can be 0, hence if we dont put the `if not root: return` then currNode.val gives Error

        resArr, queue = [], Queue()
        queue.put(root)
        while len(queue.queue):
            queueSize = queue.qsize()
            temp = []

            for i in range(queueSize):
                currNode = queue.get()
                temp.append(currNode.val)
                if currNode.left:
                    queue.put(currNode.left)
                if currNode.right:
                    queue.put(currNode.right)
            resArr.append(temp)
        return resArr

# Example usage:
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(9)

S = Solution()
print(S.levelOrder(root1))
# TC: O(n) Explanation: For traversing n nodes simply n time is taken here
# SC: O(n) Explanation: Queue can take n space in worst case