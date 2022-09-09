class StackArray:

    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0  # index of container next to top which is used to add new elements
        self.num_elements = 0

    # TODO Add the push method
    def push(self, data):
        """pushs new vdata to top of the stack
        param data: new data we need to push to top of the stack"""

        # check for stack overflow
        if self.next_index == len(self.arr):
            print("Stack Overflow; resizing the container of the stack ...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        """pops the top element of the stack"""
        if self.is_empty():
            self.next_index = 0
            return None
        else:
            self.next_index -= 1
            self.num_elements -= 1
            return self.arr[self.next_index]

    def size(self):
        """returns size of the stack"""
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value
