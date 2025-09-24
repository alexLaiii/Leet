"""
LeetCode 853 — Car Fleet (Core idea)

Compute each car’s arrival time to the target, then process cars in order of
decreasing position (The car has a starting postion nearest to target go first). Maintain a stack of *fleet arrival
times* that is strictly increasing from bottom to top.

For each car:
  - time = (target - position) / speed
  - Push time onto the stack.
  - If this time ≤ the previous top time, the current car cannot overtake the
    fleet ahead before the target and thus merges into it, so we pop the
    pushed time (no new fleet formed).

Why this works:
- Sorting by position in reverse ensures we only consider catching up to cars ahead.
- A car (or group) with a larger arrival time is “slower.” 
  If a following car’s time ≤ the top fleet’s time, it catches that fleet before the target and adopts
  the slower fleet time; otherwise it forms a new fleet, Therefore, we pop the following car's time
  since this car's will join the top fleet and adopts the slower fleet time anyways.
  
  If a following car's time > the top fleet's time, this car will never catches the top fleet, so it becomes the new top fleet
  ** Note that it become new top fleets because this fleet is the slowest independent fleet right now and future cars will be block and adopt the speed of this fleet no matter how fast it is **
- The stack ends up holding exactly one arrival time per fleet.

Returns:
- Number of fleets = len(stack).

Complexity:
- Time: O(N log N) for sorting + O(N) scan
- Space: O(N) in the worst case (all cars form distinct fleets)
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        ps_pair = []
        stack = []
        for i in range(N):
            ps_pair.append([position[i], speed[i]])
        
        ps_pair.sort(reverse = True)
        
        for i in range(N):
            time = (target - ps_pair[i][0]) / ps_pair[i][1]
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        p_t_pair = []
        for i in range(N):
            t = (target - position[i]) / speed[i]
            p_t_pair.append([position[i], t])
        
        p_t_pair.sort(reverse = True)
        
        slowest_t = p_t_pair[0][1]
        fleet = N
        for i in range(1, N):
            if p_t_pair[i][1] <= slowest_t:
                fleet -= 1
            slowest_t = max(p_t_pair[i][1], slowest_t)
        return fleet


            
