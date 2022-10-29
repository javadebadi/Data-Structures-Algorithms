"""
Binary search tree is a tree where each node has up to two children
and values in left subtree of a node are less that the value in root node
and values in right subtree of a node are bigger that the value in root node
Finally, the left and right subtrees must also be binary search trees.
"""

class BinarySearchTree:
    """Binary Search Tree data structure.
    

    Time complexity
        - insert: O(log(n))
        - build: O(n log(n))

    If the data is already sorted, binary search algorithm show poor
    performance.
    If data is already sorted, the binary search tree becomes linked list
    and the the time comlexities are:
    Worst case time complexity:
        - insert : O(n)
        - build : O(n^2)

    If we have lots of insert, delete and lookup operations, a tree-like structure
    may be useful. Binary search tree does not guarantee O(log (n)) for these operations.
    But Splay Trees, AVL-Trees and B-Tress guarantee.
    """

    class __Node:
        def __init__(
            self,
            val,
            left=None,
            right=None,
            ) -> None:
            self.val = val
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left is not None:
                for item in self.left:
                    yield item

            yield self.val

            if self.right is not None:
                for item in self.right:
                    yield item

    def __init__(self):
        self.root = None

    def insert(self, value):

        def __insert(root, value):
            """A function which gets the tree and value and returns new tree
            after insertion
            """
            if root is None:
                root = BinarySearchTree.__Node(val=value)
            else:
                if value < root.val:
                    root.left = __insert(root.left, value)
                else:
                    root.right = __insert(root.right, value)
            return root

        self.root = __insert(self.root, value)

    def build(self, values):
        """Builds tree based on given values"""
        self.root = None
        for value in value:
            self.insert(value)
        return self.root


    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()


btree = BinarySearchTree()
btree.insert(5)
btree.insert(8)
btree.insert(2)
btree.insert(1)
btree.insert(4)
btree.insert(9)
btree.insert(6)
btree.insert(7)
for item in btree:
    print(item)

