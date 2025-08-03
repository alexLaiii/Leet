    """
    Solves the Word Ladder problem by finding the shortest transformation sequence
    from beginWord to endWord such that:
    - Only one letter can be changed at a time.
    - Every intermediate word must exist in the given wordList.
    
    The function returns the number of steps in the shortest valid transformation sequence,
    including both the beginWord and the endWord. If no such sequence exists, it returns 0.

    ---------------------
    Algorithmic Approach:
    ---------------------

    This solution uses Breadth-First Search (BFS) combined with a preprocessed
    adjacency lookup via wildcard pattern matching.

    1. Wildcard Pattern Graph Construction:
       For every word in wordList, generate all possible wildcard patterns by replacing
       one character at a time with '*'. For example, the word "dog" generates:
           "*og", "d*g", "do*"
       This pattern-based mapping allows quick lookup of all possible one-letter
       neighbors of any given word in O(L) time, where L is word length.

    2. BFS Traversal:
       Starting from the beginWord, perform a BFS where each level of traversal
       represents one transformation step.
       - For the current word, generate all wildcard patterns.
       - For each pattern, get all possible next words from the pattern-to-word map.
       - If a next word equals the endWord, return the current distance + 1.
       - Otherwise, enqueue it if it hasn’t been visited yet.
       
    3. Visited Set:
       Ensures that each word is only visited once to prevent cycles and redundant work.

    ---------------
    Key Design Notes:
    ---------------
    - The beginWord does not need to be in wordList.
    - The graph is implicit: we're not building actual edges between words,
      but instead grouping them by transformation patterns.
    - This avoids the naive O(N^2) pairwise comparison and instead processes
      everything in linear time with respect to total characters.

    -------------------
    Time Complexity:
    -------------------
    - Preprocessing: O(N × L), where N is the number of words and L is word length
    - BFS Traversal: O(N × L), as each word generates up to L patterns, each looked up once
    - Total: O(N × L)

    -------------------
    Space Complexity:
    -------------------
    - O(N × L) for the pattern graph
    - O(N) for the visited set and queue

    -------------------
    Example:
    -------------------
    Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    Output:
        5

    Explanation:
        One shortest transformation path is:
        "hit" → "hot" → "dot" → "dog" → "cog"
    """


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1:]
                graph[pattern].append(w)
        

    
        dq = deque([beginWord])
        visited = set([beginWord])
        distance = 0
        while dq:
            for k in range(len(dq)):
                word = dq.popleft()
                if word == endWord:
                    return distance + 1
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for next_word in graph[pattern]:
                        if next_word in visited:
                            continue
                        visited.add(next_word)
                        dq.append(next_word)
            distance += 1
        return 0
            
  
                            
                    

        
