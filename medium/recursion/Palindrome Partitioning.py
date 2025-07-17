"""
Approach: Backtracking with Palindrome Check + Memoization

Idea:
We use backtracking to explore all possible ways to partition the input string `s` such that
every substring in the partition is a palindrome.

Each recursive branch represents one possible partitioning path.
If at any point a substring is **not a palindrome**, we prune that branch early — there’s no need
to explore it further since it won’t lead to a valid result.

Example: For input "aab", the recursive tree might look like:

           "aab"
       /     |   \
     "a"    "aa" "aab"
     / \      |
   "a" "ab"  "b"
   /
 "b"

In this example, the partition path `["a", "ab"]` is invalid because `"ab"` is not a palindrome.
So we do not recurse down that branch.

Termination Condition:
When the `start` index reaches the end of the string (`start == len(s)`), it means we've formed
a complete and valid partition, so we add a copy of the current path to the result list.

Palindrome Check:
We define a helper function `isPalindrome(left, right)` to check whether substring `s[left:right+1]` is a palindrome
by comparing characters from both ends.

To avoid recomputing palindrome checks on repeated substrings across recursive calls,
we use a memoization cache (`cache[(left, right)]`) to store results of previous checks.
This significantly improves performance on large input strings with repeated characters.

Time Complexity (Worst Case):
- O(2^N * N), where:
  - 2^N is the number of ways to partition the string.
  - N is the time to copy a path or check a palindrome.
With memoization, palindrome checking becomes nearly O(1) amortized.

Space Complexity:
- O(N) for recursion depth and current path.
- O(N^2) for the cache storing palindrome results.
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cache = {}
        def isPalindrome(left, right):
            if (left, right) in cache:
                return cache[(left, right)]
            while left <= right:
                if s[left] != s[right]:
                    cache[(left, right)] = False
                    return False
                left += 1
                right -= 1
            cache[(left, right)] = True
            return True
        result = []
        def backtrack(start, partition):
            if start == len(s):
                result.append(partition.copy())
                return

            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    partition.append(s[start: i + 1])
                    backtrack(i + 1, partition)
                    partition.pop()
            
        backtrack(0, [])
        return result

        
