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
        is_tail = False
        temp_set = []
        while node is not None:
            if node.value in temp_set:
                if self.tail == node:
                    is_tail = True
                self.delete_node(index, is_tail)
            else:
                temp_set.append(node.value)
            node = node.next
            index += 1

    def delete_node(self, location, is_tail: bool):
        node = self.head
        index = 0
        if is_tail is True:
            while node is not None:
                if node.next == self.tail:
                    break
                node = node.next
            node.next = None
            self.tail = node
        else:
            while index < location - 1:
                node = node.next
                index += 1
            next_node = node.next
            node.next = next_node.next
