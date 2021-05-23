import doubly_linked_lists

my_dll = doubly_linked_lists.DoublyLinkedList()
my_dll.create_doubly_linked_list(value=5)
print([node.value for node in my_dll])

my_dll.insert_node(0, 0)
my_dll.insert_node(1, 1)
my_dll.insert_node(2, 2)
print([node.value for node in my_dll])
my_dll.insert_node(3, 2)
print([node.value for node in my_dll])

my_dll.traversal(0)
print()
my_dll.traversal(1)
print(my_dll.search_elements(6))
