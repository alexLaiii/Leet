  """
  Compute the total number of laser beams in a security bank layout.
  An easy problem with straight forward approach.

  A beam exists only between two consecutive rows that both contain at least one device ('1'),
  and the number of beams between such rows equals (#devices in upper row) * (#devices in lower row).
  We scan rows top-to-bottom, keep the previous non-zero device count, and accumulate products.

  Time:  O(M * N) where M=len(bank), N=len(bank[0])
  Space: O(1)
  """

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        M, N = len(bank), len(bank[0])
        prev_device = 0
        total = 0
        for i in range(M):
            curr_device = 0
            for j in range(N):
                if bank[i][j] == "1":
                    curr_device += 1
            if curr_device > 0:
                total += prev_device * curr_device
                prev_device = curr_device
            
            
        return total    
                    
                
