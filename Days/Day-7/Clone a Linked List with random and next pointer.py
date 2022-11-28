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
# Approach1: Using Hashmap. We traverse through the given linked list and for each node encountered, we'll create a new node by creating a new Node Object which has the travesed node's value. We will store the new node in a dictionary hashmap with key as the traversed node and value as a newly created node. As new nodes are all created, we'll go through given linked list again and will form next and random pointer connection. For doing this we will look up the value of key=traversedNode in hashmap. For this node we will set it's next and random by connecting them with the node in the hashmap for whom key=traverseNode'sNext and key=traversedNode'sRandom respectively. Ultimately, we will return the first node of Newly made and connected node's by returning value from hashmap for which key=head.
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
            dict[temp1]=Node(temp1.val)
            temp1=temp1.next
        dict[None]=None #For below line --1 when temp2.next becomes None, dict[temp2.random] should have a dict[None] stored in hashmap, which we're here doing seperately like this
        while temp2:
            dict[temp2].next=dict[temp2.next] #--1
            dict[temp2].random=dict[temp2.random]
            temp2=temp2.next
        return dict[head]
# TC: O(2n) Explanation: n for forming hashmap and n for connecting the node's random and next pointers in the hashmap. Note: here we're assuming the lookup time in hashmap dictionary for nodes as the key is O(1) or that time would be added.
# SC: O(n) Explanation: n space used in hashmap for storing keys and n space for storing values. Total of 2n space can be generalised as n.

# Approach2: To eliminate extra n space, we'll not use hashmap, which will mean we will not store the nodes but will keep creating and adding them directly in our main linked list. So we will make a new node with value of node1 from given list, and will get this new node pointed from the next pointer of node1 from the given list. Further this node's next will point to where in original list node1 one was pointing i.e.node2 in the given list. So on, we'll create new nodes for all nodes in given linked list and will put them in between the node they're based from in the given list and the next node in the given list. After this much, we will traverse the given list again and will set the random pointers appropriately for this new set of nodes. Further once more we will traverse the given list, this time detangle next pointers of both given and new nodes.
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

        # Making new nodes' random point appropriately
        temp = head
        while temp:
            if temp.random:  # If temp.random is None in below line temp.random.next will be None.next which will give error.
                temp.next.random = temp.random.next  # On RHS temp.random will given node that original list's node is pointing, by adding a .next to it we'll get the node that is equivalent to the random pointed by newly created node
            temp = temp.next.next

        # Detangle the next pointers of new and given nodes
        temp = head
        dummy = Node(0)
        newList = dummy
        while temp:
            dummy.next = temp.next
            dummy = dummy.next
            temp.next = dummy.next
            temp = temp.next
        print(newList)
        return newList.next
# TC: O(3n) Explanation: n time for traversing to create nodes and add them in the main list + n time to traverse to make random pointers point appropriately in new nodes + n time to traverse for making next pointer appropriate in original and new linked list. Total of 3n, which would be expressed as O(n).
# SC: O(1) Explanation: although we created n new nodes, but then as in question deep copy is mentioned, hence it is given that afresh/totallyDifferentThanGivenNodesOfGivenLinkedList are to be formed and so n extra nodes are to be inevitably created, which makes the n space taken here justified. In approach1 we had to hold them in hashmap before we formed their pair, so pair was justified space, but for having that when earlier they were stored in hashmap for that interim time creates extra space usage of n.