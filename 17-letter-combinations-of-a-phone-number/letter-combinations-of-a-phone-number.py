from copy import deepcopy

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        combinations = [""]
        for digit in digits:
            possible_letters = digit_mappings[digit]
            new_combinations = []
            for combination in combinations:
                for letter in possible_letters:
                    new_combinations.append(combination + letter)
            combinations = deepcopy(new_combinations)
        return combinations