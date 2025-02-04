class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposite = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if len(stack) == 0 or stack[-1] != opposite.get(char):
                stack.append(char)
            else:
                stack.pop()
        if stack:
            return False
        return True

        