from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy node to simplify cases like removing the head node
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Advance fast pointer so that the gap between fast and slow is n nodes
        for _ in range(n + 1):
            fast = fast.next
            
        # Move fast to the end, maintaining the gap
        while fast:
            fast = fast.next
            slow = slow.next
            
        # slow.next is the node to be removed
        slow.next = slow.next.next
        
        return dummy.next
