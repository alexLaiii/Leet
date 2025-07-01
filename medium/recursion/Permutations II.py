

# Count base approach
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hash_nums = {}
        for n in nums:
            hash_nums[n] = 1 + hash_nums.get(n, 0)
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in hash_nums:
                if hash_nums[num] == 0:
                    continue
                path.append(num)
                hash_nums[num] -= 1
                backtrack(path)
                path.pop()
                hash_nums[num] += 1
        backtrack([])
        return res

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
                
