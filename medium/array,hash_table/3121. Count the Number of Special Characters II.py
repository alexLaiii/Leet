"""
Approach:
Track the first occurrence index of each uppercase letter and the last
occurrence index of each lowercase letter.

For a letter to be special in this problem, both its lowercase and uppercase
forms must appear, and every lowercase occurrence must come before every
uppercase occurrence. This is equivalent to checking whether the first uppercase
index is greater than the last lowercase index.

We scan the word once:
- For uppercase letters, store only the first occurrence.
- For lowercase letters, keep updating the last occurrence.

Then we check all 26 letters and count the ones where:

    first_uppercase_index > last_lowercase_index

Time Complexity: O(n), where n is the length of word.
Space Complexity: O(1), since we use two fixed arrays of size 26.
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upperCase_first_occurence = [-1] * 26
        lowerCase_last_occurence = [-1] * 26
        for i in range(len(word)):
            ASCII_val = ord(word[i])
            # UpperCase
            if ASCII_val <= 91 and upperCase_first_occurence[ASCII_val-65] == -1:
                upperCase_first_occurence[ASCII_val-65] = i
            # LowerCase
            elif ASCII_val >= 97:
                lowerCase_last_occurence[ASCII_val - 97] = i
        res = 0

        for i in range(26):
            upper_idx = upperCase_first_occurence[i]
            lower_idx = lowerCase_last_occurence[i]
            if upper_idx != -1 and lower_idx != -1:
                if upper_idx > lower_idx:
                    res += 1
        return res
        
