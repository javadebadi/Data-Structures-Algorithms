from LinkedList import *
from DoublyLinkedList import *

print(" ===========================")
print(" ===== Test LinkedList =====")
print(" ===========================")
linked_list = LinkedList()
linked_list.append(0.2)
linked_list.append(1)
linked_list.append(0)
# print elements of the linked list
linked_list.print_all()
print("      Reverse LinkedList ======>")
linked_list.reverse().print_all()
print("      Prepend element to LinkedList =====>")
linked_list.prepend(-1000)
linked_list.prepend(-1000)
linked_list.print_all()
print("      Search value in elements of the LinkedList and return node =====>")
print(linked_list.search(-1000))
print("      Remove nodes with specfic value from LinkedList =====>")
linked_list.remove(-1000) # Removes first node with value -1000
linked_list.print_all()
print("      Chack pop method which return value of the first element and removes it")
print(linked_list.pop())
print("size of the linked array = {}".format(linked_list.size()))
print("     Insert")
linked_list.insert(-50,0)
linked_list.insert(50,10)
linked_list.insert(50,2)
#linked_list.insert(50,2.5)  #  will raise ValueError
linked_list.print_all()



print(" =================================")
print(" ===== Test DoublyLinkedList =====")
print(" =================================")
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(4.5)
#print all elements of the doubly_linked_list
print("    print DoublyLinkedList from head to tail =>")
doubly_linked_list.print_from_head_to_tail()
print("    print DoublyLinkedList from tail to head =>")
doubly_linked_list.print_from_tail_to_head()
