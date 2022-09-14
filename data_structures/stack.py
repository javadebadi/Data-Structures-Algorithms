"""Implementation of Stack data structure.

We can use Python list to implement Stack data structure. However, we prefer
to use our own linked_list implementation to implement Stack data structure.

Stack is a data structure which is useful when data are put on top of each
other.

Stack is not appropriate if you want to access data at arbitrary index of the
collection.

Time Complexity:
    - peek: O(1)
    - pop: O(1)
    - push: O(1)

"""
from .linked_list import LinkedList

class Stack:
    """Stack data structure.
    """

    def __init__(self) -> None:
        self.items = LinkedList()

    def peek(self):
        """Returns the top element without removing it.

        The `peek` method returns the top element of the stack without
        removing the element from the stack. The `peek` method returns
        the same value as `pop` method but unlike the `pop` method it 
        does not change state of the stack.

        Time Complexity: O(1)

        Returns
        -------
        : Any
            Returns top element of the stack.

        Raises
        ------
        IndexError
            When the stack is empty, peeking from it will raise an IndexError 
            stating that 'Cannot peek from empty stack'

        """
        try:
            return self.items.head.value
        except IndexError:
            raise IndexError("Cannot peek from empty stack")

    def pop(self):
        """Returns the top element and removes it from top of stack.
        
        The `pop` method returns the top element and removes if from top of 
        the stack.

        Time Complexity: O(1)

        Returns
        -------
        : Any
            Returns top element of the stack.

        Raises
        ------
        IndexError
            When the stack is empty, poping from it will raise an IndexError 
            stating that 'Cannot pop from empty stack'.

        """
        value = self.items.pop()
        if value is None:
            raise IndexError("Cannot peek from empty stack")
        else:
            return value

    def push(self, value) -> None:
        """Pushs new value to top of the stack.
        
        Parameters
        ----------
        value : Any
            The value to be add on top of the stack.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the value is Noen it will raise a ValueError that states:
            'Cannot push None on top of the stack'

        """
        if value is not None:
            self.items.prepend(value)
        else:
            raise ValueError(
                "Cannot push None on top of the stack"
                )