"""
LeetCode 45 - Jump Game II

Greedy Idea:
At every position, examine all positions reachable in ONE jump and choose
the next position that gives the farthest future reach.

Suppose we are currently at index i.

We can jump to:
    i+1, i+2, ..., i+nums[i]

For each candidate position j, compute:
    j + nums[j]

which represents the farthest index reachable AFTER landing at j.

The greedy choice is:
    move to the position with the maximum future reach.

Why this works:
The goal is to minimize the number of jumps, so each jump should maximize
how much progress we can make toward the end. Since the problem guarantees
the last index is reachable, we never need to handle dead-end cases.

Algorithm Steps:
1. Start at index 0.
2. Check every position reachable from the current position.
3. Choose the position that maximizes:
       next_position + nums[next_position]
4. Move there and increase jump count.
5. If any reachable position can directly reach the last index,
   return jump + 1 immediately.

Example:
    nums = [2,3,1,1,4]

Start at index 0:
    reachable: index 1 and 2

    index 1 -> future reach = 1 + 3 = 4
    index 2 -> future reach = 2 + 1 = 3

Greedy picks index 1 because it reaches farther.

Then from index 1:
    can directly reach the end.

Total jumps = 2.

Time Complexity:
    Worst case can approach O(n^2),
    because for each chosen position we scan all reachable positions.

Space Complexity:
    O(1)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        jump = 0
        curr_pos = 0
        # Since the problem guaranteed that you can reach nums[n - 1], no need to consider failed cases
        while True:
            steps = nums[curr_pos]
            furthest = curr_pos + nums[curr_pos]
            temp_pos = curr_pos
            for j in range(1, steps + 1):
                if curr_pos + j >= N - 1:
                    return jump + 1
                else:
                    if curr_pos + j + nums[curr_pos + j] >= furthest:
                        furthest = curr_pos + j + nums[curr_pos + j]
                        temp_pos = curr_pos + j
            
            curr_pos = temp_pos
            jump += 1
        
                

