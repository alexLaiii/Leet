class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs_count = left_count = 0
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        for key in count:
            
            pairs_count += count[key] // 2
            if count[key] % 2 != 0:
                left_count += 1
        
        return [pairs_count, left_count]
            
