"""
Idea: 
First, each candidates in this problem are only allow to use once, so if you choose the first i candidates, then the only candidates you can choose for next is i + 1
Therefore, in the recursive call, we pass i+1 as the start for next path
Second, which is the hardest part in this problem, is removing the duplicate path, since the array can contain duplicate candidates, we cannot simplfy use the strategy for combination sum 1
Core idea: 
The first occurrence of a number already explores all valid paths using that value, so we can skip all the future duplicates.
And thats why we need to sort the array first, so we can guranteen all the duplicates are stick together:
Example [1,1,2,3]
since 1 is sticked together, after checking all the path for the first 1, then the second 1 will be skipped
Counter Example [1,3,1,2]
after checking all the path for the first 1, the next value is 3, which is not a duplicate to 1, so it will run correctly, 
but the problem kicks in after checking all the path for 3, we encounter 1 again, but the previous is 3, which is not same as 1, so we would check it again,causing duplicates

Fix 1: Sort the array first to make sure all the duplicate are neigbours, so you can skip it correctly
Fix 2: Use a hash set to store all the checked values, skip it if its in set, (ahh still need sorted)
Fix 3: loop all the previous element to check if it is seen already, trade off: worst time complexity

"""

# Solution 1
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
            for i in range(start, len(candidates)):
                if i  > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, path, curr_sum + candidates[i])
                path.pop()
        dfs(0, [], 0)
        return res


Solution 2
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



                
     
                


        
        

        
        
