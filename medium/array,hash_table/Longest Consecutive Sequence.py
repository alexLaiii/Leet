"""

Intuition:
My first thought was to use Dynamic Programming, since it feels like each number's sequence length could depend on the previous one. For example, if 6 starts a sequence of length 4, then 5 should lead to a sequence of length 3.

However, this doesn’t work well in practice because we’d need to sort the array first, and sorting takes O(n log n) time. But the problem specifically asks for an O(n) time solution, so DP+sorting doesn't meet that requirement.

Optimal Solution
1. Turn the input array into a set(), becasue set does not have duplicate and most importantly, has a look up complexity of O(1)
2. Loop through the set, let n be the current number of the set, if n-1 does not appear in the set, then num can be consider as the first num of a sequence, 
  then use a while loop to keep checking whether num + 1 is in the set or not, keep counting how many number in a row, until num + 1 is no longer in the set
3. After the loop, max_count will be the count of the Longest Consecutive Sequence

Note that we only enter the while loop if num can be consider as the num of a sequence, 
that is if, all the nums contains all consequetive numbers, there will be only one element trigger the while loop,
more generlly, no matter what happen, the total iterations in all while loops will not run more than len(nums) times after the whole for loop
So this guarantee the Time Complexity is O(n + n + n), making set + looping set + total iterations in all while loops, which simplify to O(n)

Time Complexity: O(n)
Space Complexity: O(n) the set to store mostly len(nums) elements
"""



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            curr_n = n
            seq = 0
            while curr_n in nums_set:
                seq += 1
                curr_n += 1
            res = max(seq, res)
        return res
