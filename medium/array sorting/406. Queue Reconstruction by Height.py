"""
Standard simple appraoch:
     
  Greedy:
  1) Sort by height descending; for equal height, sort by k ascending.
  2) Insert each person at index k.

  Why it works:
  
  - When we place a taller person first, everyone already in the list is
    >= this person's height, so inserting at index k guarantees exactly k
    taller-or-equal people end up before them.
  - For equal heights, smaller k must come earlier; inserting in that order
    preserves each person's required k.

    
  Complexity: O(n^2) due to list.insert; n ≤ 2000 is fine.
      
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0], x[1]))
        
        res = []
        for person in people:
            res.insert(person[1], person)
       
        return res



"""
My initial solution: Filling out the empty slot, more complicated, but works.


Fill empty slots from shortest → tallest.

Steps
1) Sort by (height) ascendingly
2) For each (h, k), scan left→right with a counter `need = k`.
   - If `need <= 0` and the current slot is empty → place (h, k) here.
   - Otherwise, if the slot is empty (future ≥ h) OR holds height == h,
     decrement `need` (because that position counts toward the ≥ h before us).

Invariant
- After sorting, anyone not yet placed is height ≥ h, so every empty slot
  represents a future ≥ h person. Already-placed equals also count toward ≥ h.
  Placing at the first empty slot after seeing k such positions satisfies k.

Time: O(n^2); Space: O(n).
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        queue = [[]] * len(people)
        queue[people[0][1]] = [people[0][0], people[0][1]]
        


        for i in range(1, len(people)):
            height, tallerFront = people[i]         
            for j in range(len(queue)):
                if tallerFront <= 0 and not queue[j]:
                    queue[j] = people[i]
                    break
                if not queue[j] or queue[j][0] == height:
                    tallerFront -= 1
                
        return queue
