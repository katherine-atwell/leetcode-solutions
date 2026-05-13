from copy import deepcopy
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substring = ""
        for i in range(len(s)):
            palindrome = True
            offset = 0
            while palindrome and i - offset >= 0:
                substring_odd = s[i-offset:i+offset+1]
                substring_even = s[i-offset:i+offset]
                #print("odd substring:", substring_odd)
                #print("even substring:", substring_even)
                #print("first half (odd):", substring_odd[:offset])
                #print("second half (odd):", substring_odd[offset+1:][::-1])
                #print("first half (even):", substring_even[:offset])
                #print("second half (even):", substring_even[offset:][::-1])
                odd_palindrome = False
                even_palindrome = False
                if len(substring_odd) == 1 or (substring_odd[:offset] == substring_odd[offset+1:][::-1]):
                    odd_palindrome = True
                elif len(substring_even) == 0 or substring_even[:offset] == substring_even[offset:][::-1]:
                    even_palindrome = True
                if not odd_palindrome and not even_palindrome:
                    palindrome = False
                    pass
                elif odd_palindrome and len(substring_odd) > len(longest_substring) and len(substring_odd) <= 1000:
                    longest_substring = deepcopy(substring_odd)
                    #print("longest_substring:", longest_substring)
                elif even_palindrome and len(substring_even) > len(longest_substring) and len(substring_even) <= 1000:
                    longest_substring = deepcopy(substring_even)
                    #print("longest_substring:", longest_substring)
                offset += 1
        return longest_substring
