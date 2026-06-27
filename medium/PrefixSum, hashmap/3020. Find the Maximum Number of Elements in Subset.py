from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        A valid subset has the form:

            x, x^2, x^4, ..., middle, ..., x^4, x^2, x

        So every value before the middle needs 2 copies,
        while the middle value only needs 1 copy.

        Special case:
        If x == 1, then 1^2 is still 1, so the best subset made of only 1s
        must have odd length. Therefore, we use the largest odd count of 1s.

        For every possible starting number x > 1:
        - keep squaring while we have at least 2 copies
        - if the next squared value exists, it can be the middle
        - otherwise, the previous paired value becomes the middle
        """
        count = Counter(nums)

        ones = count[1]
        res = ones if ones % 2 == 1 else ones - 1
        res = max(res, 1)

        for x in count:
            if x == 1:
                continue

            curr = x
            pairs = 0

            while curr in count and count[curr] >= 2:
                pairs += 1
                curr = curr * curr

            if curr in count:
                # We found a middle value.
                length = pairs * 2 + 1
            else:
                # No middle after the last pair, so the last pair level
                # becomes the middle instead.
                length = pairs * 2 - 1

            res = max(res, length)

        return res
