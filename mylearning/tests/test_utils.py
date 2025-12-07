import importlib.util
import os

def load_solution(file_name):
    """
    Loads a LeetCode solution module from the parent directory.
    The file name should be like '0001-Two-Sum.py'.
    """
    module_name = "solution_" + file_name.replace("-", "_").replace(".py", "")
    solution_file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", file_name)
    )

    spec = importlib.util.spec_from_file_location(module_name, solution_file_path)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    return solution_module
