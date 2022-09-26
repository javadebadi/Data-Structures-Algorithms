from data_structures.linked_list import LinkedList
from data_structures.stack import Stack

linked_list = LinkedList()
for i in range(10):
    linked_list.append(i)

linked_list.print_all()
print("............")
# linked_list.reverse().print_all()
linked_list.remove(0)
linked_list.remove(0)
linked_list.remove(0)
linked_list.remove(2)
linked_list.remove(9)
print("............")
linked_list.print_all()
# print(linked_list[7])
print(".............")
linked_list[5] = 10000
linked_list.print_all()


stack = Stack()
stack.push(1)
print(stack.peek())
print(stack.pop())
print(stack.push(None))