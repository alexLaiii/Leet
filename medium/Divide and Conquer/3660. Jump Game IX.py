
"""
Correct Solution:
Idea:
Treat the problem as connected components formed by inversions.

Two indices are connected if there exists an inversion:
    i < j and nums[i] > nums[j]

Instead of explicitly building the graph (which is O(n²)),
this solution recursively partitions the array using prefix maximums.

Key Observation:
If the maximum value in a left region is greater than some value
in the right region, then an inversion exists across the boundary,
meaning both regions belong to the same connected component.

Preprocessing:
prefix_max[i] stores:
    (maximum value in nums[0:i+1], index of that maximum)

Recursive Strategy:
divide_and_conquer(r, r_min, r_max)

Parameters:
    r       -> current right boundary of the unresolved region
    r_min   -> minimum value seen in the component to the right
    r_max   -> maximum value assigned to the component to the right

At each step:
1. Find the prefix maximum and its pivot position inside [0..r].
2. The segment [pivot..r] belongs to the same component because
   every value after the pivot can connect through the prefix maximum.
3. If the current maximum is greater than r_min, then an inversion
   exists between the current segment and the right segment, so both
   components merge and inherit the larger component maximum (r_max).
4. Assign the component maximum to all indices in [pivot..r].
5. Recurse on the remaining left portion [0..pivot-1].

Why this works:
The recursion progressively groups contiguous regions that are connected
through inversion relationships without explicitly constructing graph edges.

Complexity:
Preprocessing prefix maximums:
    O(n)

Recursive assignments:
    O(n)

Overall:
    Time  -> O(n)
    Space -> O(n) excluding recursion stack
"""
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_max = [0] * N
        prefix_max[0] = (nums[0], 0)
        for i in range(1, N):
            if nums[i] > prefix_max[i-1][0]:
                prefix_max[i] = (nums[i], i)
            else:
                prefix_max[i] = prefix_max[i-1]
   
        res = [0] * N
        # r = pivot - 1
        def divide_and_conquer(r, r_min, r_max):
            
            curr_max, pivot = prefix_max[r]
            next_min = r_min
            if curr_max > r_min:
                curr_max = r_max

            for i in range(pivot, r + 1):
                res[i] = curr_max
                next_min = min(nums[i], next_min)
            if pivot == 0:
                return
            divide_and_conquer(pivot - 1, next_min, curr_max)

            
        divide_and_conquer(N - 1, float("inf"), 0)
        return res 
        
        


# TLE solution
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        adj_list = defaultdict(list)
        for i in range(len(nums)):
            adj_list[i] = []
            for j in range(len(nums)):
                if i != j:
                    if j > i and nums[j] < nums[i]:
                        adj_list[i].append(j)
                    elif j < i and nums[j] > nums[i]:
                        adj_list[i].append(j)
        
        def find_max(node, curr_max, visited):
            if node in visited:
                return curr_max
            visited.add(node)
            if nums[node] > curr_max:
                curr_max = nums[node]
            for neighbour in adj_list[node]:
                curr_max = find_max(neighbour, curr_max, visited)
            return curr_max


        res = []
        for i in range(len(nums)):
            res.append(find_max(i, nums[i], set()))
            

        return res

        
