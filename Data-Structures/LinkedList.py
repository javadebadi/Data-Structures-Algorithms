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

    # prepend element to beginning of LinkedList
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        new_node  = Node(value)
        new_node.next = self.head
        self.head = new_node

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

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def reverse(self):
        """return a LinkedList which is the reverse"""
        output_list = LinkedList()

        prev_node = None

        for value in self:
            new_node = Node(value)
            new_node.next = prev_node
            prev_node = new_node

        output_list.head = prev_node
        return output_list
