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

    @Attributes:
        self.head: This attribute will hold the reference of first node's physical address in the DLL.
        self.tail: This attribute will hold the reference of last node's physical address in the DLL.
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

    # Insertion of a new node in Doubly Linked List
    def insert_node(self, value, location):
        """
        This method is created to insert a new node in the Doubly Linked List. The new node can be inserted at the
        beginning, middle or end of the list.
        :param value: This will hold the value of Node object assigned to it
        :param location: This parameter will insert the new node either at the beginning, end, or at any position in the
        list.
        :return: None
        """
        if self.head is None:
            print("The list is empty")
        else:
            new_node = Node(value=value)
            if location == 0:  # Checking if we want to insert the new node at beginning of the DLL
                new_node.prev = None  # If we insert at beginning, we need to set the previous reference of this new
                # node to None
                new_node.next = self.head  # We know that self.head has the reference to first node in the list.
                # New node's next reference should be list's first node
                self.head.prev = new_node  # First node's previous reference is set to new node thereby creating a
                # two-way link between them
                self.head = new_node  # Updating the head's reference to new node
            elif location == 1:  # Checking if we want to insert the new node at the end of the list
                new_node.next = None  # Setting the new node's next reference to None
                new_node.prev = self.tail  # We know that tail has reference to last node. setting the new node's
                # previous reference to last node.
                self.tail.next = new_node  # Setting the last node's next reference to new node. Thereby creating a
                # two-way link between them
                self.tail = new_node  # Updating the tail's reference with new node
            else:
                current_node = self.head
                index = 0
                while index < location - 1:  # Looping until the position before where we want to insert the new node
                    current_node = current_node.next
                    index += 1
                next_node = current_node.next  # Getting the next node from current node's next reference
                new_node.next = next_node  # Setting the new node's next reference to next node
                new_node.prev = current_node  # new node's previous reference to current node
                next_node.prev = new_node  # Next node's previous reference to new node
                current_node.next = new_node  # current node's next reference to new node

    def traversal(self, location):
        """
        This method will traverse through the doubly linked list either in forward or backward direction.
        :param location: 0 will traverse from beginning of the list in forward direction and 1 will traverse through
        the list from the end of the list in backward direction
        :return: None
        """
        if self.head is None:
            print("The list is empty.")
        else:
            if location == 0:
                node = self.head
                while node is not None:
                    print(node.value)
                    node = node.next
            elif location == 1:
                node = self.tail
                while node is not None:
                    print(node.value)
                    node = node.prev
            else:
                print("Location undefined. Please try again.")

    # Search for elements/nodes in Doubly Linked List
    def search_elements(self, value):
        if self.head is None:
            print("The linked list is empty")
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == value:
                    return "Found the element at position {} in the linked list".format(index + 1)
                node = node.next
                index += 1
            return "The element doesn't exist in the list"
