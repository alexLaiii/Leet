"""
Counts the total waviness of all numbers in the inclusive range [num1, num2].

A digit contributes one point of waviness if it is a middle digit and forms
either a peak or a valley compared with its immediate left and right digits.
Numbers with fewer than three digits cannot contain a wavy digit.

The solution checks each number directly, making it suitable for the smaller
constraints of Range I.
"""

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for n in range(num1, num2 + 1):
            num = str(n)
            N = len(num)
            if N < 3:
                continue
            for j in range(1, N - 1):
                if num[j - 1] > num[j] and num[j + 1] > num[j]:
                    waviness += 1
                elif num[j - 1] < num[j] and num[j + 1] < num[j]:
                    waviness += 1
        
        return waviness
            
