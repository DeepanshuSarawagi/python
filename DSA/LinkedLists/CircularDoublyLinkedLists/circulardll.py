import circular_dll

my_cdll = circular_dll.CircularDoublyLinkedLists()
my_cdll.create_circular_dll(5)
print([node.value for node in my_cdll])
my_cdll.insert_node(0, 0)
my_cdll.insert_node(1, -1)
my_cdll.insert_node(2, 2)
my_cdll.insert_node(5, -1)
my_cdll.insert_node(3, 1)
my_cdll.insert_node(4, 2)
print([node.value for node in my_cdll])
my_cdll.traverse_nodes()
