class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def dfs(start, path, curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return
            elif curr_sum > target:
                return
            i = start
            while i < len(candidates):
                
                path.append(candidates[i])
                dfs(i + 1, path, curr_sum + candidates[i])
                path.pop()
                i += 1
                while i < len(candidates) and candidates[i] == candidates[i - 1]:
                    i += 1
                        
        dfs(0, [], 0)
        return res

        
        
