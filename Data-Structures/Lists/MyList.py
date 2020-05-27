class MyList:
    def __init__(self, content = [], initial_size = 10):
        """
        the initial_size is added as a parameter so the programmer
        could assign specific amount of meomory if he/she knows how
        much element he will had in the list
        """
        self.max_size = initial_size
        self.items = [None] * initial_size
        self.size = 0

        for elem in content:
            self.items.append(elem)


myList = MyList(["a", "b"], 10)
