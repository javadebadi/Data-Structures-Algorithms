"""Implement Abstract Syntax Tree (AST)
"""

class ASTNode:

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self):
        pass


class TimesNode(ASTNode):

    def eval(self):
        return self.left.eval() * self.right.eval()


class PlusNode(ASTNode):

    def eval(self):
        return self.left.eval() + self.right.eval()

class NumNode:

    def __init__(self, num) -> None:
        self.num = num


    def eval(self):
        return self.num


if __name__ == '__main__':
    # AST Tree for (10 + 20) * 2
    num1 = NumNode(10)
    num2 = NumNode(20)
    p = PlusNode(num1, num2)
    num3 = NumNode(2)
    x = TimesNode(num3, p)
    print(x.eval())
