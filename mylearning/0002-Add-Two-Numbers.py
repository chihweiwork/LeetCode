# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next	

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode(0)

        current = head
        carry_over = 0

        while (l1 is not None) or (l2 is not None) or (carry_over != 0):

            d1: int = l1.val if l1 else 0
            d2: int = l2.val if l2 else 0

            total = d1 + d2 + carry_over
            result = total % 10
            carry_over = total // 10

            current.next = ListNode(result)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next
