"""
Solution: Letter Combinations of a Phone Number

We use a recursive approach (depth-first search):

1. Create a map (keyboard) that maps each digit to its corresponding characters,
   e.g., '2' → "abc", '3' → "def", etc.

2. Initialize a result list to store all valid combinations.

3. Define the recursive function:
   - Base case:
     If char_level == len(digits), we have built a complete combination.
     For example, if digits = "23":
       - char_level = 0 → digit '2'
       - char_level = 1 → digit '3'
       - char_level = 2 → end of digits → add word to result

   - Recursive case:
     For the current digit at char_level, get its mapped characters.
     Loop through each character:
       - Append that character to the current word
       - Recurse to the next digit level (char_level + 1)

4. As recursion unfolds:
   - Each call explores a different path (e.g., "a" → "ad", "ae", ...)
   - Once a full combination is built, it is added to the result
   - The call stack unwinds and continues with the next character

5. Return the result list after all combinations are generated.

Time complexity: O(4^n × n)
- 4^n → total number of combinations in the worst case
- n → time to build each combination string
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keyboard = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
            }
        result = []
        def letterCombHelper(word, char_level):
            if char_level == len(digits):
                if word:
                    result.append(word)
                return
            
            letters = keyboard[digits[char_level]]
            for char in letters:
                letterCombHelper(word + char, char_level + 1)
        
        letterCombHelper("", 0)
        return result
            

            

  
            
            
            
                
                
