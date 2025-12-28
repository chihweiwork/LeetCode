import pytest
from .test_utils import load_solution

solution_module = load_solution("0045-Jump-Game-II.py")
Solution = solution_module.Solution

def test_jump_example_1():
    sol = Solution()
    assert sol.jump([2, 3, 1, 1, 4]) == 2

def test_jump_example_2():
    sol = Solution()
    assert sol.jump([2, 3, 0, 1, 4]) == 2

def test_jump_single():
    sol = Solution()
    assert sol.jump([0]) == 0

def test_jump_large_first():
    sol = Solution()
    # index 0 to index 10 (1 jump), index 10 to 11 (1 jump) = 2 jumps
    assert sol.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2

def test_jump_incremental():
    sol = Solution()
    assert sol.jump([1, 1, 1, 1]) == 3
