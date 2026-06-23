class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Find the extra character in t by comparing the sum of character codes.

        Since t contains every character from s plus one additional character,
        subtracting the total ASCII/Unicode values of s from t leaves the code
        of the added character.
        """
        sum_s = sum_t = 0

        for c in s:
            sum_s += ord(c)

        for c in t:
            sum_t += ord(c)

        return chr(sum_t - sum_s)
