class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        bracket_options = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        for char in s:
            if char in bracket_options.keys():
                brackets.append(char)
            elif char in bracket_options.values():
                if len(brackets) > 0 and bracket_options[brackets[-1]] == char:
                    brackets.pop()
                else:
                    return False
            
        if len(brackets) > 0:
            return False
        return True