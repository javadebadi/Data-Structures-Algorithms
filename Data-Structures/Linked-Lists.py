class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



head = Node(2)  # head is the first element of a linked list
head.next = Node(1) # create a new Node object and assign the object (its location in memory) to head.next
# add other nodes
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

# test the linked list
print("head value                        = " + str(head.value))
print("next of head value                = " + str(head.next.value))
print("next next of head value           = " + str(head.next.next.value))
print("next next next of head value      = " + str(head.next.next.next.value))
print("next next next next of head value = " + str(head.next.next.next.next.value))
