import pytest
from .test_utils import load_solution

solution_module = load_solution("0031-Next-Permutation.py")
Solution = solution_module.Solution

def test_next_permutation_example_1():
    sol = Solution()
    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    assert nums == [1, 3, 2]

def test_next_permutation_example_2():
    sol = Solution()
    nums = [3, 2, 1]
    sol.nextPermutation(nums)
    assert nums == [1, 2, 3]

def test_next_permutation_example_3():
    sol = Solution()
    nums = [1, 1, 5]
    sol.nextPermutation(nums)
    assert nums == [1, 5, 1]

def test_next_permutation_single():
    sol = Solution()
    nums = [1]
    sol.nextPermutation(nums)
    assert nums == [1]

def test_next_permutation_complex():
    sol = Solution()
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    # First decreasing from right is 4 (at index 3)
    # Just larger than 4 is 5 (at index 6)
    # Swap 4 and 5 -> [1, 5, 8, 5, 7, 6, 4, 3, 1]
    # Reverse after index 3 -> [1, 5, 8, 5, 1, 3, 4, 6, 7]
    sol.nextPermutation(nums)
    assert nums == [1, 5, 8, 5, 1, 3, 4, 6, 7]
