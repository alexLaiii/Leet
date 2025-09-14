"""
LeetCode 752: Open the Lock — BFS (level order)

Idea:
- Model each 4-digit combo as a node; edges are turning one wheel ±1 (with wrap-around).
- Use a queue for BFS from "0000", a `visited` set to avoid repeats, and a `deadend_set` to block invalid states.
- Expand level-by-level: iterate `len(dq)` items per layer; if we see `target`, return the current `shortest` turns.
- Generate neighbors by explicitly rolling one digit left/right (9↔0, 0↔9), matching the intuitive “turn the wheel” logic.

Why BFS:
- All moves cost 1, so the first time we reach `target` is the minimal number of turns.

Edge cases:
- If start or target is in deadends ⇒ return -1; if target == "0000" ⇒ return 0.

Complexity:
- ≤10⁴ states, ≤8 neighbors each ⇒ time O(10⁴), space O(10⁴).
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend_set = set(deadends)
        startpw = "0000"
        if target in deadend_set or startpw in deadend_set:
            return -1
        dq = deque([startpw])
        visited = set()
        visited.add(startpw)
        shortest = 0
        while dq:
            for i in range(len(dq)):
                currPw = dq.popleft()
                
                if currPw == target:
                    return shortest
                for j in range(len(currPw)):
                    for rotate in (-1, 1):
                        digit = int(currPw[j])
                        if rotate == 1 and digit == 9:
                            digit = 0
                        elif rotate == -1 and digit == 0:
                            digit = 9
                        else:
                            digit += rotate
                        newPw = currPw[:j] + str(digit) + currPw[j + 1:]
                        if newPw in visited or newPw in deadend_set:
                            continue
                        dq.append(newPw)
                        visited.add(newPw)
            shortest += 1
        return -1

