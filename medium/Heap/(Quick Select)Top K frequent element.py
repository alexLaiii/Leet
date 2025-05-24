"""
Quickselect approach for LeetCode 347: Top K Frequent Elements
This approach is conceptually similar to LeetCode 215: Kth Largest Element in an Array. Revisit that if the quickselect logic is unclear.

Overview:
Use quickselect to partition the [element, frequency] pairs and retrieve the top K frequent elements.

Implementation:
1. Count the frequency of each number in `nums` using a hashmap.
   - Time: O(n)
   - Space: O(m), where m = number of unique elements

2. Convert the hashmap into an array of [element, frequency] pairs.
   - Time: O(m)
   - Space: O(m)

3. Define a quickselect function:
   - Randomly choose a pivot from the array.
   - Partition the array into three parts:
     - `left`: elements with frequency > pivot
     - `mid`: elements with frequency == pivot
     - `right`: elements with frequency < pivot
   - Recursively determine where the top K frequent elements lie:
     - If K falls entirely in `left`, recurse on `left`.
     - If K overlaps `left` and `mid`, return `left` and as many from `mid` as needed.
     - If K goes beyond `left + mid`, return all from `left` and `mid`, then recurse on `right`.

   - Time (average): O(m), due to geometric series behavior like n + n/2 + n/4 + ... = O(n)
   - Time (worst): O(m²), if pivot choices are consistently bad
   - Space: O(m), due to recursive partitioning and storage

4. After quickselect returns the top K [element, frequency] pairs, extract only the elements.
   - Time: O(k)
   - Space: O(k)

  Time Complexity Breakdown (average case):
- Frequency count: O(n)                  ← n = number of total elements in nums
- Build [element, frequency] pairs: O(m) ← m = number of unique elements
- Quickselect partitioning: O(m)         ← behaves like geometric series: m + m/2 + m/4 + ... = 2m = O(m)
- Extract result: O(k)                   ← extract top K elements
→ Total: O(n + m + m + k) = O(n) (since m ≤ n, and k ≤ m)

Worst-case Time: O(n²), if pivot choices are always poor.

Space Complexity:
- Hashmap (frequency count): O(m)
- Array of pairs: O(m)
- Partition arrays (left, mid, right): O(m)
- Final result array: O(k)
→ Total: O(n) in the worst case where all elements are unique

Note:
- The problem allows any valid K elements with the highest frequencies.
- Ties in frequency are acceptable and handled via slicing the mid group.
"""

import random
class Solution(object):
    def topKFrequent(self, nums, k):
        freq_count, arr, res= {}, [], []
        for i in range(len(nums)):
            freq_count[nums[i]] = 1 + freq_count.get(nums[i], 0)
        for key in freq_count:
            arr.append([key, freq_count[key]]) # [number:frequent] pair

        def qs(arr, k):
            p = random.choice(arr)
            l,m,r = [], [], []
            # quicksort it in decending order
            for i in range(len(arr)):
                if arr[i][1] > p[1]:
                    l.append(arr[i])
                elif arr[i][1] < p[1]:
                    r.append(arr[i])
                else:
                    m.append(arr[i])
            L,M,R = len(l), len(m), len(r)
            # left contains all the valid nums now
            if k == L:
                return l
            # left has some valid nums, but not all are valid
            elif k < L:
                return qs(l, k)
            # That means k is from L to M, and k is lie in m
            elif L +  M >= k:
                # Since all the element in middle are the same, no sorting needed, we slice the result, take what we needed
                return l + m[:k - L]
            # else: implicitly state that L + M < k, means k lied in the right array
            else:
                return l + m + qs(r, k - M -L)
            
        res = qs(arr, k)
        # since the result is structure like [[1,3],[2,2]] where the res[i][0] is the number and res[i][1] is the frequency, we need to extract the number to the result
        res = [x[0] for x in res]
        return res
