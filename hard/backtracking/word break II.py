    """
    Solves the Word Break II problem using recursive DFS.

    Given a non-empty string `s` and a list of words `wordDict`, this function returns all possible
    sentences you can form by inserting spaces into `s` so that each resulting word is in the dictionary.

    The approach is to recursively try all prefixes of the string `s` and check if the prefix is a valid
    word (i.e., exists in `wordDict`). If it is, recursively solve the rest of the string (the suffix),
    and combine the current prefix with all valid sentence results returned from the suffix.

    Parameters:
    - s (str): The input string to be segmented.
    - wordDict (List[str]): The list of allowed dictionary words.

    Returns:
    - List[str]: A list of all valid sentences formed by breaking the input string into dictionary words.

    Example:
        Input: s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]
        Output: ["cats and dog", "cat sand dog"]

    Time Complexity:
    - Exponential in the worst case due to overlapping recursive calls.
    - Can be improved significantly with memoization.

    Notes:
    - This version does **not** use memoization, so it may recompute the same suffix multiple times.
    - Optimization tip: Add `@lru_cache` or use a `memo` dictionary to cache results for subproblems.

    Idea Summary:
    - Try every possible prefix of `s`.
    - If prefix is in `wordDict`, recursively solve the suffix.
    - Combine the prefix with each valid result from the suffix.
    """


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
       
        def dfs(s):
            res = []
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                suffix = s[i:]
                if prefix in wordSet:
                    if not suffix:
                        res.append(prefix)
                    else:
                        ans = dfs(suffix)
                        for each_string in ans:
                            res.append(prefix + " " + each_string)
            return res
        
        return dfs(s)

        
