"""
This problem is very similar to  438: Find All Anagrams in a String. Revisit that problem if I forget:
Intuition:
Since the problem specify it only contains lower case letter,
We can use an counting array of size 26 to keep track of the count of each character
A permutation of string is, if their character count are the same, then one is the permutation of the other,
that is, if s1_count == substring_count, then it is substring is a permutation of s1.
With that information, we can initialize two counting array, s1_count, subs_count
s1_count store the counting of s1, where s1 is the target string to find
subs_count store the counting of a substring in s2, use it to compare to s1_count

initialize s1_count, so s1_count represent s1 correctly, in the code, I loop through s2 and store it to subs_table at the same time as a small optimization
so I can compare two counting array imiatedly after the first loop, but this is just optimization and its not necessary

inialize i as a right pointer to keep track of the current window, such that i is the left pointer, j is the right pointer, i -> j is the current window
start looping at len(s1), since we already get the count of the first len(s1) character
if j - i >= len(s1), it means that the current window/substring is longer than s1, so it can't be the permutation of s1, we need to shrink the window
take out the left most character from the counting array, that is "subs_count[ord(s2[i]) - ord("a")] -= 1],increment i by 1 to keep track of the current window
add the right most character to the window, that is "subs_count[ord(s2[j]) - ord("a")] += 1
check if s1_count == subs_count, if they are equal, then the current window is a permutation of s1, return True immediately

if nothing return after the loop, permutation is not found in any window/substring of s2, so we can safely return False



"""




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

            


                        
                        

            
                
                
                    

                    
                
        
