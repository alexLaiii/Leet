"""
Union Find problem with hashmap for parents and ranks.
Idea:
The main idea is to connect all the emails that belongs to the same person, so when we retreive all the email for that person, we can "traversal" the related graph
to get all the emails.

We group the emails belongs to the same person using Union Find, since we only need to know the email belongs to which group,as the entire group belongs to a single person.
Therefore,we treat each email as a node, and the parents and ranks are storing the email nodes, names is not needed here.

After the entire DSU is built correctly, we go through the accounts List again to match the Names to the email, 
just pick one email from that person, and then find the reprsentated email for that person, and therefore, now we got all the emails from ranks.

Implementation:
First, we initialize the Disjoin set Union Data Structures.
  "parents = {}
   ranks = defaultdict(list)"
   Since our nodes is not an integer here, is a string, therefore we need to use a hashmap here as the index of a list cannot represent a string.
   The strucutre here is
   parents = {email : representative}
   ranks = {email : all the email in the same group}
   Therefore, we initialize:
   - All the email's parents are the email itself before any connection added.
   - All the email's group only contains itself before any union happened.
 We loop through the accounts to acheive above, the goal in the first loop is just get all the emails and initialize it, not connections made yet.

 Second, Implement the Union and find function
   "def find(email): "
   standard find function, instead of parents list, we are referring to an parent hash_map here, but the overall logic is the same.
     - If an email's parent is not itself, then find its parent, return its parent when found, alongside with path compression.
   "def union(e1,e2): "
   modified union function.
   The find part is the same, if both email has same parent, they are in the same group/connected already, no need to perform Union.
   The main difference here is:
   - Our ranks is not storing the number of elements in the Group
   - Instead it uses a list to store all the emails belongs to the same group
   - Therefore, when we decided which group is larger and smaller for merging, 
     - we retreive this information by getting the length of the list, so we know how many emails are in that group
   - Since we are merging two list, we can += operation in python to merge it, note that this is not just adding the count,
     in fact we are merging two list into one, now two list is merge into one list with one representative.

  After we construct all the connections/group all the emails accordingly, we are ready to produce the result.
  - We loop through the account again:
    " person = [accounts[i][0]] "
    - Get the names of each person, and get a sample email(any) for that person.
    " representative = find(accounts[i][1]) "
    - Use the find(email) function to get the representative email of that person, so now we have access to the group that contains all the emails for that person
    " person += sorted(ranks[representative]) "
    - By our structure, All the emails stored in ranks[representative] belongs to that person, so we add all of it to that person
      - Since this problem want a alphabetic sorted result, so we sort it.
    " res.append(person) "
    - append the current person to the result
  ## Important Notes ##
  - Some of the names might referred to the same person previously, that happens when their email belongs to the same group that appeared previously.
  - Therefore, we need a visited set to mark the Group as visited, so we know it is the same person.
  " visited.add(representative) "
  - Store the representative is sufficient to mark the group as visited because all the emails in group have the same representative.
    " if representative in visited:
        continue "
  - Whenever we encounter a representative again, it means we reach to a person that is done before, so we skip this person as it is finished already.

  Finally, return the result

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
