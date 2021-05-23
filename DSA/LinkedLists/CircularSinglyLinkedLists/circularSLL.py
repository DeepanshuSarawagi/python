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
                new_node.next = self.tail.next  # Here, we are setting the next reference of new node with the first
                # node. We know that tail has reference to last node. And last node's next reference is first node.
                # Hence a link will be established between new node and first node
                self.tail.next = new_node  # Here we are setting the last node's next reference with new node
                self.tail = new_node  # Setting the tail's reference with new node, thereby making it last node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next  # considering temp node is current node, current node's next value is next
                # node
                temp_node.next = new_node  # Inserting new node in between current node and current's next node
                new_node.next = next_node  # and setting new node's next reference to next node
            return "New node has been successfully inserted"

    # Traversal in circular singly linked list
    def traversal_circularSLL(self):
        if self.head is None:
            print("The list is empty")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break

    # Searching for an element in circular SLL
    def search_element(self, value):
        if self.head is None:
            print("The list is empty")
        else:
            temp_node = self.head
            while temp_node is not None:
                if temp_node.value == value:
                    return "Value found in list"
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return "Value does not exist in the list"

    # Deleting a node from circular SLL
    def delete_node(self, location):
        if self.head is None:
            print("The linked list is empty")
        else:
            if location == 0:
                if self.head == self.tail:  # Checking if there is only one node in the Circular SLL
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next  # Here we are setting the reference of head with the next node of
                    # first node.
                    self.tail.next = self.head  # Creating the link between last node and second node
            elif location == 1:
                if self.head == self.tail:  # Checking if there is only one node in the Circular SLL
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:  # here we are looping until the node before last node
                            break
                        node = node.next
                    node.next = self.head  # here we are setting this node's reference to the head (first node)
                    self.tail = node  # Setting the reference of tail with this node
            else:
                node = self.head
                index = 0
                while index < location - 1:  # here we are looping until the location of node which needs to be deleted
                    node = node.next
                    index += 1
                next_node = node.next  # Getting the next node of current node
                node.next = next_node.next  # Creating the link between current node and node after next node. This way
                # the node between current node and node after next node gets deleted.
