"""
DLL is abbreviated as Doubly Linked List
We are creating two classes here. One is the Node class and the other is Doubly Linked List which will be the
blue print of the implementation.
"""


class Node:
    """
    This class will be used to create the Node objects. The Node objects will be linked together to form a Doubly
    Linked List.

    @Attributes:
        self.value = Node objects value
        self.next = This will hold the next node's reference of physical address
        self.prev = This will hold the previous node's reference of phycial address
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    This class will be used to create Doubly Linked List objects.
    They will form the blueprint of implementing doubly linked list data structure

    @attributes:
        self.head = This attribute will hold the reference of first node's physical address in the DLL.
        self.tail = This attribute will hold the reference of last node's physical address in the DLL.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of doubly linked list
    def create_doubly_linked_list(self, value):
        node = Node(value=value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return "The Doubly Linked List is created successfully"
