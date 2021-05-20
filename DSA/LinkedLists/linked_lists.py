"""
We will be creating singly linked lists with one head, one node and one tail.
SLL - is abbreviated as Singly Linked List
"""


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insertion in singly linked list
    def insert_singly_linked_list(self, value, location):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node  # By doing this we are adding the first node in our SLL
        else:
            if location == 0:  # If location is zero, we are inserting the element at beginning of SLL
                new_node.next = self.head  # We are doing this because head stores node1's physical location.
                # Hence we are setting the new node's next reference to the first node's physical location
                self.head = new_node  # Here we are updating the head with new node's physical location


