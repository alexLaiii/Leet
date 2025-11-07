"""
Monotonic stack (strictly decreasing prices).
Invariant:
- Stack holds pairs (price, day).
- After popping all prices <= current price, the new top (if any) is
  the nearest previous day with a strictly greater price.
Span logic:
- If such a day exists, span = curr_day - prev_greater_day.
- Otherwise, span = curr_day (all days so far).
Amortized O(1) time per call, O(n) space over n calls.
"""

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.stockCount = 1
    def next(self, price: int) -> int:
        
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        self.stack.append((price, self.stockCount))
        self.stockCount += 1
        if len(self.stack) > 1:
            return self.stack[-1][1] - self.stack[-2][1]
        else:
            return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
