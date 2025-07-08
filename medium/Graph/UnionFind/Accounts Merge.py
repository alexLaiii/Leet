"""
LeetCode 721: Accounts Merge

Union-Find problem with hashmap-based parents and ranks.

Idea:
The main idea is to connect all the emails that belong to the same person, so we can traverse the connected components (groups) later 
to gather all emails for that person.

We group the emails using Union-Find (Disjoint Set Union), treating each email as a node. The goal is to identify which group 
each email belongs to — since each group corresponds to a unique person, we don’t need names in the DSU structure itself.

After building the DSU structure, we iterate through the accounts again to attach names and format the final result.

Implementation:

1. Initialize DSU structures:
   - `parents`: {email -> representative} — maps each email to its parent (or itself initially).
   - `ranks`: {email -> list of emails in group} — maps each representative to the list of emails in its group.

   Since email is a string, we use dictionaries instead of arrays.

   During initialization, each email is:
   - its own parent
   - in its own group (i.e., ranks[email].append(email)

2. Def `find(email)`:
   - Standard path-compressed find.
   - If the email's parent is not itself, recursively find and compress the path.

3. Def `union(e1, e2)`:
   - Find their parents.
   - If their parents are the same, they already in the same group, return.
   - Otherwise, merge the smaller group into the larger one using rank lists:
     - `ranks[p1] += ranks[p2]` and update `parents[p2] = p1` if p1 is larger
     - else do the opposite

4. Union all emails in each account:
   - For each account, connect all its emails with the first one using `union`.

5. Build the final result:
   - Iterate through `accounts` again.
   - For each account, use any email (e.g., `accounts[i][1]`) to find the representative.
   - If that representative is not already processed (tracked via `visited` set):
     - Append `[name] + sorted(ranks[representative])` to the result.

Important Notes:
- Some names may appear multiple times in `accounts`, but if the emails are in the same group, we only include them once.
- The `visited` set prevents processing duplicate groups. Only the representative needs to be tracked.
- This approach avoids building a full graph and makes use of optimized DSU logic.

Time Complexity:
- Union-Find operations with path compression: O(α(N)) per operation
- Total: O(N log N)
  - N = total number of emails

Space Complexity:
- O(N)
  - For `parents`, `ranks`, and `visited`

This approach is both intuitive and efficient for merging accounts using shared emails.
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {}
        ranks = defaultdict(list)

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email not in parents:
                    parents[email] = email
                    ranks[email].append(email)

        def find(email):
            if parents[email] != email:
                parents[email] = find(parents[email])
            return parents[email]
        def union(e1,e2):
            p1, p2 = find(e1), find(e2)
            if p1 == p2:
                return
            if len(ranks[p1]) >= len(ranks[p2]):
                ranks[p1] += ranks[p2]
                parents[p2] = p1
            else:
                ranks[p2] += ranks[p1]
                parents[p1] = p2
            
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                    union(accounts[i][1], accounts[i][j])

        res = []
        visited = set()
        for i in range(len(accounts)):
            representative = find(accounts[i][1])
            if representative in visited:
                continue
            person = [accounts[i][0]]
            emails = []
            visited.add(representative)
            person += sorted(ranks[representative])
            res.append(person)
            
        return res
