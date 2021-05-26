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
        node.next = node  # Since we are creating circular doubly linked list with just one node, we are point the
        # node's next reference and node's previous reference to itself
        node.prev = node
        self.head = node
        self.tail = node

    def insert_node(self, node_value, location):
        """
        This method is used to insert new_node in the circular doubly linked list based on the location parameter
        passed. If value of location is 0, then new node will be inserted at the beginning of the list. if value of
        location is -1, the new node will be inserted at the end of the list. Else new node will be inserted at any
        given position between first and last node
        :param node_value: This parameter will hold the value of new node
        :param location: This parameter will decide in which position new node will be inserted
        :return: None
        """
        if self.head is None:
            print("The circular doubly linked list is empty")
        else:
            new_node = Node(value=node_value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                next_node = current_node.next
                new_node.next = next_node
                new_node.prev = current_node
                next_node.prev = new_node
                current_node.next = new_node
