class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_from_head_to_tail(self):

        if self.head == None:
            return

        doubleNode = self.head
        print(doubleNode.value)
        while doubleNode.next:
            doubleNode = doubleNode.next
            print(doubleNode.value)

    def print_from_tail_to_head(self):

        if self.tail == None:
            return

        doubleNode = self.tail
        print(doubleNode.value)
        while doubleNode.prev:
            doubleNode = doubleNode.prev
            print(doubleNode.value)

    def append(self, value):

        if self.head == None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        # add elemet to tail
        self.tail.next = DoubleNode(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        return
