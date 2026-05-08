"""
For each query word, compare it against every word in dictionary.

Since all words have the same length, count how many character positions are
different between the query and the dictionary word. If the difference count is
at most 2, then the query is valid and can be added to the result.

Use early stopping:
- If the difference count becomes greater than 2, stop comparing that word.
- If one dictionary word matches within two edits, add the query once and move
  to the next query.

Time Complexity:
    O(Q * D * L), where Q = number of queries, D = number of dictionary words,
    and L = word length.

Space Complexity:
    O(1) extra space, excluding the result list.
"""
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for i in range(len(queries)):
            for w in dictionary:
                diff = 0
                for j in range(len(w)):
                    if queries[i][j] != w[j]:
                        diff += 1
                    if diff > 2:
                        break
                if diff <= 2:
                    res.append(queries[i])
                    break
        return res
                    
                
        
