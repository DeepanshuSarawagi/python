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
            if node.next == self.head:
                break
            node = node.next

    def create_circular_sll(self, node_value):
        node = Node(value=node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The circular singly linked list is created"
