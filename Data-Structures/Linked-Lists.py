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

def create_linked_list(input_list):
    """
    Function to create a linked list
    param input_list: a list of integers
    return: head node of the linked list
    """
    head = None
    tail = None

    for value in input_list:

        if head is None:
            head = Node(value)
            tail = head # when we only have 1 node, head and tail refer to the same node
        else:
            tail.next = Node(value) # attach the new node to the `next` of tail
            tail = tail.next # update the tail
            
    return head


# create a linked input
linked_list = create_linked_list([1,0,10,15])
# print elements of the linked list
print_linked_list(linked_list)
