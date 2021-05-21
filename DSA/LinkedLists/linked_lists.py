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
            elif location == 1:  # inserting element at the end of SLL
                new_node.next = None  # Here we are setting last node's next reference to null
                self.tail.next = new_node  # Here we are setting the next reference of last node to new node
                self.tail = new_node
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

    # Traverse through Single Linked List
    def traverse_singly_linked_list(self):
        if self.head is None:
            print("The Singly Linked List is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search in Single Linked List
    def search_singly_linked_list(self, value):
        if self.head is None:
            return "The Singly Linked List is empty"
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == value:
                    return "Found element at index {}".format(index)
                node = node.next
                index += 1
            return "The value does not exist in the list"

    # Deleting a node from singly linked list
    def delete_node(self, location):
        if self.head is None:
            print("The list is empty")
        else:
            if location == 0:  # Checking if we want to delete the node at beginning of SLL
                if self.head == self.tail:  # Checking if we have just one node in SLL
                    self.head = None
                    self.tail = None  # Breaking the links of head/tail with that node
                else:
                    self.head = self.head.next  # We know that head has reference of first node's physical location.
                    # hence we are setting the head's reference with first node's next node i.e., second node
                    # this will delete the link between head and first node
            elif location == 1:  # checking if we want to delete the last node
                if self.head == self.tail:  # Checking if we have just one node in SLL
                    self.head = None
                    self.tail = None  # Breaking the links of head/tail with that node
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:  # we know that tail has reference to last node, hence traverse
                            # until we find the last node and then break the loop. Loop will terminate at last node's
                            # previous node
                            break
                        node = node.next
                    node.next = None  # once last node is found, set its previous node's reference to Null
                    self.tail = node  # and set the tail with reference of previous node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next  # iterate until we find the node we want to delete. temp node is the
                    # one before the node which has to be deleted
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next  # setting temp node's next reference with next node's next reference.
                # hence this will break the link between current node and next node.

    def delete_singly_linked_list(self):
        if self.head is None:
            print("The list is empty.")
        else:
            self.head = None
            self.tail = None
