import linkedlist

my_ll = linkedlist.LinkedList()
my_ll.generate(10, 0, 99)
print(my_ll)
print(len(my_ll))

linkedlist_1 = linkedlist.LinkedList()
linkedlist_1.add(1)
linkedlist_1.add(2)
linkedlist_1.add(2)
linkedlist_1.add(3)
linkedlist_1.add(4)
linkedlist_1.add(1)
linkedlist_1.add(6)
linkedlist_1.add(6)
linkedlist_1.add(2)
linkedlist_1.add(1)
print(linkedlist_1)
# linkedlist_1.remove_duplicates()
inst1 = linkedlist.LinkedList()
print(inst1.remove_dups(linkedlist_1))

print(linkedlist_1.nth_from_last(3))
