import pytest
import sys
import os
import importlib.util

# Helper to import module with dashes in name
def load_module(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Construct path to the solution file relative to this test file
current_dir = os.path.dirname(os.path.abspath(__file__))
solution_path = os.path.join(current_dir, '..', '0002-Add-Two-Numbers.py')
solution_module = load_module(solution_path, 'solution_0002')
Solution = solution_module.Solution
ListNode = solution_module.ListNode

# Helpers for testing Linked Lists
def create_linked_list(arr):
    if not arr:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_add_two_numbers_example_1():
    solution = Solution()
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    # 342 + 465 = 807 -> [7, 0, 8]
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8]

def test_add_two_numbers_example_2():
    solution = Solution()
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    # 0 + 0 = 0
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0]

def test_add_two_numbers_example_3():
    solution = Solution()
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    # 9999999 + 9999 = 10009998 -> [8, 9, 9, 9, 0, 0, 0, 1]
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

def test_add_two_numbers_diff_len():
    solution = Solution()
    l1 = create_linked_list([1, 8]) # 81
    l2 = create_linked_list([0])    # 0
    # 81 + 0 = 81 -> [1, 8]
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [1, 8]
