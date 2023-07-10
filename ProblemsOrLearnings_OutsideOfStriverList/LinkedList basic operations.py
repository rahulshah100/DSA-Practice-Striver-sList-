import math

class Node:
    def __init__(self, val): # __init__ is constructor method of the Class    #here self represents the object class which gets by default passed in class & all it's methods as they're invoked by the class' object
        self.value = val #above seen param- 'val' is called formal param while where this function/method is called, the variable passed is called actual param.  #associating self and thus re-instiating passed params ensures that variables passed in constructor could be accessed not just within this one method i.e. __init__ but throughout all the methods in this class
        self.next = None #By default next pointer will be None


class LinkedList:
    def __init__(self):
        self.head = None #By default head points to None i.e. an empty LL

    # Adds new node at front
    def push(self, new_val):
        new_node = Node(new_val) #Creates New Node with the designated value
        new_node.next = self.head #Set New Node's Next to where head is pointing i.e. at front
        self.head = new_node #Head points to this new node

    def insert_after(self, ref_node, val):
        if ref_node is None:
            return
        new_node = Node(val)
        new_node.next = ref_node.next
        ref_node.next = new_node

    def insert_at_end(self, new_val):
        new_node = Node(new_val)

        # If empty linked list is given
        if self.head is None:
            self.head = new_node
            return

        # Traversing the given LL to reach the end
        ref_node = self.head
        while ref_node.next:
            ref_node = ref_node.next
        ref_node.next = new_node

    def delete_key(self, key):
        temp = self.head

        # Checking if the key to be deleted is at the head
        if temp is not None: #pre-requisite condition
            if temp.value == key:
                self.head = temp.next #head points to next elem
                temp = None #and the current elem is removed/made None
                return

        # If the key isn't at the head
        # TRICK -> Assign first, check later. If check yields True, break and don't update.
        while temp is not None:
            if temp.value == key:
                break
            prev_node = temp #We're tracking temp so in case key is found as seen below we make prev's next as temp's next and temp is made None
            temp = temp.next

        # If key isn't present in the linked list
        if temp is None:
            print("\nInvalid Entry! ")
            return

        prev_node.next = temp.next
        temp = None

    # Delete the first occurrence
    def delete_key_using_dummy(self,key):
        dummy_head = Node(-math.inf)
        dummy_head.next = self.head
        curr_node = dummy_head

        while curr_node.next is not None:
            if curr_node.next.value == key:
                curr_node.next = curr_node.next.next
                break
            else:
                curr_node = curr_node.next
        self.head= dummy_head.next

    def delete_all_occurrences(self,key):
        dummy_head = Node(-math.inf) #We entered arbitary val so it acts as a placeholder value and will not match any valid value in the list
        dummy_head.next = self.head  #Dummy's next is head/starting of list
        curr_node = dummy_head

        while curr_node.next is not None:
            if curr_node.next.value == key:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        self.head= dummy_head.next

    def print_linked_list(self):
        if self.head is None:
            return ""

        node = self.head
        while node:
            print(node.value, end = "   ")
            node = node.next

    def length(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def search_key(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.value == key:
                return True
            else:
                curr_node = curr_node.next
        return False

    def search_key_recursive(self, node, key):
        if not node:
            return
        if node.value == key:
            return True
        return self.search_key_recursive(node.next,key)

    def get_at_index(self, index):
        curr_node = self.head
        if index > self.length() - 1:
            return -1
        for i in range(index):
            if curr_node:
                curr_node = curr_node.next
        return curr_node.value

    def n_from_end(self, n):
        curr_node = self.head
        if n > self.length():
            return -1
        index = self.length() - n
        for i in range(index):
            if curr_node:
                curr_node = curr_node.next
        return curr_node.value

    def n_from_end_runner(self, n):
        p1 , p2, count = self.head, self.head, 0
        if self.head is not None:
            while count < n: #by using 2 pointers and increasing one of them to just one less than n, we are making sure to have fixed distance of n-1 between the pointers
                if p2 is None:
                    return -1
                p2 = p2.next
                count += 1

        while p2 is not None:
            p1 = p1.next
            p2 = p2.next
        return p1.value

    def middle_val(self):
        p1, p2 = self.head, self.head
        if self.head:
            while p2 and p2.next:
                p1 = p1.next
                p2 = p2.next.next
        return p1.value

    def count_repetition(self, key):
        curr_node, count = self.head, 0
        while curr_node:
            if curr_node.value == key:
                count += 1
            curr_node = curr_node.next
        return count

    def detect_loop_hm(self):
        S, curr_node = set(), self.head
        while curr_node:
            if curr_node in S:
                return True
            S.add(curr_node)
            curr_node = curr_node.next
        return False

    # Floyd's Cycle Finding Algorithm
    def find_cycle(self):
        p1, p2 = self.head, self.head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

    def reverse_linked_list(self):
        curr_node, prev, next = self.head, None, None
        while curr_node:
            # Making changes to the node
            next = curr_node.next
            curr_node.next = prev

            # Traversing through the Linked List
            prev = curr_node
            curr_node = next
        self.head = prev



if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.insert_at_end(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.insert_at_end(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insert_after(llist.head.next, 8)

    print('Created linked list is:')
    llist.print_linked_list()

    # llist.delete_key(4)
    llist.delete_key_using_dummy(4)
    llist.delete_key_using_dummy(4)

    print('\nUpdated linked list is:')
    llist.print_linked_list()

    print('\nlength is : ')
    print(llist.length())

    llist.delete_all_occurrences(4)

    print('\nUpdated linked list is:')
    llist.print_linked_list()

    print("\n\nIterative Search")
    print(llist.search_key(7))

    print("\nRecursive Search ")
    print(llist.search_key_recursive(llist.head,7))

    print("\n Search at Index")
    print(llist.get_at_index(4))

    print("\n Search from end")
    print(llist.n_from_end(2))

    print("\n Search from end via Runner technique")
    print(llist.n_from_end_runner(2))

    print("\n Print the middle value of the linked list")
    print(llist.middle_val())

    print("\n Count repetition of given key")
    print(llist.count_repetition(7))

    print("\nDetect Cycles")
    print(llist.detect_loop_hm())

    llist2 = LinkedList()
    llist2.push(20)
    llist2.push(4)
    llist2.push(15)
    llist2.push(10)
    # Creating a loop for testing
    llist2.head.next.next.next.next = llist2.head

    print("\nDetect Cycles")
    print(llist2.detect_loop_hm())

    print("\nFloyd's Cycle Finding Algo Implementation")
    print(llist2.find_cycle())

    llist.reverse_linked_list()
    print("\nReversed Linked List")
    llist.print_linked_list()