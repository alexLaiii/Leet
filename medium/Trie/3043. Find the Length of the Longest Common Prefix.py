"""
Build a Trie from all numbers in arr1, treating each number as a string of digits.
Then for each number in arr2, walk through the Trie digit by digit and count how
many digits match before the path breaks. The maximum matched length over all
numbers in arr2 is the longest common prefix length.

Time: O(total digits in arr1 + total digits in arr2)
Space: O(total digits in arr1)
"""

class TrieNode:
    def __init__(self):
        self.node = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Idea: put arr1 into trie
        trieRoot = TrieNode()
        for num in arr1:
            currNode = trieRoot
            num = str(num)
            for d in num:
                if d not in currNode.node:
                    currNode.node[d] = TrieNode()
                currNode = currNode.node[d]
        res = 0   
        for num in arr2:
            currNode = trieRoot
            count = 0
            num = str(num)
            for d in num:
                if d not in currNode.node:
                    break
                currNode = currNode.node[d]
                count += 1
            res = max(count, res)
        return res
