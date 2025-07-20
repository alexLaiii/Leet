"""
Returns all words in the input list that are concatenations of at least two shorter words
from the same list.

    Approach:
    - Use DFS with memoization to check if each word can be formed by concatenating
    other words from the list.
    - For each word, we try every possible split into prefix and suffix:
    - If the prefix is a valid word and the suffix is also a valid word or can be 
      recursively broken into valid words, then the word is a valid concatenated word.
    - To avoid using the word itself as one of its parts, we temporarily remove it from
    the set during the check.

Optimization:
- The words are stored in a set to allow O(1) lookups.
- A cache (dictionary) is used to store results of previously computed words (memoization).

Time Complexity:
- Let N = number of words, L = maximum length of a word.
- Worst-case time complexity is approximately O(N * L^2), since for each word, we try
all split positions and recurse on suffixes.

Args:
words (List[str]): A list of strings representing the dictionary of words.

Returns:
List[str]: A list of all concatenated words that can be formed by joining at least
           two shorter words from the dictionary.
"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Convert the list into a set for O(1) lookups
        word_set = set(words)

        # Memoization cache to avoid recomputation
        cache = {}

        def dfs(word):
            """
            Recursive function to determine if `word` can be formed by concatenating 
            two or more other words from word_set.
            """
            if word in cache:
                return cache[word]
            
            # Try every possible split point
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                # Two valid cases:
                # 1. Both parts are in word_set
                # 2. Prefix is in word_set and suffix can be formed recursively
                if (prefix in word_set and suffix in word_set) or \
                   (prefix in word_set and dfs(suffix)):
                    cache[word] = True
                    return True

            # If no valid split found, mark as False
            cache[word] = False
            return False

        res = []
        for w in words:
            # Temporarily remove the current word to prevent using itself
            word_set.remove(w)
            if dfs(w):
                res.append(w)
            word_set.add(w)  # Add back for next iteration

        return res
