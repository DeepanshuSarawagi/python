"""
This Python file is created to learn about Cirulcar Doubly Linked Lists.
This will have following two classes.

@class: Node
@class: CircularDoublyLinkedLists

"""


class Node:
    """
    This class is used to create node objects which have three attributes
    @Attributes:
        value: This attribute is used to hold the node's value
        next: This attribute will hold the reference to address of next node
        prev: This attribute will hold the reference to address of previous node
    @Methods:
        __init__(self) : This is the constructor used to create Node objects. One parameter is required to initialize
        Node objects

    """

    def __init__(self, value):
        """
        :param value: This will hold the value of Node passed as parameter while constructing Node objects
        """
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedLists:
    """
        This class will be used to create Circular Doubly Linked List objects.
        They will form the blueprint of implementing doubly linked list data structure

        @Attributes:
            self.head: This attribute will hold the reference of first node's physical address in the DLL.
            self.tail: This attribute will hold the reference of last node's physical address in the DLL.
        """

    def __init__(self):
        """
        :param head: This attribute will hold the reference of first node's physical address in the DLL.
        :param tail: This attribute will hold the reference of last node's physical address in the DLL.
        """
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.tail.next:
                break

    def create_circular_dll(self, node_value):
        node = Node(value=node_value)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node
