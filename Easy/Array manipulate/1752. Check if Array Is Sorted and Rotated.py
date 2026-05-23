class Solution:
    def check(self, nums: List[int]) -> bool:
        decreased = 0
        last_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                decreased += 1
            if (decreased == 1 and nums[i] > last_min) or decreased >= 2:
                return False
        return True
            
                
            
        
