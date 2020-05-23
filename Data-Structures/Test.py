from LinkedList import *
from DoublyLinkedList import *


print(" ===== Test LinkedList =====")
linked_list = LinkedList()
linked_list.append(0.2)
linked_list.append(1)
linked_list.append(0)
# print elements of the linked list
linked_list.print_all()

print(" ===== Test DoublyLinkedList =====")
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(4.5)
#print all elements of the doubly_linked_list
print("    print DoublyLinkedList from head to tail =>")
doubly_linked_list.print_from_head_to_tail()
print("    print DoublyLinkedList from tail to head =>")
doubly_linked_list.print_from_tail_to_head()
