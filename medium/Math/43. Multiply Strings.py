"""
Idea:
Simulate elementary-school string multiplication manually without converting
the full numbers into integers.

Approach:
1. Reverse both strings so multiplication starts from the least significant digit.
2. For each digit in num2:
    - Multiply it against every digit in num1.
    - Maintain carry exactly like normal handwritten multiplication.
    - Store the partial product as a reversed string.
    - Prepend j zeros ("0" * j) to represent place shifting.
3. Store all partial products inside `vals`.
4. Add all partial products together digit-by-digit:
    - Since all strings are stored reversed, addition proceeds naturally
      from left to right.
    - Maintain carry during addition.
5. Reverse the final result before returning.

Key Insight:
Reversing the strings avoids complicated indexing from the back and allows
both multiplication and addition to proceed in natural left-to-right order.

Why the shifting works:
Because the strings are reversed, multiplying by powers of 10 is represented
by prepending zeros to the reversed partial product instead of appending them.

Complexity:
Let M = len(num1), N = len(num2)

Time:
- Partial product generation: O(M * N)
- Summation of partial products: O(M * N)
Overall: O(M * N)

Space:
- Stores all partial products.
Overall: O(M * N)
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        vals = []
        for j in range(len(num2)):
            s = "0" * j
            digit_2 = int(num2[j])
            carry = 0
            for i in range(len(num1)):
                digit_1 = int(num1[i])
                digit = (digit_1 * digit_2 + carry) % 10
                carry = (digit_1 * digit_2 + carry) // 10
                s += str(digit)
            if carry != 0:
                vals.append(s + str(carry))
            else:
                vals.append(s)
        res = ""
 
        for num in vals:
            ans = ""
            carry = 0
            for i in range(len(num)):
                if i >= len(res):
                    val = int(num[i]) + carry
                    digit = val % 10
                    carry = val // 10
                    ans += str(digit)
                    continue
                val = int(res[i]) + int(num[i]) + carry
                digit = val % 10
                carry = val // 10
                ans += str(digit)
            if carry != 0:
                res = ans + str(carry)
            else:
                res = ans
        return res[::-1]
