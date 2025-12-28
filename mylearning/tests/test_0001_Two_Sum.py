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
solution_path = os.path.join(current_dir, '..', '0001-Two-Sum.py')
solution_module = load_module(solution_path, 'solution_0001')
Solution = solution_module.Solution

def test_two_sum_example():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert sorted(solution.twoSum(nums, target)) == expected

def test_two_sum_example_2():
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    assert sorted(solution.twoSum(nums, target)) == expected

def test_two_sum_same_elements():
    solution = Solution()
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    assert sorted(solution.twoSum(nums, target)) == expected

def test_two_sum_negative_numbers():
    solution = Solution()
    nums = [-1, -2, -3, -4, -5]
    target = -8
    expected = [2, 4]
    assert sorted(solution.twoSum(nums, target)) == expected

def test_two_sum_no_solution():
    solution = Solution()
    nums = [1, 2, 3]
    target = 7
    expected = []
    assert solution.twoSum(nums, target) == expected