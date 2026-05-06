"""
Idea:
Break the number into digit-place values (ones, tens, hundreds, thousands),
then directly map each value to its Roman numeral representation using a
precomputed dictionary.

Key Observation:
Roman numerals are constructed independently for each digit position.

Example:
1994
= 1000 + 900 + 90 + 4
= "M" + "CM" + "XC" + "IV"

Approach:
1. Build a dictionary containing all possible Roman numeral values:
   - Ones: 1..9
   - Tens: 10..90
   - Hundreds: 100..900
   - Thousands: 1000..3000

2. Extract digits from right to left using modulo/division.
   Multiply each digit by its place value:
       4   -> 4
       9   -> 90
       9   -> 900
       1   -> 1000

3. Push each computed value into a stack.

4. Pop from the stack to process values from largest place value
   to smallest place value, appending the mapped Roman numeral.

Why Stack Works:
Digits are extracted from least significant to most significant,
but Roman numerals must be constructed from highest place value first.
The stack reverses the order naturally.

Time Complexity:
O(d), where d is the number of digits.
(Effectively O(1) since num <= 3999)

Space Complexity:
O(d) for the stack.
(Effectively O(1))
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        digits = {
            0 : "",
            1 : 'I',
            2 : 'II',
            3 : 'III',
            4 : 'IV',
            5 : 'V',
            6 : 'VI',
            7 : 'VII',
            8 : 'VIII', 
            9 : 'IX',
            10 : 'X',
            20 : 'XX',
            30 : 'XXX',
            40 : 'XL',
            50 : 'L',
            60 : 'LX', 
            70 : 'LXX', 
            80 : 'LXXX', 
            90 : 'XC',
            100 : 'C',
            200 : 'CC',
            300 : 'CCC',
            400 : 'CD',
            500 : 'D', 
            600 : 'DC',
            700 : 'DCC',
            800 : 'DCCC',
            900 : 'CM',
            1000 : 'M',
            2000 : 'MM', 
            3000 : 'MMM'
        }
        
        j = 1
        val_stack = []
        while num > 0:
            d = num % 10
            num = num // 10
            val_stack.append(d * j)
            j = j * 10
        res = ""
        while val_stack:
            res += digits[val_stack.pop()]

        return res
        
            
            
        
