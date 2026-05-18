"""
Solve Jump Game IV using BFS over array indices.

Each index is treated as a node in a graph. From index i, we can move to:
1. i - 1
2. i + 1
3. any other index j where arr[j] == arr[i]

The dictionary `position` maps each value to all indices containing that value,
so same-value jumps can be found quickly. BFS is used because each BFS level
represents taking one more jump, so the first time we reach index N - 1, we have
found the minimum number of jumps.

Important optimization:
After processing all same-value jumps for a value `arr[i]`, clear that group
from `position`. Otherwise, we may repeatedly scan the same list of indices,
which can cause TLE for arrays with many repeated values.

Time Complexity: O(n)
- Each index is visited at most once.
- Each same-value group is scanned at most once.

Space Complexity: O(n)
- Used by the value-to-indices map, visited set, and BFS queue.
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        position = defaultdict(set)
        for i in range(N):
            position[arr[i]].add(i)
        
        visited = set([0])
        dq = deque([0])
        
        jump = 0
        while dq:
            for _ in range(len(dq)):
                curr_pos = dq.popleft()
                if curr_pos == N - 1:
                    return jump
                val = arr[curr_pos]
                for idx in position[val]:
                    if idx not in visited:
                        visited.add(idx)
                        dq.append(idx)
                position[val].clear()
                if curr_pos > 0 and curr_pos - 1 not in visited:
                    visited.add(curr_pos - 1)
                    dq.append(curr_pos - 1)
                if curr_pos + 1 < N and curr_pos + 1 not in visited:
                    visited.add(curr_pos + 1)
                    dq.append(curr_pos + 1)
            jump += 1
        return jump
                
            
        
        
