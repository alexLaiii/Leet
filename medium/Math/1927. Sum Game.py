"""
Alice wants the two halves' digit sums to end up unequal; Bob wants them equal.
Each still-unknown digit is filled by whichever player moves next, alternating turns.

Count '?' and known digit sums separately in each half (q1, sum1 / q2, sum2).

Case 1 - q1 + q2 is odd:
    Alice makes the last move, giving her one free move Bob can't answer.
    She can always use it to break equality, so Alice wins -> True.

Case 2 - q1 + q2 is even:
    Since the total is even, q1 and q2 must share the same parity, so
    (q2 - q1) is always even and (q2 - q1) // 2 is an exact integer.

    With optimal play (Bob mirrors each of Alice's moves with a digit that
    keeps things balanced), the final gap converges to:
        sum1 - sum2 == (q2 - q1) // 2 * 9
    Alice wins if she can prevent this, i.e. if the actual difference
    does NOT equal that forced value -> return sum1 - sum2 != (q2 - q1) // 2 * 9.

    (q1 == q2 is just the special case where this forced value is 0.)
"""

class Solution:
    def sumGame(self, num: str) -> bool:
        # Alice try to make unequal
        # Bobs try to make equal
        # If  q1 +  q2 is odd, Alice move last, some Alice can always mess up whatever Bob is doing since Alice get one free move

        q1 = q2 = 0
        sum1 = sum2 = 0
        cutoff = len(num) // 2
        for i in range(cutoff):
            if num[i] == "?":
                q1 += 1
            else:
                sum1 += int(num[i])
        for j in range(cutoff, len(num)):
            if num[j] == "?":
                q2 += 1
            else:
                sum2 += int(num[j])
        if (q1 + q2) % 2 != 0:
            return True
        if q1 == q2:
            return sum1 != sum2
        return sum1 - sum2 != ((q2-q1) // 2) * 9  

        # If sum2 has more "?"" -> k > 0
        # Assume sum1 < sum2 -> sum1 - sum2 < 0 (k is guranteen even because if q1 + q2 is even, then any split must have same parity, so their deduction must be even, and k = q2 - q1, and q1 and q2 has same parity)
        # sum1 - sum2 == (k // 2) * 9

        # sum2 has less ? -> k < 0
        # Assume sum1 < sum2 -> sum1 - sum2 < 0
        # sum1 - sum2 == (k // 2) * 9 = <0 == <0

  
        
