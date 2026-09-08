"""
Count total commas used writing 1..n in standard format.

Given n <= 10^5, every number has at most 6 digits, so it can
only ever pick up one comma (the thousands separator). A number
gets that comma iff it is >= 1000, so the answer is just the
count of integers in [1000, n].
"""

class Solution:
    def countCommas(self, n: int) -> int:
        # Since 10^5 is 100,000
        return n - 999 if n - 999 > 0 else 0        
