"""
*** This Problem is very similar to "875. Koko Eating Bananas", tackle that before trying this. ***

Hint: Perform Binary Search on the answer, where the answer must lie in range [1, sum(weights)]

Main idea:
    The answer is the minimal ship capacity C such that all packages can be sent
    in at most D days if loaded in order without reordering. This induces a
    monotone predicate over capacities:
        - If capacity C works (feasible in ≤ D days), then any C' > C also works.
        - If C fails, any C' < C also fails.
    Because feasibility is monotone in C, we can binary search C.

Why the greedy feasibility check works:
    Given a candidate capacity C, simulate day-by-day loading from left to right,
    always packing the next package if it fits; otherwise start a new day.
    Greedy is optimal here because:
        - Packages must remain in order, so delaying a package that fits provides
          no advantage—it only reduces remaining capacity for later items.
        - Starting a new day earlier never decreases the number of days used.
    Thus, the simple “take as much as possible each day” simulation uses the
    fewest days for that C, correctly deciding feasibility.

Bounds:
    Lower bound = max(weights)  (must fit the heaviest package).
    Upper bound = sum(weights)  (one-day shipment).

Complexity:
    Let n = len(weights). The feasibility check is O(n). Binary searching over
    capacities (range up to sum(weights)) costs O(log(sum(weights))). Total:
    O(n log sum(weights)) time and O(1) extra space.
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def takeAll(w, days):
            l = 0
            while days > 0:
                curr_w = w
                while l < len(weights) and curr_w >= weights[l]:
                    curr_w -= weights[l]
                    l += 1
                if l >= len(weights):
                    return True
                days -= 1
            return False
                
        l, r = 1, sum(weights)
        minWeight = float("inf")


        while l <= r:
            mid = (l + r) // 2
            if takeAll(mid, days):
                minWeight = mid
                r = mid - 1
            else:
                l = mid + 1
        return minWeight
            
        
