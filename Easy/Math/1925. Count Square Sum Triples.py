"""
Count the number of square sum triples (a, b, c) such that:
    1 <= a, b, c <= n  and  a^2 + b^2 = c^2.

The loops iterate over all integer triples with 1 <= a <= b <= c <= n.
Whenever a^2 + b^2 equals c^2, the result is increased by 2 to account
for both ordered pairs (a, b, c) and (b, a, c).

Note that a == b cannot occur in a valid triple with positive integers,
since 2a^2 = c^2 has no integer solutions for a > 0, so this doubling
never over-counts.

Time Complexity:
    O(n^3) – three nested loops over a, b, and c up to n.
Space Complexity:
    O(1) – only a few integer variables are used.
"""

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        
        for a in range(1,n + 1):
            for b in range(a, n + 1):
                for c in range(b, n + 1):
             
                    if a ** 2 + b ** 2 == c ** 2:
                        res += 2
        return res
                        
             
            
