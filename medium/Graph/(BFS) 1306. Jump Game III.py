"""
Jump Game III

Idea:
Treat each index as a graph node. From index i, we can jump to:
    i - arr[i]
    i + arr[i]

Use BFS starting from start. If we ever reach an index where arr[index] == 0,
return True. Use a visited set to avoid cycles and repeated work.

Key detail:
Mark an index as visited when adding it to the queue, so each index is processed
at most once.

Time:  O(n)
Space: O(n)
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        visited = set([start])
        dq = deque([start])
        while dq:
            curr_pos = dq.popleft()
            if arr[curr_pos] == 0:
                return True
            left = curr_pos - arr[curr_pos]
            right = curr_pos + arr[curr_pos]
            if left not in visited and left >= 0:
                dq.append(left)
                visited.add(left)
            if right not in visited and right < N:
                dq.append(right)
                visited.add(right)
        return False
        
