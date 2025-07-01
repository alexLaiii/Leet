class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(path, visited):
            if len(nums) == len(path):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i-1] and i - 1 not in visited:
                    continue
                path.append(nums[i])
                visited.add(i)
                backtrack(path, visited)
                path.pop()
                visited.remove(i)
        backtrack([], set())
        return res
                
