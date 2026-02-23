"""
Too easy, don't bother explain
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        arr = [int(d) for d in str(num)]
        nums = 0
        changed = False
        for i in range(len(arr)):
            if arr[i] == 6 and not changed:
                arr[i] = 9
                changed = True
            nums = nums * 10 + arr[i]                
        
        return nums
                

        
