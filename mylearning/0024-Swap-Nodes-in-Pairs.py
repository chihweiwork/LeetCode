from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle the head swap easily
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Swapping logic
            # 1. Point the previous node's next to the second node
            prev.next = second
            # 2. Point the first node's next to the node after the second
            first.next = second.next
            # 3. Point the second node's next back to the first node
            second.next = first
            
            # Move the pointer forward for the next pair
            prev = first
            
        return dummy.next
