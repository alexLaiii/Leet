"""
We can use a max-heap (priority queue) to solve this problem.

The idea:
- Store each (frequency, element) pair in a max-heap.
- Since the heap is sorted by frequency, the most frequent elements will be at the top.
- By popping the heap k times, we retrieve the top k frequent elements.

Implementation Steps:
1. Create a hashmap to count the frequency of each number in nums.
2. Push each (frequency, number) pair into a max-heap.
   - Since Python's heapq is a min-heap by default, we store negative frequency to simulate a max-heap.
3. Pop the heap k times and collect the elements.
4. Return the list of top k elements.

Time Complexity:
- Frequency count: O(n)                    ← one pass through nums
- Heap push for m elements: O(m log m)     ← m = number of unique elements
- Pop k elements from heap: O(k log m)
→ Total: O(n + m log m), and since m ≤ n, this simplifies to **O(n log n)** in the worst case

Space Complexity:
- Hashmap: O(m)
- Heap: O(m)
- Result list: O(k)
→ Total: **O(n)** in the worst case
"""

from heapq import heappop, heappush    

    # Solution must be better than O(nlogn), so sorting is not consider
    #default is min heap, thats why I struggle.
    hash_table, res = {}, []
    for i in range(len(nums)):
        hash_table[nums[i]] = 1 + hash_table.get(nums[i], 0)
    h = []
    for key in hash_table:
        heappush(h, (-hash_table[key], key))
    for i in range(k):
        value = heappop(h)
        res.append(value[1])
    return res
