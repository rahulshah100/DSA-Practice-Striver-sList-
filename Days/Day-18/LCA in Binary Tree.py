# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# --------------------------------------------------------------------------------------------------------------------------------------
# Approach1: While traversing inOrder in the given Binary tree when currently traversed node matches with either p or q we return that call from there itself. This could hold for one of two cases where further below the returned call say we were to encounter the other target node like for below tree say p=2, q=4 so when p=2 is encountered, and we return, 4 never is reached to, and we directly go to 2's parent's right call. This was case1, and case2 is where the returned call doesn't overshadow the other target node. Example of case2 is p=2 q=9 so when inOrder first encounters 2 and returns we still go to 2's parent's right i.e. 3 where we go to 3's left and then right and thus also encounter 9 which is the second target node. Further building the logic when a value gets returned, and it is not None we know down that line we have found either/both target node, and we'd wanna return that value up the calls as it is coming from lower levels which is in-line with question requirement of Lowest Common Ancestor. To achieve this the base case of `if not root: return` is modified to `if not root or root == p or root == q: return root`. Now as values are bumping up through the calls, for case1 where p=2, and q=4 when 4 is returned to node2 and then node1 and at node1 the right call will return None, we have a case of choosing what to return for output between a number and None which is quite understandable that we shall return number. Hence, left and right call are assigned to a variable so the return values can be thus preserved and once we have both return values i.e. of right and left call we put if calls to check if left call's return is None in which case we return right's returned value and vice versa. But for case2 where both calls returns values, the common ancestor is the current Node where these returned values are obtained for first time like the earlier used example of case2 is p=2,q=9 where 2 returns as left of 1 and 3 will return 9 to 1's right. Thus 1 is where left and right calls are non-none and that's the case where we return the currNode itself.
#     1
#    / \
#   2   3
#  / \   \
# 4   5   9
# \
#  11
"""
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # base case
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # result
        if left is None:
            return right
        elif right is None:
            return left
        else:  # both left and right are not None, we found our result
            return root
"""
# TC:O(n)
# SC:O(n)