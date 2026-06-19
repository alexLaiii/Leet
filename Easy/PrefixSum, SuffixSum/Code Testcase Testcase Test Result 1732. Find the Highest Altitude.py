class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Track the running altitude starting from 0 and return the highest
        altitude reached after applying each gain value.
        """
        curr_altitude = 0
        res = 0

        for g in gain:
            curr_altitude += g
            res = max(res, curr_altitude)

        return res
