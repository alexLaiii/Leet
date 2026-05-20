"""
Build the prefix common array by tracking numbers that have appeared
in exactly one of the two prefixes so far.

Since A and B are permutations, each number appears once in each array.
The set `seen` stores values that have been seen only once total.
When we see a value that is already in `seen`, that means it has now
appeared in both prefixes, so it becomes a common value. We increment
`common` and remove it from `seen`.

After processing A[i] and B[i], `common` equals the number of values
that appear in both A[:i+1] and B[:i+1].

Time: O(n)
Space: O(n)
"""

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        seen = set()
        res = [0] * N
        common = 0
        for i in range(N):
            valA, valB = A[i], B[i]
            if valA not in seen:
                seen.add(valA)
            else:
                common += 1
                seen.remove(valA)
            if valB not in seen:
                seen.add(valB)
            else:
                common += 1
                seen.remove(valB)
            res[i] = common                
        return res
        
        
        
        
