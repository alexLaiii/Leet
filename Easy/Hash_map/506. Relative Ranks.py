"""
Approach:
- Since all scores are unique, first build a mapping from each score to
  its original index.
- Sort the scores in descending order so the highest score appears first.
- Traverse the sorted scores while assigning ranks:
    * Rank 1 -> "Gold Medal"
    * Rank 2 -> "Silver Medal"
    * Rank 3 -> "Bronze Medal"
    * Remaining ranks -> rank number as a string
- Use the score-to-index mapping to place each assigned rank back into
  its original position in the result array.

Time Complexity:
- O(n log n)
  - O(n) to build the score-to-index map.
  - O(n log n) to sort the scores.
  - O(n) to assign the ranks.

Space Complexity:
- O(n)
  - O(n) for the score-to-index map.
  - O(n) for the output array.
"""
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # val:idx map
        valToidx = defaultdict(int)
        for i in range(len(score)):
            valToidx[score[i]] = i
        
        score.sort(reverse = True)
        placement = {
            1 : "Gold Medal",
            2 : "Silver Medal",
            3 : "Bronze Medal"
        }
        res = [None] * len(score)
        rank = 1
        for s in score:
            idx = valToidx[s]
            if rank in placement:
                res[idx] = placement[rank]
            else:
                res[idx] = str(rank)
            rank += 1
        return res
