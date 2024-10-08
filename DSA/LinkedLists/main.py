import linked_lists

singlyLinkedList = linked_lists.SinglyLinkedList()
singlyLinkedList.insert_singly_linked_list(1, 1)
singlyLinkedList.insert_singly_linked_list(2, 1)
singlyLinkedList.insert_singly_linked_list(3, 1)
singlyLinkedList.insert_singly_linked_list(4, 1)
singlyLinkedList.insert_singly_linked_list(0, 0)
singlyLinkedList.insert_singly_linked_list(6, 3)
# node1 = linked_lists.Node(1)
# node2 = linked_lists.Node(2)
#
# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2
print([node.value for node in singlyLinkedList])

singlyLinkedList.traverse_singly_linked_list()
print(singlyLinkedList.search_singly_linked_list(6))
print()
singlyLinkedList.delete_node(0)
print([node.value for node in singlyLinkedList])
singlyLinkedList.delete_node(1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.delete_node(2)
print([node.value for node in singlyLinkedList])
singlyLinkedList.delete_singly_linked_list()
print([node.value for node in singlyLinkedList])
