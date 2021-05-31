import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)  # When we call the print function on Node object, this fn will be called


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            node = Node(value=value)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(value=value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(random.randint(min_value, max_value))
        return self

    def remove_duplicates(self):
        node = self.head
        index = 0
        node_value = node.value
        while node:
            node = node.next
            index += 1
            next_node_value = node.value
            if next_node_value == node_value:
                print("Found duplicate at index {}".format(index))
        self.delete_node(index)

    def delete_node(self, location):
        node = self.head
        index = 0
        while index < location:
            node = node.next
        next_node = node.next
        if self.tail == next_node:
            print("We are deleting the duplicate node which is tail of the linked list")
            node.next = None
            self.tail = node
        else:
            print("We are deleting the duplicate node from the middle of the linked list")
            node.next = next_node.next
