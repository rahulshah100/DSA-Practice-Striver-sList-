# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Given the root of a binary tree, calculate the vertical order traversal of the binary tree. For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values. Return the vertical order traversal of the binary tree.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.

# Example 2:
# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
#           1 is at the top, so it comes first.
#           5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.

# Example 3:
# Input: root = [1,2,3,4,6,5,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# This case is the exact same as example 2, but with nodes 5 and 6 swapped.
# Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: To gain full control of ordering nodes, we mark every node with its vertical i.e. y and level i.e. x-axis coordinate. So 1 will be (0,0) 2 will be (-1,1) 3 will be (1,1) and 4 will be (-2,2) 10 will be (0,2) 5 will be (0,2) 10 will be (2,2). Further we use level order traversal so the order of visiting nodes will be like 1, then 2,3 then 4,10 and then 5,10. To make this traversal possible we'll use a queue DataStructure and traverse till it is not empty. While thus visiting we'll store items in a mapDataStructure called nodes where against the vertical coordinate as key we store the value which is a map. This value that's a map stores levelCoord as key, and an array of value of nodes is stored. So for 10,5 which are at the bottom center what'll happen is it will be stored as {0: {2: [10,5]}}. Now this is primarily important because as we see for same level and vertical coord we can have multiple items in which case as mentioned in question we'll have to store them in sorted order. So our task is thus made easier that at end of level order traversal nodes Data Structure could be visited in order of its sorted keys so like (-2: 4), (-1: 2), (0: 1,10,5), (1: 3), (2: 10) are visited in this order, and for (1,10,5) actually it'd be (0:1), (2: 10,5) so we visit them in sorted keys and thus when coming across 2 we find array we sort the array and insert these all node Values into an resArr array that gets returned once filled. Thus, preference of left to right and in that top-to-bottom and in which at the same coord ascending order of item values are thus maintained. Also, while traversing which is done using queue, so that we have access to all the pieces of info i.e.(node, vertical and level coord) which we want to store in nodes DataStructure we'll have to make them available to Queue as well so that nodes can fetch it from there. Hence, in Queue we store items in the format - node, (verticalCoord, levelCoord). We store it like this so that popping node from Queue is easier while traversing.
#         1
#       /   \
#     2      3
#    /  \   /  \
#   4   10 5   10
from queue import Queue
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = {}
        queue = Queue()

        queue.put((root, (0, 0)))  # initial vertical and level
        while len(queue.queue):
            temp, (x, y) = queue.get()
            if x not in nodes:
                nodes[x] = {}
            if y not in nodes[x]:
                nodes[x][y] = []
            nodes[x][y].append(temp.val)  # inserting into set

            if temp.left:
                queue.put((temp.left, (x - 1, y + 1)))
            if temp.right:
                queue.put((temp.right, (x + 1, y + 1)))

        resArr = []
        for p in sorted(nodes): #sorted will sort items of map in ascending order on basis of keys
            temp = []
            for q in sorted(nodes[p]):
                temp.extend(sorted(nodes[p][q]))
            resArr.append(temp)

        return resArr


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(10)
root.left.left.right = TreeNode(5)
root.left.left.right.right = TreeNode(6)
root.right = TreeNode(3)
root.right.left = TreeNode(9)
root.right.right = TreeNode(10)

S = Solution()
print(S.verticalTraversal(root))
# TC: O(n + nlogn*nlogn*nlogn)   Explanation: n for level order traversal. Then nlogn for sorting the key-values in nodes where key will be verticalCoord. Further the values are maps with keys as levelOrderCoord that has to be sorted again on basis of keys and that takes nlogn. This subMaps value is array that again has to be sorted which takes nlogn.
# SC: O(6n) Explanation: Roughly the main space is used by queue and node which are both storing 3 pieces of info. At worst they'll have 3 pieces of info to be stored for all n nodes hence collectively as both will store 3n, we need 6n space.