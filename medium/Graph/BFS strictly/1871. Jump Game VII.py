"""
Use BFS to explore reachable indices, but avoid rescanning the same jump ranges.

Each reachable index i can jump to any position in:
    [i + minJump, i + maxJump]

A naive BFS would repeatedly scan overlapping ranges, which can become O(n^2).
To optimize this, we keep track of the farthest index that has already been
checked. For each popped index, we only scan from the first unchecked position
inside its jump range.

Whenever we find a '0', that index is reachable and is added to the queue.
If we reach the last index, return True.

Time Complexity: O(n), because each index is scanned at most once.
Space Complexity: O(n), for the queue in the worst case.
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        checked_idx_range = [float("inf"), float("-inf")]
        dq = deque([0])
        while dq:
            for i in range(len(dq)):
                curr_idx = dq.popleft()
                tocheck = [curr_idx + minJump, min(curr_idx + maxJump + 1, N)]
                if tocheck[0] < checked_idx_range[0]:
                    for j in range(tocheck[0], min(tocheck[1], checked_idx_range[0])):
                        if j >= N:
                            break
                        if j == N - 1:
                            return s[j] == "0"  
                        if s[j] == "0":
                            dq.append(j)
                           
                elif tocheck[1] > checked_idx_range[1]:
                    for j in range(max(0, checked_idx_range[1], tocheck[0]), min(tocheck[1], N)):
                        if j >= N:
                            break
                        if j == N - 1:
                            return s[j] == "0"  
                        if s[j] == "0":
                            dq.append(j)
                 
                checked_idx_range = min(checked_idx_range[0], tocheck[0]), min(max(checked_idx_range[1], tocheck[1]), N)
            
        return False
