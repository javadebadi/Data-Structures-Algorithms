# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    reversed_list = None
    
    def update(reversed_list, head):
        if head is None:
            return reversed_list, None
        else:
            temp = head
            head = head.next
            temp.next = reversed_list
            reversed_list = temp
            return update(reversed_list, head)
        
    reversed_list, head = update(reversed_list, head)
    return reversed_list