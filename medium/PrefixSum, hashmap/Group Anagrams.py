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



                

                
                
            
            
            
        
