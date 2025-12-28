from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a min-heap to keep track of the smallest current node among all lists
        min_heap = []
        
        # Add the head of each non-empty list to the heap
        # Note: We include id(node) to handle cases where node.val is the same,
        # as ListNode is not directly comparable.
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Attach the smallest node to the result
            curr.next = node
            curr = curr.next
            
            # If the popped node has a next node, add it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
