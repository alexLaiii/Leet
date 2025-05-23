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

"""
Below is the optimal solution. Instead of comparing the entire size-26 array in each loop (which causes O(26n) time complexity),
we can optimize it to flat O(n).

Solution:
We create a `matches` variable to track how many character counts match between `s1` and the current substring window of `s2`.

First, we create the correct character frequency arrays `s1_count` and `subs_count`.
Then we loop through both arrays once to count how many characters already match, and store that in `matches` (O(26) here).

If `matches` is 26 at this point, it means the first `len(s1)` characters of `s2` already form a permutation of `s1`,
so we can return True immediately.

Enter the main loop:
Since we remove the leftmost character and add a new character from `s2` into the sliding window each time,
we need to check how the number of matches changes.

First, we record the decrement of the leftmost character.
Then check if the count of the leftmost character is equal to `s1_count`:
- If it equals, this means the decrement **caused it to equal**, so `matches += 1`.
- If not equal, then there are two conditions:
  1. They were not equal before decrement.
  2. They were equal before decrement.
So we need to check if `subs_count[s2[left]] + 1 == s1_count[s2[left]]`:
    - If they are equal, it means scenario 2 → `matches -= 1`.
    - If they are not equal, it means scenario 1 → do nothing.

Same logic applies for the added character when updating matches.

At any point, if `matches == 26`, it means the current window is a valid permutation of `s1`, so return True.

If nothing is returned after the loop ends, it means no permutation was found → return False.
"""



class Solution(object):
    def checkInclusion(self, s1, s2):
        # Optimize solution O(26n) -> O(n)

        if len(s1) > len(s2): return False
        s1_count, subs_count, matches = [0] * 26,[0] * 26, 0
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            subs_count[ord(s2[i]) - ord("a")] += 1
        
        for i in range(len(s1_count)):
            if s1_count[i] == subs_count[i]:
                matches += 1
        if matches == 26: return True
        left = 0
        for right in range(len(s1), len(s2)):
            if right - left + 1 > len(s1):
                subs_count[ord(s2[left]) - ord("a")] -= 1
                if subs_count[ord(s2[left]) - ord("a")] == s1_count[ord(s2[left]) - ord("a")]:
                    matches += 1
                elif subs_count[ord(s2[left]) - ord("a")] + 1 == s1_count[ord(s2[left]) - ord("a")]:
                    matches -= 1
                # the last case is if the decrement has no effect on the result, example initially is 3, we want 1, 3-1 = 2, so is still unmatch, but the value is unmatch before decrement, so we dont do anything to the matches
                left += 1

            subs_count[ord(s2[right]) - ord("a")] += 1
            if subs_count[ord(s2[right]) - ord("a")] == s1_count[ord(s2[right]) - ord("a")]:
                matches += 1
            elif subs_count[ord(s2[right]) - ord("a")] - 1 == s1_count[ord(s2[right]) - ord("a")]:
                matches -= 1
    
            if matches == 26: return True
 
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

            


                        
                        

            
                
                
                    

                    
                
        
