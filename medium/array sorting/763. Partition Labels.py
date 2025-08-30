    """
    LeetCode 763 — Partition Labels
    Interval-merge formulation (build [first,last] per character, then merge).

    Core idea
    ---------
    For each lowercase letter 'a'..'z', compute the earliest index it appears
    (first) and the latest index it appears (last). Each character therefore
    induces a closed interval [first, last] inside the string. Any valid
    partition must not split a character across parts, so the partition
    boundaries are exactly the boundaries after you merge all overlapping
    character intervals into disjoint blocks. The length of each merged block
    is one partition size.

    Steps
    -----
    1) Scan `s` left→right and fill an array of size 26 with [first,last]
       intervals for each character (None if the char never appears).
    2) Collect non-None intervals and sort them by start index.
    3) Merge intervals in order:
         - If the next interval starts before the current block ends, extend
           the block's end to the max end.
         - Otherwise, close the current block (append its length) and start a
           new block.
    4) Append the final block length.

    Why this works
    --------------
    A partition can end at position `i` only if *every* character that appears
    in the current segment finishes (its last occurrence ≤ i). Merging all
    character spans ensures each resulting block contains full occurrences of
    all characters it touches; thus no block needs to be extended by a later
    character occurrence.

    Complexity
    ----------
    - Time: O(n) to build intervals + O(Σ) to sort (Σ = 26 letters ⇒ constant),
            so overall O(n).
    - Space: O(Σ) extra (the 26-length array), i.e., O(1) auxiliary space.

    Notes
    -----
    - This implementation assumes `s` contains only lowercase English letters
      (per problem constraints), so a fixed-size 26 array is used.
    - The overlap check here treats touching intervals as separate blocks.
      With character-induced intervals, exact endpoint equality between
      *distinct* characters cannot occur at the same index, so this condition
      is sufficient and yields the canonical partitions.
    """

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        intervalsMap = [None] * 26
        
        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            if not intervalsMap[idx]:
                intervalsMap[idx] = [i,i]
            else:
                intervalsMap[idx][1] = i
        intervals = sorted(x for x in intervalsMap if x is not None)
        
        
        res = []
        merge = [intervals[0]]
        for interval in intervals[1:]:
            if merge[-1][1] > interval[0]:
                merge[-1][1] = max(merge[-1][1], interval[1])
            else:
                res.append(merge[-1][1] - merge[-1][0] + 1)
                merge.append(interval)
        res.append(merge[-1][1] - merge[-1][0] + 1)
        return res
        
