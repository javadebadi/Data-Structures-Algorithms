"""AVL Tree Data Structure

AVL Tree data structure is such that its heigh is guarnateed to be O(log(n))
and therefore guaranteed to have the following time complexities:
- insert: O(log(n))
- update: O(log(n))
- delete: O(log(n))
- traverse yield item in ascending order: O(n)
- build tree: O(n log(n))

AVL Tree data structures are balanced unlike the ordinary binary search tree
data structure.


Height of Tree : 1 + height of subtrees where height of leaf nodes are 1
Balance: The balance of a node in a binary tree is = height(right subtree) - height(left subtree)
AVL Tree: a binary tree in which balance of every node in the tree is -1, 0, 1
"""
import json

import logging

# create logger
logger = logging.getLogger('avl')
logger.setLevel(logging.INFO)

# create handler
ch = logging.FileHandler('avl.log', mode='w')
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


class AVLTree:

    class AVLNode:
        def __init__(
            self,
            item,
            balance=0,
            left=None,
            right=None,
            ) -> None:
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance

        def __iter__(self):
            for item in self.left:
                yield item.__iter__()

            yield self.item

            for item in self.right:
                yield item.__iter__()

        def to_json(self):
            d = {}
            if self is not None:
                d["item"] = self.item
                d["balance"] = self.balance
            else:
                return {}
            if self.left is None:
                d["left"] = None
            else:
                d["left"] = self.left.to_json()
            if self.right is None:
                d["right"] = None
            else:
                d["right"] = self.right.to_json()
            return d

        def to_d3_hierarchy(self):
            d = {}
            if self is None:
                return {
                    "name": "null",
                }
            else:
                d["name"] = f"({self.item}, {self.balance})"
                if self.left is not None or self.right is not None:
                    d["children"] = []
                    if self.right is not None:
                        d["children"].append(self.right.to_d3_hierarchy())
                    else:
                        d["children"].append({"name": "null"})
                    if self.left is not None:
                        d["children"].append(self.left.to_d3_hierarchy())
                    else:
                        d["children"].append({"name": "null"})
            return d

        def __repr__(self) -> str:
            return "AVLTree.AVLNode(" + repr(self.item) + ", balance=" +\
                repr(self.balance) + ", left=" + repr(self.left) +\
                    ", right=" + repr(self.right) +  ")"

    def __init__(self) -> None:
        self.root = None
        self.path_stack = []

    def clear_path_stack(self):
        self.path_stack = []

    # def rebalance()

    def insert(self, value):

        self.clear_path_stack()

        def __insert(root, value):
            """A function which gets the tree and value and returns new tree
            after insertion
            """
            if root is None:
                root = AVLTree.AVLNode(item=value)
                self.path_stack.append(root)
            else:
                if value < root.item:
                    self.path_stack.append(root.left)
                    root.left = __insert(root.left, value)
                    root.balance -= 1
                else:
                    self.path_stack.append(root.right)
                    root.right = __insert(root.right, value)
                    root.balance += 1
            return root

        self.root = __insert(self.root, value)
        logger.info(self.__str__())
        logger.info(self.path_stack)

    def __iter__(self):
        if self.root is None:
            return [].__iter__()
        else:
            return self.root.__iter__()

    def to_json(self):
        d = {"root": {}}
        if self.root is not None:
            d["root"] = self.root.to_json()
        return d

    def to_d3_hierarchy(self):
        result = []
        if self.root is not None:
            result = [self.root.to_d3_hierarchy()]
        # result = json.dumps(result, indent=4)
        return result

    def to_d3_html(self):

        
        treeData = self.to_d3_hierarchy()

        d = {
            "treeData": treeData,
        }
        from string import Template
        result = ""
        with open('templates/tree.html', 'r') as f:
            src = Template(f.read())
            result = src.substitute(d)
        with open("avl.html", "w") as fp:
            fp.write(result)

    def __str__(self) -> None:
        return json.dumps(self.to_json(), indent=4)



tree = AVLTree()
tree.insert(10)
tree.insert(18)
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(13)
tree.insert(40)
tree.insert(39)
tree.insert(38)
logger.info(tree.to_d3_hierarchy())
tree.to_d3_html()