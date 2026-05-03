"""
Count how many numbers from 1 to n are valid after rotation.

A number is valid if:
1. Every digit can still form a digit after rotation.
   Valid mappings are:
   0->0, 1->1, 2->5, 5->2, 6->9, 8->8, 9->6
2. The rotated number is different from the original number.

For each number i:
- Extract each digit from right to left.
- If any digit is invalid, stop checking this number.
- Otherwise, rebuild the rotated number using the mapped digits.
- If the rebuilt number is not equal to i, then i is a "good" rotated number.

Time Complexity: O(n * d), where d is the number of digits in n.
Space Complexity: O(1), since the mapping table has constant size.
"""

class Solution:
    def rotatedDigits(self, n: int) -> int:
        hash_table = {
            0 : 0,
            1 : 1,
            2 : 5,
            5 : 2,
            6 : 9,
            8 : 8,
            9 : 6
        }
        res = 0
        for i in range(n, 0,-1):
            k = i
            val = 0
            j = 1
            flag = True
 
            while k > 0:
                d = k % 10
                if d not in hash_table:
                    flag = False
                    break
                val += hash_table[d] * j

                k = k // 10
                j = j * 10
            if val != i and flag:
                res += 1
     

     
        return res
            


        
