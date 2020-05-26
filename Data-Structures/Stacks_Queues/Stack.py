# implement Stack data structure using Linked Lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.num_elements = 0

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def push(self, data):
        """ push data to top of the stack
        """

        if self.top == None:
            self.top = Node(data)
            self.num_elements = 1
            return

        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.num_elements += 1

    def pop(self):
        """returns the top value of the Stack and removes that value
        from Stack
        """
        if self.is_empty():
            print("No value in Stack, returns None")
            return None

        pop_value = self.top.value
        self.top = self.top.next
        self.num_elements -= 1

        return pop_value

    def __str__(self):

        output = ""
        output += ("number of elements : " + str(self.num_elements) + "\n")
        if self.is_empty():
            return ""
        else:
            node = self.top

        while node:
            try:
                output += str(node.value)
                output += " -> "
            except:
                pass
            node = node.next
        return output
