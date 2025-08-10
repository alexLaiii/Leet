"""
Deep-copy a linked list where each node has:
  - `next` (the usual next pointer)
  - `random` (can point to any node in the list or None)

Approach (2-pass with hashmap):
1) First pass: iterate the original list in order. For each original node `curr`,
   create its copy `cpy` with the same `val`, append `cpy` to the cloned `next`
   chain, and record a mapping: original -> copy in `hash_map`.
   At the end of this pass, the cloned list has correct `next` pointers but all
   `random` pointers are still None.

2) Second pass: walk the original and cloned lists in lockstep. For each original
   node `curr`, if `curr.random` is not None, set the cloned node’s random to
   `hash_map[curr.random]`. The hashmap gives O(1) access to the corresponding
   clone of any original node.

Why this works:
- Every original node is created exactly once and stored in the map, so any random
  reference can be resolved in constant time.
- We separate building the `next` chain from wiring `random` to avoid looking up
  nodes that haven’t been created yet.

Complexity:
- Time: O(n) — each node is visited a constant number of times.
- Space: O(n) — the hashmap stores one entry per node.

Edge cases covered:
- Empty list (`head is None`) -> returns None.
- Nodes whose `random` is None.
- Multiple nodes sharing the same `random` target.
- `random` pointers forming arbitrary graphs (including self-loops).
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        curr_cpy = dummy
        curr = head
        hash_map = {}
        while curr:
            curr_cpy.next = Node(curr.val)
            curr_cpy = curr_cpy.next
            hash_map[curr] = curr_cpy
            curr = curr.next
        
        curr = head
        curr_cpy = dummy.next
        while curr:
            if curr.random:
                curr_cpy.random = hash_map[curr.random]
            curr = curr.next
            curr_cpy = curr_cpy.next
        return dummy.next
            

            

            
            
