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
solution_path = os.path.join(current_dir, '..', '0019-Remove-Nth-Node-From-End-of-List.py')
solution_module = load_module(solution_path, 'solution_0019')
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

def test_remove_nth_example():
    sol = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    result = sol.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [1, 2, 3, 5]

def test_remove_nth_head():
    sol = Solution()
    head = create_linked_list([1, 2])
    result = sol.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [2]

def test_remove_nth_only_one():
    sol = Solution()
    head = create_linked_list([1])
    result = sol.removeNthFromEnd(head, 1)
    assert linked_list_to_list(result) == []
