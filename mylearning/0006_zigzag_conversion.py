class Solution:
    def convert(self, s: str, numRows: int) -> str:
        _result = ["" for x in range(numRows)]

        arrow = 1
        step = 0

        for char in s:
            _result[step] += char

            if step == 0:
                arrow = 1
            elif step == numRows-1:
                arrow = -1

            if numRows > 1:
                step += arrow
        
        return "".join(_result)
