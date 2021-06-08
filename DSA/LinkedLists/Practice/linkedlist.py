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
                print("Found duplicate at index {}".format(index))
                if self.tail == node:
                    is_tail = True
                self.delete_node(index, is_tail)
                print(self)
            else:
                temp_set.append(node.value)
                index += 1
            print("Temp set is now {}".format(temp_set))
            node = node.next

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

    def remove_dups(self, ll):
        if ll.head is None:
            return
        else:
            current_node = ll.head
            visited_nodes = {current_node.value}
            while current_node.next:
                if current_node.next.value in visited_nodes:
                    current_node.next = current_node.next.next
                else:
                    visited_nodes.add(current_node.next.value)
                    current_node = current_node.next
        return ll

    def nth_from_last(self, n):
        pointer1 = self.head
        pointer2 = self.head

        for i in range(n):
            if pointer2 is None:
                return
            else:
                pointer2 = pointer2.next
                print(pointer2)
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
