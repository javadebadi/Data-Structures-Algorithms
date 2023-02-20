# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]


        Time Complexity: O(n)
        Memoery: O(n)
        """
        head = None
        p1 = list1
        p2 = list2
        
        # define head
        if p1 is not None and p2 is not None:
            if p1.val < p2.val:
                head = ListNode(val=p1.val)
                p1 = p1.next
            else:
                head = ListNode(val=p2.val)
                p2 = p2.next
        elif p1 is not None:
            head = ListNode(val=p1.val)
            p1 = p1.next
        elif p2 is not None:
            head = ListNode(val=p2.val)
            p2 = p2.next
        else:
            head = None
            
        # find other elements
        current = head
        while (
            p1 is not None or p2 is not None
        ):
            if p1 is not None and p2 is not None:
                if p1.val < p2.val:
                    current.next = ListNode(val=p1.val)
                    p1 = p1.next
                else:
                    current.next = ListNode(val=p2.val)
                    p2 = p2.next
            elif p1 is not None:
                current.next = ListNode(val=p1.val)
                p1 = p1.next
            elif p2 is not None:
                current.next = ListNode(val=p2.val)
                p2 = p2.next
            
            current = current.next
        
        return head