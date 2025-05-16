"""
Intuition:

Since given the input array can only contained character [a-z], we can create 2 constant size array to store the characters count of strings p and substring s
Use the sliding window techquie, curr_head is for tracking the current tracking header of the substring, the for loop i is the last character of the current substring
keep track of the counting array of the substring is equal to the counting array of p or not, if it i equal, add curr_head to the results, since this is the start of a
substring that represent an anagram. If the substring is longer than the string p, remove the curr_head character and increase curr_head by 1, since 
it cant be the head as the number of characters not match. we discard the curr_head element by decrease 1 of the related curr_head character in the substring counting array.

Time compelxity: O(n) -> n == len(s)
Space compelxity O(1) -> map is constant size 26 storing count of (a-z)

"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        # Need O(n)

        if len(s) < len(p): return []
        #counter_p, counter_subs  = [0] * 26, [0] * 26
        counter_p, counter_subs = [0] * 26, [0] * 26
        results, maps = [], {}
        curr_head =  0
      

        for i in range(len(p)):
            counter_p[ord(p[i]) - ord("a")] += 1
            counter_subs[ord(s[i]) - ord("a")] += 1
        
        maps[tuple(counter_p)] = 0
        if tuple(counter_subs) in maps:
            results.append(0)
           
        for i in range(len(p), len(s)):

            if i - curr_head >= len(p):
                counter_subs[ord(s[curr_head]) - ord("a")] -= 1
                curr_head += 1
        
            counter_subs[ord(s[i]) - ord("a")] += 1
            if tuple(counter_subs) in maps:
                results.append(curr_head)
                counter_subs[ord(s[curr_head]) - ord("a")] -= 1
                curr_head += 1


        return results
            
            
            


        
