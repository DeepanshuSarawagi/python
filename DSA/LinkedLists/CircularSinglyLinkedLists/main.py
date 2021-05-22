import circularSLL

circular_sll = circularSLL.CircularSinglyLinkedList()

circular_sll.create_circular_sll(node_value=1)
print([node.value for node in circular_sll])

circular_sll.insert_circular_sll(0, 0)
circular_sll.insert_circular_sll(5, 1)
circular_sll.insert_circular_sll(2, 2)
circular_sll.insert_circular_sll(3, 3)
circular_sll.insert_circular_sll(4, 3)
print([node.value for node in circular_sll])
print()
circular_sll.traversal_circularSLL()
print()
print(circular_sll.search_element(5))
