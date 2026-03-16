"""
Beginner level hash table problem
"""
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        typeSeen = set()
        canEat = len(candyType) // 2
        eat = 0
        for c in candyType:
            if c in typeSeen:
                continue
            if eat == canEat:
                break
            typeSeen.add(c)
            eat += 1
        return eat

        
