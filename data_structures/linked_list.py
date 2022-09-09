"""Linked List Implementation in Python.

Linked List is a linear data structure.

Time complexity of operations on Linked Lists is as following:
- Access Head: O(1)
    The Linked List is defined by its head, therefore it takes constant
    time to access the head node.
- Access: O(n)
    To access the elements in Linked List, it is necessary to traverse
    all nodes starting from head to access the nth element.
- Append: O(n)
    To append to end of the linked list, it is neccessary to reach tail
    and then add new node.
- Prepend: O(1)
    To prepend to start fo the linked list the only operation needed is
    to access the head and swap it with newly created node
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        """Determines whether the Linked List is empty or not
        
        Time complexity: O(1)

        Returns
        -------
        : bool
            If the the linked list is empty it returns True else
            it returns False.
        """
        return self.head is None

    def print_all(self) -> None:
        """prints all element of a linked lis
        
        Time complexity: O(n)
        """
        # if the linked list is empty there is nothing to print
        if self.is_empty():
            return None

        # print all elements by traversing from head to tail
        node = self.head
        node_counter = 0
        while node:
            print(f"{node_counter}: {node.value}")
            node = node.next
            node_counter += 1
        return None

    def append(self, value) -> None:
        """Appends a new node with give value to end of the linked list.

        Time complexity: O(n)

        Parameters
        ----------
        value : any

        Returns
        -------
        None
        """
        if self.head is None:
            self.head = Node(value)
            return None

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        # set next node of the existing tail to a new node
        node.next = Node(value)
        return None

    def prepend(self, value) -> None:
        """Prepends a new node with given value to start of the linked list.

        Parameters
        ----------
        value : any

        Returns
        -------
        None
        """
        # for empty linked list prepending is just same as
        # the creating the head node
        if self.is_empty():
            self.head = Node(value)
            return None
        # create new node and make it the head of the linked list
        new_node  = Node(value)
        new_node.next = self.head
        self.head = new_node

    def to_list(self) -> list:
        """Returns a Python list from linked list with same order.

        Time Complexity: O(n)

        Reutrns
        -------
        list_of : list
        """

        list_of = []
        if self.is_empty():
            return list_of

        node = self.head
        while node:
            list_of.append(node.value)
            node = node.next
        return list_of

    def __iter__(self):
        """Iterator on linked list
        """
        node = self.head
        while node:
            yield node.value
            node = node.next

    def reverse(self, inplace=True) -> list:
        """return a LinkedList which is the reverse of this linked list.

        Time complexity: O(n)

        Returns
        -------
        list
        """
        output_list = LinkedList()

        for value in self:
            output_list.prepend(value)

        return output_list

    def search(self, value) -> Node:
        """Searches the linked list for a value and returns the Node.

        If the method finds the value in a node, it return the Node,
        else it will return None.

        Time complexity: O(n)

        Returns
        -------
        Node
        """
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        # if the value is not found the None will be returned
        return None

    def remove(self, value, how='first') -> None:
        """Deletes the first node with the desired data.

        Time complexity: O(n)

        Parameters
        ----------
        value : any
            The value that is needed to be deleted from linked list.
        how : str
            The `how` parameter sepcifies how deletion must be done. If it
            is set to 'all', it will remove all occurence of the value in
            the linked list. If it is set to 'first' if will just remove
            the first occurence of the value in the linked list.

        Returns
        -------
        None
        """

        if self.is_empty():
            return None

        # variables to keep track of prev and next nodes
        prev = None
        next_ = None

        # loop over all nodes in the linked list and delete the node(s)
        # with give value
        node = self.head
        while node:
            next_ = node.next
            if node.value != value:
                prev = node
                node = next_
            else:
                if prev is not None:
                    prev.next = next_
                    node = next_
                else:
                    prev = None
                    node = next_
                    self.head = node
                # determine whether remove all occurence or
                # just the first occurence
                if how == 'all':
                    continue
                elif how == 'first':
                    break

    def pop(self):
        """Returns the first node's value and removes it from the list.

        Time complexity: O(1)
        """
        if self.is_empty():
            return None

        val = self.head.value
        self.head = self.head.next
        return val

    def size(self) -> int:
        """Returns size of the linked list.
        
        Time complexity: O(n)

        Returns
        -------
        : int
            size of the linked list
        """
        size = 0
        if self.is_empty():
            return size

        node = self.head()
        while node:
            size += 1
            node = node.next
        return size

    def __len__(self) -> int:
        """Returns size of the linked list.

        It is natural to define length of the linked list as the number
        of nodes in the linked list.

        Time complexity: O(n)

        Returns
        -------
        : int
        """
        return self.size()

    def insert(self, value, pos):
        """Inserts value at given position in the linked list.


        Time complexity: O(n)

        Parameters
        ----------
        pos : int
            Position of the insertion

        value : any
            The value to insert in the position `pos`

        
        If `pos` is larger than the length of the linked list,
        append to the end of the list.
        """

        if type(pos) != int or pos < 0:
            raise ValueError(
                f"Position `pos` value '{pos}' is "
                "invalid index for LinkedList"
                )

        if self.is_empty():
            self.append(value)
            return None

        if pos == 0:
            self.prepend(value)
            return None

        current_pos = pos
        node = self.head
        while current_pos > 1:
            if node.next is not None:
                node = node.next
                current_pos -= 1
            else:
                break

        old_next_node = node.next
        new_next_node = Node(value)
        node.next = new_next_node
        new_next_node.next = old_next_node


    def __getitem__(self, index):
        """Returns the value of the node in given index.
        
        Time complexity: O(n)

        Returns
        -------
        value : any
        """
        node = self.head
        assert type(index) == int and index >= 0
        for index_ in range(index + 1):
            if node is None:
                raise IndexError(f"index = '{index}' is out of range.")
            if index_ == index:
                return node.value
            else:
                node = node.next
