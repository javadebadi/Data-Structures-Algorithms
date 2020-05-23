class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Print method
    def print_all(self):
        """prints all element of a linked lis"""
        if self.head == None:
            return

    # print all elements by going from head to tail
        node = self.head
        print(node.value)
        while node.next:
            node = node.next
            print(node.value)

    # Append method
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    # convert LinkedList to python list
    def to_list(self):

        list_of = []
        if self.head == None:
            return list_of

        node = self.head
        list_of.append(node.value)
        while node.next:
            node = node.next
            list_of.append(node.value)

        return list_of


linked_list = LinkedList()
linked_list.append(0.2)
linked_list.append(1)
linked_list.append(0)
# print elements of the linked list
linked_list.print_all()
