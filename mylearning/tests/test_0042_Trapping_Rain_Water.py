import pytest
from .test_utils import load_solution

solution_module = load_solution("0042-Trapping-Rain-Water.py")
Solution = solution_module.Solution

def test_trap_example_1():
    sol = Solution()
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

def test_trap_example_2():
    sol = Solution()
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9

def test_trap_empty():
    sol = Solution()
    assert sol.trap([]) == 0

def test_trap_no_water():
    sol = Solution()
    assert sol.trap([1, 2, 3, 4]) == 0
    assert sol.trap([4, 3, 2, 1]) == 0

def test_trap_single_v_shape():
    sol = Solution()
    assert sol.trap([3, 0, 3]) == 3
