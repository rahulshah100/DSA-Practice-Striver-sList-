# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

# Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.
#
# Left view of following tree is 1 2 4 8.
#
#           1
#        /     \
#      2        3
#    /    \    /  \
#   4     5   6    7
#    \
#      8
#
# Example 1:
# Input:
#    1
#  /  \
# 3    2
# Output: 1 3
#
# Example 2:
# Input:
# Output: 10 20 40
# Your Task:
# You just have to complete the function leftView() that returns an array containing the nodes that are in the left view. The newline is automatically appended by the driver code.
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).
#
# Constraints:
# 0 <= Number of nodes <= 100
# 1 <= Data of a node <= 1000
# ------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: For Left View we'll follow the depth traversal of given tree where we keep visiting left item of given node starting from root, up-till the left item is encountered as 0. While undergoing this traversal we'll also keep storing the values of these nodes, into an array called resArr which is returned at the end. Thus having complete left branch we started with right item and go in further of its left but here we face an issue of not knowing whether the node we're traversing appears at the face of Binary tree from left side. Consider below example:
#           1
#        /     \
#      2        3
#    /    \    /  \
#   4     5   6    7
#    \
#     8
# We start at 1, store it and go-to left and store 2 and then 4. 4 doesn't have a left so we go-to right and store 8. Thus, when exhausted the parent call of 4 yields as the result of its parent i.e. 2's left call, and we further go to 2's right i.e. 5. Here we face difficulty of not knowing whether this is part of left view or coming behind after a veil of left nodes.
# To handle this challenge we introduce concept of level; like 1 is on level 0; 2 and 3 are on level 1; then 4,5,6,7 are on level 2, and 8 is on level3. So for traversal we'll use a subFunction where levels are passed as a function param and incremented with every left or right call. How we use it to identify if current item is part of left view based on existing number of items already stored items in resArr at that point. So first subFunction call will have item, level params as 1,0. Here we check if len(resArr) == level i.e. 0 === 0 and as it matches we add 1 into resArr. Thus, further for 2,1  len(resArr)=>1 === level and so we add 2 in resArr. For 4 we have level=2 and resArr=[1,2] so len(resArr) == level, and we add 4 into resArr. For 8 again len(resArr) == level == 3 and 8 is added. Thus following when 5 is encountered where if it was supposed to be added there mustn't have been a lefter item and so when there and because we've traversed since top, we should only have numOfItemsInResArr==LevelOf5 which wont be true and so we wont store it.

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def LeftView(root):
    resArr = []

    def helperFunc(node, level):
        if not node:
            return

        if len(resArr) == level:
            resArr.append(node.data)
        helperFunc(node.left, level + 1)  #To obtain right view we'll just swap this line with next below and rest stays same
        helperFunc(node.right, level + 1)

    helperFunc(root, 0)
    return resArr
# TC: O(n)
# SC: O(n) Explanation: Auxiliary space in worst case