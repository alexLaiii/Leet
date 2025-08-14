"""
Return, for each day, how many days you must wait to see a warmer temperature.

Core idea (monotonic stack):
- Maintain a stack of indices whose temperatures form a **strictly decreasing** sequence.
- As you scan left→right, for the current day i:
    * While the stack’s top day j is cooler (temps[j] < temps[i]),
      pop j and set res[j] = i - j (the next warmer day is i).
    * Push i so it can be resolved by some future warmer day.
- Days that never see a warmer future day remain 0.

Why it works:
- Each index is pushed once and popped at most once → O(n).
- The stack invariant (strictly decreasing temps) ensures that when a warmer day arrives,
  it resolves all strictly cooler days waiting for it in one pass.

Edge cases handled:
- Equal temps do not pop (need strictly warmer), so their res stays 0 unless a strictly warmer
  day appears later.
- Last elements naturally remain 0 if no warmer day exists.

Complexity:
- Time:  O(n) because each index is pushed/popped at most once.
- Space: O(n) for the stack and result array.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:            
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        return res
        
