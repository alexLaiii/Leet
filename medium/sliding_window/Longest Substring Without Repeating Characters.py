###
Use a hash map to store the last index of each character.

Keep a cutoff pointer (cutoff) to mark the start of the current non-repeating window.

If a repeat is found after the cutoff:

Update cutoff to the last seen index of that character.

Update longest as current_index - cutoff.

Track the maximum length seen so far using prev_long.

Return max(longest, prev_long) at the end.
###


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        map ={}
        prev_long, longest, cutoff = 0, 0, 0
        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = i
                longest += 1
            else:
                prev_long = max(longest,prev_long)
                if(map[s[i]] > cutoff):
                    cutoff = map[s[i]]
                map[s[i]] = i
                longest = map[s[i]] - cutoff
                
        return max(longest,prev_long)


""" Version 2 but same idea """

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {}
        count,max_count, i= 0,0, 0
        for j in range(len(s)):
            if s[j] not in maps:
                maps[s[j]] = j
                count += 1
            else:
                if maps[s[j]] >= i:
                    i = maps[s[j]] + 1
                count = j - i + 1
                maps[s[j]] = j
            max_count = max(count,max_count)



        return max_count
            
