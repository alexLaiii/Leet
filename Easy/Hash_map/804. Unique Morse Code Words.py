"""
Too Easy, not bother to write a docstring
"""
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        res = 0
        for w in words:
            morse = ""
            for c in w:
                idx = ord(c) - 97
                morse += morse_table[idx]
            if morse not in seen:
                res += 1
                seen.add(morse)
        
        return res
