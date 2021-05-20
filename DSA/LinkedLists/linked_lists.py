"""
We will be creating singly linked lists with one head, one node and one tail.
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

