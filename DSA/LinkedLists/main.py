import linked_lists

singlyLinkedList = linked_lists.SinglyLinkedList()
node1 = linked_lists.Node(1)
node2 = linked_lists.Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2
