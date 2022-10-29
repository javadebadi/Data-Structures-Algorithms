"""A function to parse prefix expression and build AST Tree

Grammer G = (N, J, P, E) where
    N = {E}
    J = {identifier, number, +, *}
    P is defined by the set of productions
        E -> + E E | * E E | number
"""

import queue
from ast import TimesNode, PlusNode, NumNode


def E(q):

    while not q.empty():

        token = q.get()

        if token == '+':
            return PlusNode(E(q), E(q))

        if token == '*':
            return TimesNode(E(q), E(q))

        return NumNode(float(token))


def parse(x):
    """Top-down parser"""

    q = queue.Queue()

    for token in x.split():
        q.put(token)

    root = E(q)

    print(root.eval())


print(parse(x = "+ * 6 2 2"))
    