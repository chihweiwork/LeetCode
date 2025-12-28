import pytest
import os
import sys
import importlib.util

# Helper to import module with dashes in name
def load_module(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

current_dir = os.path.dirname(os.path.abspath(__file__))
solution_path = os.path.join(current_dir, '..', '0023-Merge-k-Sorted-Lists.py')
solution_module = load_module(solution_path, 'solution_0023')
Solution = solution_module.Solution
ListNode = solution_module.ListNode

# Helpers
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def test_merge_k_lists_example():
    sol = Solution()
    l1 = create_linked_list([1, 4, 5])
    l2 = create_linked_list([1, 3, 4])
    l3 = create_linked_list([2, 6])
    result = sol.mergeKLists([l1, l2, l3])
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]

def test_merge_k_lists_empty():
    sol = Solution()
    assert sol.mergeKLists([]) == None
    assert sol.mergeKLists([None]) == None

def test_merge_k_lists_one_list():
    sol = Solution()
    l1 = create_linked_list([1, 2, 3])
    result = sol.mergeKLists([l1])
    assert linked_list_to_list(result) == [1, 2, 3]
