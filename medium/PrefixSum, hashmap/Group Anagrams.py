"""
Intuition
We count the number of occurence for each character on each string,
if the number of occurence between two string is the same, then they must be Anagram of each other, so we can group them into a subarray, and append it to the big array.

Note: This appraoch only works if you know what is going to be in the strings, in this case, only a-z.

Approach: 
results: An array to group the final result
count: Each index represent a lower case character, the value of count[i] represent the counted number of that character
maps: Use count as a key, to gain O(1) complexity for comparision
index: keep track of the position on where each group on strings should be place in the results array

Notes: I cast tuple() type to the count array because array is not hashable in python, but tuple is.

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """       
        # optimal solution O(m*n)/O(m*n)
        maps, results, index = {}, [], 0
        for i in range(len(strs)):
            # reset the counts for each string
            count = [0] * 26
            for char in strs[i]:
                count[ord(char)-ord("a")] += 1
            count = tuple(count)
            if count not in maps:
                maps[count] = index
                results.append([strs[i]])
                index += 1
            else:
                results[maps[count]].append(strs[i])
        
        return results



"""
Solution 2:
check the character count of each string in strs, store the counting array as a key into the hash_map, with the corresponding value as a list of strings
whenever hit a string with the same character count in hash_map, append that strings into that key:value,
If its a new_count (never happen before): create a new key in the hash_map

After all the strings is checked,
loop through the hash_maps and append all the value(these are list) to the result.

Time complexity: 
O(n * m) -> n is the number of strings in strs, m is the average length of each strings
Second loop -> the worst case is no string is a anagram of the other, so the hash_map would have size n, so it will be O(m*n + n)-> which simplify to O(m*n)
Space complexity:
O(1) for store the character count (fixed 26)
O(n + n) for stored the result and hash_map -> which simplifies to O(n)
"""

class Solution(object):
    def groupAnagrams(self, strs):
        res = []
        hash_table = {}
        for s in strs:
            s_count = [0] * 26
            for c in s:
                s_count[ord(c) - ord("a")] += 1
            hash_table[tuple(s_count)] = hash_table.get(tuple(s_count), [])
            hash_table[tuple(s_count)].append(s)
        
        for key in hash_table:
            res.append(hash_table[key])
        return res
        
        # O(m*nlogn)/O(m*n)
        # big_maps = {}
        # results = []
        # index = 0
        # for i in range(len(strs)):
        #         sort_s = "".join(sorted(strs[i]))
        #         if sort_s in big_maps:
        #             results[big_maps[sort_s]].append(strs[i])
        #         else:
        #             big_maps[sort_s] = index
        #             results.append([strs[i]])
        #             index += 1
        # return results



                

                
                
            
            
            
        
