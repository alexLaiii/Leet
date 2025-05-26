"""
Idea: 
maintain a visited map to store the visited number of each recursive level, travel through all the possible numbers at each stage and add the number that is not visited,

e.g ->
[1,2,3]
so at first level
loop through [1,2,3]
n = 1
permuate = [1]
visited = [1]
recursive call ([1],[1])
loop through [1,2,3]
1 in visited -> continue
2 not in visited -> append
permuate = [1,2]
visited = [1,2]
recursive call ([1,2],[1,2])
loop through [1,2,3]
1 in visited -> continue
2 in visited -> continue 
3 not in visited -> append
permuate = [1,2,3]
visited = [1,2,3]
recursive call ([1,2,3],[1,2,3])
len(permute) == len(nums) -> append to result
return
back ([1,2,3],[1,2,3])
pop last element
permute, visited = [1,2],[1,2]
for loop reach the end
back ([1,2],[1,2])
pop last element
permute, visited = [1],[1]
for loop not reach the end n = 3
3 not in visited -> append
permute, visited = [1,3],[1,3]
recursive call ([1,3],[1,3])
loop through [1,2,3]
1 in visited -> continue
2 not in visited -> append
permute, visited = [1,3,2],[1,3,2]
recursive call ([1,3,2],[1,3,2])
len(permute) == len(nums) -> append to result
return
back ([1,3,2],[1,3,2])
pop last element 
permute, visited = [1,3],[1,3]
continue for loop, n = 3
3 in visited -> continue
for loop ends
back ([1,3],[1,3])
pop last element
permute, visited = [1],[1]
continue loop 
loop reach the end
back ([1],[1])
pop the last element
permute, visited = [],[]
coninute for loop -> n = 2
***
same logic until the for loop of first level ends
***
"""



class Solution(object):
    def permute(self, nums):
        res = []

        def backtrack(permute, visited):
            if len(permute) == len(nums):
                res.append(permute[:])
                return
            for n in nums:
                if n not in visited:
                    permute.append(n)
                    visited.add(n)
                    backtrack(permute, visited)
                    permute.pop()
                    visited.remove(n)
        backtrack([], set())
        return res


        # res = []
        # def backtrack(permute):
        #     if len(permute) == len(nums):
        #         res.append(permute[:])
        #         return
        #     for n in nums: 
        #         if n not in permute:
        #             permute.append(n)
        #             backtrack(permute)
        #             permute.pop()
        # backtrack([])
        # return res

