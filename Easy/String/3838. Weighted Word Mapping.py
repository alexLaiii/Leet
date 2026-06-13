"""
1. For each word, sum character weights using weights[c - 'a']
2. Take the sum modulo 26
3. Map the value to a character using reverse order: char = 'z' - value
4. Append all mapped characters in order to form the result string
"""
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for w in words:
            weight = 0
            for c in w:
                weight += weights[ord(c) - ord('a')]
            val = weight % 26
            res += chr(ord('z') - val)
        return res
            
        
