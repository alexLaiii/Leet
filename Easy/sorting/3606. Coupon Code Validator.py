  """
  Filter and sort coupon codes by business line.

  Rules implemented:
  - A coupon is valid only if:
    1) code[i] is non-empty
    2) every character in code[i] is alphanumeric (A-Z, a-z, 0-9) or underscore '_'
    3) isActive[i] is True
  - Valid active coupons are grouped by businessLine into four categories:
    "electronics", "grocery", "pharmacy", "restaurant"
  - Output order is fixed by business line:
    electronics -> grocery -> pharmacy -> restaurant
  - Within each business line, codes are sorted in lexicographic order.

  Approach:
  - Iterate once through all coupons, validate each code by scanning its characters.
  - If valid and active, append to the corresponding bucket.
  - Sort each bucket and concatenate in the required business-line order.

  Time Complexity:
  - O(L) for validating all characters across all codes (L = total characters),
    plus sorting cost O(n log n) across buckets in total.

  Space Complexity:
  - O(n) to store valid codes in buckets (excluding output list).
  """

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        a,b,c,d = [],[],[],[]
        
        for i in range(len(code)):
            if len(code[i]) == 0:
                continue
            codeF = False
            for j in range(len(code[i])):
                if not ((code[i][j] >= "a" and code[i][j] <= "z") or(code[i][j] >= "A" and code[i][j] <= "Z") or (code[i][j] >= "0" and code[i][j] <= "9")) and code[i][j] != "_":
                    codeF = True
                    break
            if codeF or not isActive[i]:
                continue
            if businessLine[i] == "electronics":
                a.append(code[i])
            elif businessLine[i] == "grocery":
                b.append(code[i])
            elif businessLine[i] == "pharmacy":
                c.append(code[i])
            elif businessLine[i] == "restaurant":
                d.append(code[i])
        
        a.sort()
        b.sort()
        c.sort()
        d.sort()
        
        return  a + b + c + d

            
        
