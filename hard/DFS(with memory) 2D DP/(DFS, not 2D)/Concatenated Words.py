class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        
        cache = {}
        def dfs(word):
            if word in cache:
                return cache[word]
            for  i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if (prefix in word_set and suffix in word_set) or (prefix in word_set and dfs(suffix)):
                    cache[word] = True
                    return True
            cache[word] = False
            return False
        res = []
        for w in words:
            if dfs(w):
                res.append(w)
        return res

        
