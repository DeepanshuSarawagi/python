# Create a login to sum lists and print the digits of a list in reverse order of LinkedList

from linkedlist import LinkedList


def sumList(lla, llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0
    ll = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    return ll


llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)

print(llA)
print(llB)
print(sumList(llA, llB))
