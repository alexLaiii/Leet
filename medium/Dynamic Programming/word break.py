"""
Idea:
Using bottom-up Dynamic Programming, we decide whether each prefix of the string `s` can be written as a combination of words from `wordDict`.

Why DP?
We store the results of previous substring checks so that for any current substring, if removing a word from the end leaves a prefix that was already marked `True`, 
we can confidently say the current substring is also valid.

Explanation:
Let s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
We initialize a DP array where dp[i] is True if s[:i] can be segmented.
We set dp[0] = True since the empty string is always valid.

Step-by-step walkthrough:
Initial DP: [True, False, False, False, False, False, False, False, False, False]

- i = 1 → s[:1] = "c" → No match
- i = 2 → s[:2] = "ca" → No match
- i = 3 → s[:3] = "cat" → "cat" matches, "cat" - "cat" = "", dp[0] = True → set dp[3] = True
  DP: [True, False, False, True, False, False, False, False, False, False]
- i = 4 → s[:4] = "cats" → "cats" matches, "cats" - "cats" = "", dp[0] = True → set dp[4] = True
  DP: [True, False, False, True, True, False, False, False, False, False]
- i = 5, 6 → No matches
- i = 7 → s[:7] = "catsand"
    - "sand" matches end, s[3:7] = "sand", dp[3] = True → set dp[7] = True
    - or "and" matches end, s[4:7] = "and", dp[4] = True → also valid
  DP: [True, False, False, True, True, False, False, True, False, False]
- i = 8 → "o" → No match
- i = 9 → "og" → "dog" would match but s[6:9] = "dog" and dp[6] = False → can't mark dp[9]

Final result:
dp = [True, False, False, True, True, False, False, True, False, False]
Return dp[len(s)] → dp[9] = False → Cannot segment "catsandog" using given dictionary

Time Complexity:
O(n * k * l)
- n = len(s)
- k = number of words in wordDict
- l = average length of each word

Space Complexity:
O(n)
- For the DP array storing segmentation validity
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(dp)):
            for e in wordDict:
                if i >= len(e) and s[i- len(e):i] == e and dp[i - len(e)]:
                    dp[i] = True
                    break
        return dp[-1]
"""
Solution 2:
Top-down recursion with memories
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)
        cache = {}
        def dfs(word):
            if not word:
                return True
            if word in cache:
                return cache[word]
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]
                if (prefix in wordDict_set and suffix in wordDict_set) or (prefix in wordDict_set and dfs(suffix)):
                    cache[word] = True
                    return True
            cache[word] = False
            return False
        return dfs(s)
        

        
        

        
