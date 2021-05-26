import circular_dll

my_cdll = circular_dll.CircularDoublyLinkedLists()
my_cdll.create_circular_dll(1)
print([node.value for node in my_cdll])
