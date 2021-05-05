"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
from objectives import add_to_head, add_to_tail, add_to_next, print_list

class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    curr_node = head_of_list
    prev_node = None
    next_node = curr_node.next

    while curr_node is not None:
        # point current node backwards
        curr_node.next = prev_node

        # move all the pointers forward
        prev_node = curr_node
        curr_node = next_node
        if curr_node is not None: 
            next_node = curr_node.next

    return prev_node

linked_list = LinkedListNode(3)
tail = linked_list

linked_list = add_to_head(linked_list, 2)
linked_list = add_to_head(linked_list, 5)
middle = linked_list
linked_list = add_to_head(linked_list, 6)
linked_list = add_to_head(linked_list, 0)

tail = add_to_tail(tail, 12)
add_to_next(middle, 7)

print_list(linked_list)
linked_list = reverse(linked_list)
print("-------------")
print_list(linked_list)