class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the value to symbol mapping in descending order
        # Including the special subtraction cases (4, 9, 40, 90, 400, 900)
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        res = []
        for value, symbol in value_map:
            if num == 0:
                break
            # Count how many of this symbol can fit into num
            count, num = divmod(num, value)
            res.append(symbol * count)
            
        return "".join(res)