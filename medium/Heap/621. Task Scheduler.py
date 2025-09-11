"""
LeetCode 621 — Task Scheduler (Greedy + Max-Heap, cycle of n+1)

Idea / Intuition
----------------
We want the shortest timeline to execute all tasks with a cooldown `n` between
two runs of the SAME task. The cooldown makes the *most frequent* letters the
bottleneck. If you don’t spread them out early, you’ll run out of “filler”
tasks later and be forced to idle. Therefore, in each step we should prefer the
tasks with the largest remaining counts.

Why pick the most frequent first?
---------------------------------
Greedy exchange argument: Suppose at some time you run a task with smaller
remaining count while a larger-count task is available. Swapping them (run the
larger-count one now) never hurts—if anything, it reduces the chance you’ll be
forced to insert idles later when the high-frequency task needs space. So an
optimal schedule exists that always chooses the largest remaining counts first.

Algorithm (heap-based simulation)
---------------------------------
1) Count frequencies. Push each positive count as a negative number into a
   min-heap (acts like a max-heap).
2) We simulate time in *cycles* of up to `n+1` slots. In one cycle:
   - Pop up to `n+1` DISTINCT tasks with highest remaining counts.
   - Run each once (decrement its count). Collect survivors in a `used` list.
   - Push survivors back into the heap after the cycle.
3) Time accounting:
   - If the heap is NOT empty after this cycle, add a full `(n+1)` to the
     timeline (we conceptually include idles to respect cooldowns).
   - If the heap IS empty, add only the number of jobs actually run (`ran`)
     to avoid trailing idle padding.
4) Repeat until the heap is empty.

Correctness sketch
------------------
• Cooldown safety: Within a cycle we run each task at most once. If work
  remains, we pad the cycle to full length `(n+1)`, guaranteeing any task run
  in this cycle cannot reappear earlier than `n` slots later.  
• Minimality: Always choosing the largest counts first keeps bottleneck tasks
  consistently placed early in each cycle, preventing the need for extra front
  idles in later cycles when smaller tasks run out.

Complexity
----------
Let `N = len(tasks)` and `K` be distinct task types (≤ 26 here).
• Time: Each task instance is popped/pushed O(1) times ⇒ O(N log K).
  With K ≤ 26, this is effectively O(N).
• Space: O(K) for the heap and frequency storage.

Edge cases
----------
• `n = 0` → answer is just `N`; the loop naturally counts one per step.
• Many distinct tasks (enough fillers) → often no idles; the “full cycle if
  heap nonempty, else ran” rule automatically avoids padding the tail.

Dry run (example)
-----------------
tasks = [A,A,A,B,B,B], n = 2
Cycle 1: pick A,B (and maybe C if present). Here we get A,B,_  → time += 3
Cycle 2: A,B,_  → time += 3
Cycle 3: A,B    → heap empty after cycle → time += ran (=2)
Total = 8, which matches the known optimal.

Alternative one-liner (math approach)
-------------------------------------
Let maxCount = maximum frequency of any task,
    countMax = number of tasks achieving maxCount.
Minimum time = max(N, (maxCount - 1) * (n + 1) + countMax)

This heap solution matches that bound and is easy to reason about in interviews.
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [[0, ""] for i in range(26)]
        for t in tasks:
            count[ord(t) - ord("A")][0] += 1
            count[ord(t) - ord("A")][1] = t
        
        maxHeap = []
        for nums, task in count:
            if nums > 0:
                heapq.heappush(maxHeap, [-nums, task])
        
        interval = 0
        
   
        while maxHeap:
            used = []
            ran = 0
      
            for i in range(n + 1):
                if not maxHeap:
                    break
                nums, task = heapq.heappop(maxHeap)
                nums += 1
                if nums != 0:
                    used.append([nums, task])
                ran += 1
                
            for num,task in used:
                if num != 0:
                    heapq.heappush(maxHeap, [num, task])
            
            interval += (n + 1) if maxHeap else ran

       
        return interval
