import pytest
import importlib.util
from typing import List, Optional

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0002", "0002-Add-Two-Numbers.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution
ListNode = solution_module.ListNode

# Helper function to create a ListNode from a list
def create_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to convert a ListNode to a list
def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    if not node:
        return []
    items = []
    current = node
    while current:
        items.append(current.val)
        current = current.next
    return items

@pytest.mark.parametrize("l1_list, l2_list, expected_list", [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
])
def test_addTwoNumbers(l1_list: List[int], l2_list: List[int], expected_list: List[int]):
    s = Solution()
    l1 = create_linked_list(l1_list)
    l2 = create_linked_list(l2_list)
    result_node = s.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result_node)
    assert result_list == expected_list
