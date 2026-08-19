"""
Count the max number of 4-seat families that fit, given reserved seats.

Each row has 3 possible 4-seat groups: left [2-5], middle [4-7],
right [6-9]. Left and right are disjoint (both can be used together);
middle overlaps both. A row can seat 2 families only if left and
right are both fully free, which is only possible for rows with
zero reservations. So any row that appears in reservedSeats yields
at most 1 family - 0 only if all three groups are blocked, else 1.
Untouched rows each contribute 2 families for free.

Time:  O(m), where m = len(reservedSeats)
       (only rows with reservations are processed)
Space: O(k), k = number of distinct rows with reservations, k <= m

:param n: total number of rows
:param reservedSeats: list of [row, seat] reservations
:return: max number of 4-person families that can be seated
"""

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        not_avaialble_group = defaultdict(set)
        
        for row, seat in reservedSeats:
            if seat in [2,3,4,5]:
                not_avaialble_group[row].add(1)
            if seat in [4,5,6,7]:
                not_avaialble_group[row].add(2)
            if seat in [6,7,8,9]:
                not_avaialble_group[row].add(3)
        res = 0
        for row, group in not_avaialble_group.items():
            if 1 in group and 2 in group and 3 in group:
                continue
            res += 1

        return (n - len(not_avaialble_group)) * 2 + res
            
        
        
