  """
  Add two binary strings by converting them to a decimal integer sum, then converting
  that sum back into a binary string.

  Approach
  --------
  1) Convert `a` from binary -> decimal:
     - Iterate bits from least-significant to most-significant (a[::-1]).
     - Maintain `decimal` as the current power of 2 (1, 2, 4, ...).
     - If the bit is '1', add `decimal` into `decia`.

  2) Convert `b` from binary -> decimal similarly into `decib`.

  3) Add the decimals: `sums = decia + decib`.

  4) Convert `sums` from decimal -> binary:
     - Special-case `sums == 0` -> "0".
     - Find the highest power of 2 <= `sums` by doubling `decimal` until it exceeds
       `sums`, then stepping back once.
     - Greedily build the result from most-significant bit to least-significant:
       if current `decimal` fits in `sums`, append '1' and subtract it; else append '0'.
       Then halve `decimal` each step.

  Correctness intuition
  ---------------------
  The first two loops compute the exact integer values represented by `a` and `b`
  (standard base-2 expansion). The final greedy conversion works because every
  nonnegative integer has a unique binary representation; at each step we decide
  whether the current highest power of two is present in the sum.

  Complexity
  ----------
  Let n = len(a), m = len(b), and k = number of bits in (value(a) + value(b)).
  Time:  O(n + m + k)
  Space: O(1) extra auxiliary space (output string excluded).

  Notes
  -----
  This works well in Python because integers have arbitrary precision. In languages
  with fixed-width integers, direct binary addition with carry is safer.
  """

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decia = 0
        decib = 0
        decimal = 1
        for n in a[::-1]:
            if n == "1":
                decia += decimal
            decimal *= 2
        decimal = 1
        for n in b[::-1]:
            if n == "1":
                decib += decimal
            decimal *= 2

        sums = decia + decib
        if sums == 0:
            return "0"
        length = 0
        decimal = 1
        res = ""
        while decimal <= sums:
            decimal *= 2
            length += 1
        decimal //= 2
   
        for i in range(length):
            if decimal <= sums:
                sums -= decimal
                res += "1"
            else:
                res += "0"
            decimal //= 2

        return res
            
        
        
