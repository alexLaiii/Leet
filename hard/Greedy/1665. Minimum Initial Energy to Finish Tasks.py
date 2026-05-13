"""
LeetCode 1665 - Minimum Initial Energy to Finish Tasks

Idea:
Each task has:
    actual  = energy spent after doing the task
    minimum = energy required before starting the task

The important greedy observation is that tasks with larger (minimum - actual)
should be done earlier. This value represents how much "extra energy buffer"
a task needs beyond the energy it consumes.

Example:
    actual = 2, minimum = 8
    minimum - actual = 6

This task requires a large amount of energy upfront but does not consume as
much, so delaying it can make it harder to satisfy later. Therefore, we sort
tasks in descending order of (minimum - actual).

After sorting, we binary search the minimum starting energy.

For a guessed starting energy:
    - simulate the tasks in the greedy order
    - before each task, check if current energy >= minimum
    - if yes, subtract actual
    - if any task cannot be started, the guess is too small

Binary search works because:
    if starting energy E is enough, then any larger energy is also enough.
    if E is not enough, then any smaller energy is also not enough.

Time Complexity:
    Sorting: O(n log n)
    Binary search simulation: O(n log S)
    where S is the search range for initial energy.

Space Complexity:
    O(n) for the sorted task list.
"""
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        def canFinish(allTask, energy):
            for actual, minimum in allTask:
                if energy >= minimum:
                    energy -= actual
                else:
                    return False
            return True
        # n logn
        sortedTask = []
        l = r = 0
        for i in range(len(tasks)):
            actual, minimum = tasks[i]
            r += minimum
            sortedTask.append((minimum-actual, i))
        
        sortedTask = sorted(sortedTask, reverse = True)
        for i in range(len(sortedTask)):
            d, idx = sortedTask[i]
            sortedTask[i] = tasks[idx]
     
        # Binary Search on res
        while l < r:
            mid = (l + r) // 2
            if canFinish(sortedTask, mid):
                r = mid
            else:
                l = mid + 1
        
        return r
    
                
