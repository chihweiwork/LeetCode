import pytest
from .test_utils import load_solution

solution_module = load_solution("0046-Permutations.py")
Solution = solution_module.Solution

def test_permute_example_1():
    sol = Solution()
    nums = [1, 2, 3]
    result = sol.permute(nums)
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])
    assert len(result) == 6

def test_permute_example_2():
    sol = Solution()
    nums = [0, 1]
    result = sol.permute(nums)
    expected = [[0, 1], [1, 0]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

def test_permute_single():
    sol = Solution()
    assert sol.permute([1]) == [[1]]

def test_permute_empty():
    sol = Solution()
    # Problem says nums.length >= 1, but good to handle
    assert sol.permute([]) == [[]]
