# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Check Day18/LevelOrderTraversal.py coz here it is the exact same thing with a difference that initially assigned 0 is a flag variable that we use extra here. 0 denotes whether left to right the level has to be written, and 1 denoted right to left. So on this basis here we do `resArr.append(temp)` or `resArr.append(temp[::-1])` and accordingly toggle flag after each level
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return

        resArr, queue = [], Queue()
        queue.put(root)
        flag=0
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
            if flag==0:
                resArr.append(temp)
                flag=1
            else:
                resArr.append(temp[::-1])
                flag=0
        return resArr
# TC: O(n)
# SC: O(n)