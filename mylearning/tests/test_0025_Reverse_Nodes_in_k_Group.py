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
solution_path = os.path.join(current_dir, '..', '0025-Reverse-Nodes-in-k-Group.py')
solution_module = load_module(solution_path, 'solution_0025')
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

def test_reverse_k_group_example_1():
    sol = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    result = sol.reverseKGroup(head, 2)
    assert linked_list_to_list(result) == [2, 1, 4, 3, 5]

def test_reverse_k_group_example_2():
    sol = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    result = sol.reverseKGroup(head, 3)
    assert linked_list_to_list(result) == [3, 2, 1, 4, 5]

def test_reverse_k_group_k1():
    sol = Solution()
    head = create_linked_list([1, 2, 3])
    result = sol.reverseKGroup(head, 1)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_reverse_k_group_all():
    sol = Solution()
    head = create_linked_list([1, 2])
    result = sol.reverseKGroup(head, 2)
    assert linked_list_to_list(result) == [2, 1]
