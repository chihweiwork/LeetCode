import pytest
from .test_utils import load_solution

solution_module = load_solution("0006-ZigZag-Conversion.py")
Solution = solution_module.Solution

def test_zigzag_example_1():
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

def test_zigzag_example_2():
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

def test_zigzag_example_3():
    sol = Solution()
    assert sol.convert("A", 1) == "A"

def test_zigzag_numrows_1():
    sol = Solution()
    assert sol.convert("AB", 1) == "AB"

def test_zigzag_numrows_large():
    sol = Solution()
    assert sol.convert("ABC", 5) == "ABC"
