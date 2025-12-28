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

current_dir = os.path.dirname(os.path.abspath(__file__))
solution_path = os.path.join(current_dir, '..', '0004-Median-of-Two-Sorted-Arrays.py')
solution_module = load_module(solution_path, 'solution_0004')
Solution = solution_module.Solution

def test_find_median_sorted_arrays_example_1():
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0
    assert solution.findMedianSortedArrays(nums1, nums2) == expected

def test_find_median_sorted_arrays_example_2():
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    expected = 2.5
    assert solution.findMedianSortedArrays(nums1, nums2) == expected

def test_find_median_sorted_arrays_empty_one():
    solution = Solution()
    nums1 = []
    nums2 = [1]
    expected = 1.0
    assert solution.findMedianSortedArrays(nums1, nums2) == expected

def test_find_median_sorted_arrays_negative():
    solution = Solution()
    nums1 = [-5, -3]
    nums2 = [-2, -1]
    # Sorted merged: [-5, -3, -2, -1] -> (-3 + -2)/2 = -2.5
    expected = -2.5
    assert solution.findMedianSortedArrays(nums1, nums2) == expected

def test_find_median_sorted_arrays_large_diff():
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4, 5, 6, 7]
    # Sorted: [1, 2, 3, 4, 5, 6, 7] -> 4
    expected = 4.0
    assert solution.findMedianSortedArrays(nums1, nums2) == expected
