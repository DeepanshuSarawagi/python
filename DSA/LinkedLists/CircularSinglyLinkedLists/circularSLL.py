"""
SLL is abbreviated as Singly Linked Lists
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create_circular_sll(self, node_value):
        node = Node(value=node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The circular singly linked list is created"

    # Insertion in circular singly linked list
    def insert_circular_sll(self, value, location):
        if self.head is None:
            print("The ciruclar linked list doesnt exist")
        else:
            new_node = Node(value=value)
            if location == 0:  # Inserting element at beginning of circular SLL
                new_node.next = self.head  # Here we are creating link between new node and first node. We know that
                # head has reference to first node. So new node's next reference will be set to first node
                self.head = new_node  # Then we will link the new and head. So head will have the reference to new node
                # and will break the link with existing first node. Thereby, link will be like this
                # head -> new node -> first node
                self.tail.next = new_node  # We know that tail has the reference to last node. hence last node's next
                # reference will be new node
            elif location == 1:
                new_node.next = self.tail.next  # Here, we are setting the next reference of new node with the first node.
                # We know that tail has reference to last node. And last node's next reference is first node. Hence a
                # link will be established between new node and first node
                self.tail.next = new_node  # Here we are setting the last node's next reference with new node
                self.tail = new_node  # Setting the tail's reference with new node, thereby making it last node
