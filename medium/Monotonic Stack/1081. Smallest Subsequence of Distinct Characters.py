 """
Return the lexicographically smallest subsequence of `s` that contains
every distinct character exactly once.

Approach:
- First, record the last index at which each character appears.
- Use a monotonic increasing stack to build the answer greedily.
- Maintain a `visited` set so that each character is added at most once.
- When processing a new character:
    1. If it is already in the subsequence, skip it.
    2. Otherwise, while the stack is non-empty and the current
       character is smaller than the top of the stack, attempt to
       improve the lexicographical order.
    3. A character can only be removed from the stack if it appears
       again later in the string (i.e., we have not passed its last
       occurrence). If it will not appear again, we must keep it.
    4. Push the current character onto the stack and mark it as seen.

The stack is maintained such that it represents the lexicographically
smallest valid subsequence seen so far.

Time Complexity:
    O(n)
    Each character is pushed onto and popped from the stack at most once.

Space Complexity:
    O(k)
    Where k is the number of distinct characters in `s`
    (at most 26 for lowercase English letters).
"""

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_idx = defaultdict(int)
        for i in range(len(s)):
            last_idx[s[i]] = i
        
        m_stack = []
        visited = set()
        for i in range(len(s)):
            curr_c = s[i]
            if curr_c in visited:
                continue
            while m_stack and ord(curr_c) < ord(m_stack[-1]):
                if i > last_idx[m_stack[-1]]:
                    break
                visited.remove(m_stack[-1])
                m_stack.pop()
            visited.add(curr_c)
            m_stack.append(curr_c)
            
        return "".join(m_stack)
