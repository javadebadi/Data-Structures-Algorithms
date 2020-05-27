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

        for index in range(len(content)):
            self.items[index] = content[index]
            self.size += 1

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
            self.size += 1
        else:
            raise IndexError("Setting value for out of range index")

    def __add__(self, other):
        result = MyList(initial_size = self.capacity + other.capacity)

        for index in range(self.size):
            result.append(self.items[index])

        for index in range(other.size):
            result.append(other.items[index])

        return result

    def __increaseCapacity(self):
        """increase the capacity for class container

        Time complexity:
            O(n)
        """

        new_capacity = int(2*self.capacity)
        self.capacity = new_capacity

        new_items = [None]*new_capacity
        for index in range(self.size):
            new_items[index] = self.items[index]
        self.items = new_items

    def append(self, value):
        """add new values to end of the items

        Args:
            value: the value which will be added

        Returns:
            no Returns

        Time complexity:
            - no increse in capacity: O(1)
            - increase in capacity: O(__increaseCapacity)
        """
        if self.size >= self.capacity:
            self.__increaseCapacity()

        self.items[self.size] = value
        self.size += 1



myList = MyList(["0", "1"], 3)
print(" -----> set value '2' to index 2")
myList[2] = "2"
print(" -----> get value from index 2")
print(myList[2])
print(" -----> get value form index 10")
#print(myList[10])
print(" -----> append values")
myList.append("3")
myList.append("4")
print(myList.capacity)
myList1 = MyList(content = ["Jack","John"])
myList2 = MyList(content=["Javad", "Joe"])
print((myList1 + myList2)[1])
