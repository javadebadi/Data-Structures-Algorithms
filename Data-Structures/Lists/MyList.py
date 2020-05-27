class MyList:
    def __init__(self, content = [], initial_size = 10):
        """
        the initial_size is added as a parameter so the programmer
        could assign specific amount of meomory if he/she knows how
        much element he will had in the list

        Time Complexity:
            - no content provided = O(1)
            - with content: O(n)
        """
        self.capacity = initial_size
        self.items = [None] * initial_size
        self.size = 0

        for elem in content:
            self.items.append(elem)

    def __getitem__(self, index):
        """getting value of the item with specified index

        Args:
            index (int): index of the item

        Raises:
            IndexError: out of range access

        Returns:
            value of self.items[index]

        Time complexity:
            O(1)
        """
        if index >= 0 and index < self.capacity:
            return self.items[index]
        else:
            raise IndexError("Getting value from an out of range index")

    def __setitem__(self, index, value):
        """setting value to item with specified index

        Args:
            index (int): index of the item
            value: value to add to items

        Raises:
            IndexError: setting value to out of range index

        Returns:
            no returns

        Time complexity:
            O(1)
        """

        if index >= 0 and index < self.capacity:
            self.items[index] = value
        else:
            raise IndexError("Setting value for out of range index")

        def __increaseCapacity(self):
            """increase the capacity for class container

            Time complexity:
                O(n)
            """

            new_capacity = int(2*self.capacity)
            self.capacity = new_capacity

            new_items = [None]*new_capacity
            for index in range(self.size):
                new_list[index] = self.items[index]
            self.items = new_items


myList = MyList(["a", "b"], 10)
print(" -----> set value 'c' to index 2")
myList[2] = "c"
print(" -----> get value from index 2")
print(myList[2])
print(" -----> get value form index 10")
print(myList[10])
