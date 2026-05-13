from copy import deepcopy
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = ""
        current_string = ""
        for x in s:
            current_string += x
            if len(list(current_string)) != len(set(list(current_string))):
                most_recent_occurrence = current_string[:-1].rfind(x)
                current_string = current_string[most_recent_occurrence+1:]
            if len(current_string) > len(longest_substring):
                longest_substring = deepcopy(current_string)
            #print(current_string)
        return len(longest_substring)
        