"""Sorts arr1 so elements appear in the relative order defined by arr2.

Elements of arr1 that also appear in arr2 are ordered according to
their position in arr2 (with duplicates preserved by count).
Elements of arr1 that do not appear in arr2 are appended at the end
in ascending sorted order.

Approach:
    1. Build a set of arr2 for O(1) membership checks.
    2. Walk arr1 once, tallying counts of each value that is present
       in arr2 (via a hash map) and collecting the rest into
       `left_over`.
    3. Walk arr2 in order, emitting each value `count` times using
       the tallied counts.
    4. Sort `left_over` and append it to the result.

Args:
    arr1: The array to be sorted. May contain duplicates.
    arr2: An array of distinct integers defining the desired
        relative order for any values shared with arr1.

Returns:
    A list containing all elements of arr1, with the shared elements
    ordered per arr2 followed by the remaining elements in ascending
    order.

Time Complexity:
    O(n + m + k log k), where n = len(arr1), m = len(arr2), and
    k = len(left_over) <= n. Building the set and count map is
    O(n + m); emitting the ordered elements is O(n) total across
    all counts; sorting the leftovers is O(k log k). Worst case
    (arr2 empty) reduces to O(n log n).

Space Complexity:
    O(n), for hash_arr2, hash_arr1_count, left_over, and the
    result list.
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_arr2 = set(arr2)
        hash_arr1_count = defaultdict(int)
        left_over = []
        for n in arr1:
            if n in hash_arr2:
                hash_arr1_count[n] += 1
            else:
                left_over.append(n)

        res = []
        for n in arr2:
            for _ in range(hash_arr1_count[n]):
                res.append(n)
        
        return res + sorted(left_over)
