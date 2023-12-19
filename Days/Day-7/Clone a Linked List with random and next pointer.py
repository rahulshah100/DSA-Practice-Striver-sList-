# https://leetcode.com/problems/copy-list-with-random-pointer/

# Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Constraints:
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random is null or is pointing to some node in the linked list.
# ---------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using Hashmap. We will traverse through the given LL. With each iteration we'll store traversed node as hashmap's key and a new Node with traversed node's value as hashmap's value. After one such iteration we'll reiterate the given LL this time to form connections of next and random amongst the newly created nodes in hashmap. So traversed node as the key in dictionary, we'll set it's next and random as dictionary's value for traversed node's next and random. At the end return traversed node's value for head.
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp1=temp2=head
        dict={}
        while temp1:
            dict[temp1]=Node(temp1.val) #because Nodes are stored as keys so even if linked list has nodes with repeating values, as not values but Nodes are keys, we'll still have all nodes as unique keys here
            temp1=temp1.next

        dict[None]=None #For below line --1. As we're told random ponters could point to None in which case dict[None] would have to be available
        while temp2:
            dict[temp2].next=dict[temp2.next] #--1
            dict[temp2].random=dict[temp2.random]
            temp2=temp2.next
        return dict[head]
# TC: O(2n) Explanation: n for forming hashmap and n for connecting the node's random and next pointers in the hashmap. Note: here we're assuming the lookup time in hashmap dictionary for nodes as the key is O(1) or that time would be added.
# SC: O(n) Explanation: n space used in building hashmap, for which values are n newly created nodes. Thus total 2n space. But as deep copy is given in question n space i.e. for creating new nodes is expected, we mention SC to be O(n) only involving hashmap space


# Approach2: To eliminate extra n space, we'll not use a hashmap. But if we create new nodes seperately then as we have them created although we can keep connecting them with newer nodes and thus have their next pointer's sorted, but we'll possibly not be able to connect their random. This gives idea to accommodate the newly created nodes directly in our given linked list in between the existing nodes so to have some failiar structure that can be leveraged to connect random pointers of new nodes. First off we'll traverse the given LL, creating newNodes with values of the ones being traversed and store them between two Nodes of given LL. This will essentially weave new nodes alternately between the nodes of given LL. Further we'll traverse the updated LL to set the random pointers amongst the newNodes. For this part, traversed node's random will have it's next pointing to it's newly created replica node. At the end we have to de-tangle nexts of newNodes. Important part is detangling and removing next pointers should not be simultaneous or else say a next is removed now when current node's random's next is checked the new node has been disconnected, and we'll run into inconsistencies.
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head

        # Putting New Nodes in given linkedlist
        temp = head
        while temp:
            newNode = Node(temp.val)
            newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next

        # Making new node's random attribute to point appropriately
        temp = head
        while temp:
            if temp.random:  # If temp.random is None in below line temp.random.next will be None.next which will give error.
                temp.next.random = temp.random.next  # On RHS temp.random will given node that original list's node is pointing, by adding a .next to it we'll get the node that is equivalent to the random pointed by newly created node
            temp = temp.next.next

        # De-tangle the next pointers of new and given nodes
        temp = head
        newList = dummy = Node(0)
        while temp:
            dummy.next = temp.next
            dummy = dummy.next
            temp.next = dummy.next
            temp = temp.next
        return newList.next
# TC: O(n) Explanation: n time for first traversal to create and add nodes in the given LL + 2n (as nodes in given LL have doubled with addition of n new Nodes) time to traverse to adjust random pointers + n time to traverse for making next pointer appropriate in original and new linked list. Total of 4n, which would be expressed as O(n).
# SC: O(1) Explanation: although we created n new nodes, but then as in question deep copy is mentioned, hence it is given that afresh/totallyDifferentThanGivenNodesOfGivenLinkedList are to be formed and so n extra nodes are to be inevitably created, which makes the n space taken here justified. In approach1 we had to hold them in hashmap before we formed their pair, so pair was justified space, but for having that when earlier they were stored in hashmap for that interim time creates extra space usage of n.