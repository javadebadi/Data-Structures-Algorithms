class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_linked_list(head):
    """prints all element of a linked list
    param head: is a linked list
    """
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next



head = Node(2)  # head is the first element of a linked list
head.next = Node(1) # create a new Node object and assign the object (its location in memory) to head.next
# add other nodes
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

# print elements of the linked list
print_linked_list(head)
