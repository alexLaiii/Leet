# This problem is very similar to Leetcode 438: Find All Anagrams in a String.
# Revisit that problem if I forget the technique.

# Intuition:
# Since the problem specifies that the strings only contain lowercase letters,
# we can use an array of size 26 to count character frequencies.

# Key Idea:
# Two strings are permutations if and only if their character counts are the same.
# So if s1_count == subs_count (a substring window in s2), then that window is a permutation of s1.

# Approach:
# 1. Initialize two arrays of size 26:
#    - s1_count: frequency of characters in s1 (the target pattern).
#    - subs_count: frequency of the current sliding window in s2.
#
# 2. Pre-fill s1_count with frequencies from s1.
#    Pre-fill subs_count with the first len(s1) characters from s2.
#
# 3. Start a sliding window from index len(s1) to end of s2:
#    - For each step:
#       a. Remove the leftmost character of the previous window.
#       b. Add the rightmost character of the new window.
#       c. Compare the updated subs_count with s1_count.
#          If they match, return True.
#
# 4. If no matching window is found, return False.

# Time Complexity: O(n) where n = len(s2), since we update the window in constant time.
# Comparing two 26-element arrays is O(1).


class Solution(object):
    def checkInclusion(self, s1, s2):
        # POSSIBLY SLIDING WINDOW
        # Version 2
        if len(s1) > len(s2):
            return False
        
        s1_table, subs_table = {},{}
        for i in range(len(s1)):
            s1_table[s1[i]] = 1 + s1_table.get(s1[i], 0)
            subs_table[s2[i]] = 1 + subs_table.get(s2[i], 0)

        if s1_table == subs_table: return True
        
        i = 0
        for j in range(len(s1),len(s2)):
            if j - i >= len(s1):
                subs_table[s2[i]] -= 1
                if subs_table[s2[i]] == 0:
                    subs_table.pop(s2[i])
                i += 1
            subs_table[s2[j]] = 1 + subs_table.get(s2[j], 0)
            if subs_table == s1_table:
                return True
    
        return False

        # # Edge case: s2 must longer than s1, so s1 can be a substring of s2
        # if len(s1) > len(s2):
        #     return False
        # # store the character count of string s1, and the substring representing substring of s2
        # s1_count,subs_count = [0] * 26, [0] * 26
        # for i in range(len(s1)):
        #     s1_count[ord(s1[i]) - ord("a")] += 1
        #     subs_count[ord(s2[i]) - ord("a")] += 1

        # if s1_count == subs_count:
        #     return True
        # # Key idea: a permutation substring from s2 must be the same length as s1
        # i = 0
        # for j in range(len(s1), len(s2)):
        #     if j - i >= len(s1):
        #         subs_count[ord(s2[i]) - ord("a")] -= 1
        #         i += 1
        #     subs_count[ord(s2[j]) - ord("a")] += 1
        #     if subs_count == s1_count:
        #         return True
        # return False

            


                        
                        

            
                
                
                    

                    
                
        
