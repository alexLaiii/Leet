"""
Convert each date to its day number within the year.
The overlap starts at the later arrival and ends at the earlier departure.
Return the inclusive overlap length, or 0 if they do not overlap.

Time: O(1). Space: O(1).
"""
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        cum_date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, len(cum_date)):
            cum_date[i] +=  cum_date[i - 1]
        
        arriveAlice, leaveAlice = cum_date[int(arriveAlice[:2]) - 1] + int(arriveAlice[3:]), cum_date[int(leaveAlice[:2]) - 1] + int(leaveAlice[3:])
        arriveBob, leaveBob = cum_date[int(arriveBob[:2]) - 1] + int(arriveBob[3:]), cum_date[int(leaveBob[:2]) - 1] + int(leaveBob[3:])

        return max(min(leaveAlice, leaveBob) - max(arriveAlice, arriveBob) + 1, 0)
        
