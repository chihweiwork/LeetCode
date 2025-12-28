import pytest
from .test_utils import load_solution

solution_module = load_solution("0038-Count-and-Say.py")
Solution = solution_module.Solution

def test_count_and_say_example_1():
    sol = Solution()
    assert sol.countAndSay(1) == "1"

def test_count_and_say_example_2():
    sol = Solution()
    assert sol.countAndSay(4) == "1211"

def test_count_and_say_n2():
    sol = Solution()
    assert sol.countAndSay(2) == "11"

def test_count_and_say_n3():
    sol = Solution()
    assert sol.countAndSay(3) == "21"

def test_count_and_say_n5():
    sol = Solution()
    assert sol.countAndSay(5) == "111221"
