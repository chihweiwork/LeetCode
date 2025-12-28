from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Use a dummy node to handle head changes easily
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Find the k-th node of the current group
            kth = self.get_kth(group_prev, k)
            if not kth:
                # If there are fewer than k nodes left, we are done
                break
            
            # The node after this group
            group_next = kth.next
            
            # 2. Reverse the current group
            # prev starts as group_next to connect the reversed group to the rest of the list
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                # Standard linked list reversal
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. Re-connect the reversed group to the previous part
            # The original first node of the group is now the last node
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next
        
    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
