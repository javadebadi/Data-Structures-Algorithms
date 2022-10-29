"""Implement Abstract Syntax Tree (AST)
"""
import queue


class ASTNode:

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self):
        pass

    def inorder(self):
        """Returns inorder expression string"""
        pass

    def postorder(self):
        """Returs postfix expression string"""
        pass

    def preorder(self):
        """Returns preorder expression string"""
        pass


class TimesNode(ASTNode):

    def eval(self):
        return self.left.eval() * self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " * " + self.right.inorder() + ")"

    def postorder(self):
        return self.left.postorder() + " " + self.right.postorder() + " *"

    def preorder(self):
        return "* " + self.left.preorder() + " " + self.right.preorder()

class PlusNode(ASTNode):

    def eval(self):
        return self.left.eval() + self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " + " + self.right.inorder() + ")"

    def postorder(self):
        return self.left.postorder() + " " + self.right.postorder() + " +"

    def preorder(self):
        return "+ " + self.left.preorder() + " " + self.right.preorder()

class NumNode:

    def __init__(self, num) -> None:
        self.num = num

    def eval(self):
        return self.num

    def inorder(self):
        return str(self.num)

    def postorder(self):
        return str(self.num)

    def preorder(self):
        return str(self.num)


if __name__ == '__main__':
    # AST Tree for (10 + 20) * 2
    # postfix expression 10 20 + 2 *
    # infix expression ((10 + 20) * 2)
    # prefix expression * + 10 20 2
    num1 = NumNode(10)
    num2 = NumNode(20)
    p = PlusNode(num1, num2)
    num3 = NumNode(2)
    x = TimesNode(p, num3)
    print(x.eval())
    print(x.inorder())
    print(x.postorder())
    print(x.preorder())
