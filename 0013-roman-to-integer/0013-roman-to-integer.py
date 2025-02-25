class Solution:
    def romanToInt(self, s: str) -> int:
        number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        edge_case = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        total = 0
        previous = ''
        for char in s:
            if edge_case.get(previous+char):
                total -= number[previous]
                total +=edge_case[previous+char]
            else:
                total += number[char]
            previous = char
        return total
            
