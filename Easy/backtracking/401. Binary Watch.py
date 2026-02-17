  """
  Generates all possible times on a binary watch with exactly `turnedOn` LEDs turned on.

  The binary watch consists of 10 LEDs:
  - The first 4 represent hours with values [8, 4, 2, 1]
  - The last 6 represent minutes with values [32, 16, 8, 4, 2, 1]

  A depth-first search (DFS) backtracking approach is used to explore all subsets of LEDs.
  At each step, the algorithm decides whether to turn on the current LED or skip it, while
  maintaining running totals for hours and minutes.

  Invalid states are pruned early if:
  - hours exceed 11
  - minutes exceed 59

  Once exactly `turnedOn` LEDs are selected, the current time is formatted and added
  to the result list (with minutes padded to two digits).

  Args:
      turnedOn (int): Number of LEDs that must be turned on.

  Returns:
      List[str]: All valid times in "H:MM" format that can be represented with `turnedOn` LEDs.

  Time Complexity:
      O(2^10) in the worst case, since each LED can be either selected or skipped.

  Space Complexity:
      O(10) for recursion depth, excluding the output list.
  """

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        res = []
        nums = [8,4,2,1,32,16,8,4,2,1]

        def dfs(i, turned, hours, mins):
            if hours > 11 or mins > 59:
                return
            if turned == turnedOn:
                time = f"{hours}:" + f"{mins:02d}"
                res.append(time)
                return
            if i >= len(nums):
                return

            if i < 4:
                hours += nums[i]
            else:
                mins += nums[i]
            dfs(i + 1, turned + 1, hours, mins)
            if i < 4:
                hours -= nums[i]
            else:
                mins -= nums[i]
            dfs(i + 1, turned, hours, mins)

        dfs(0, 0, 0, 0)
        return res
            
            
