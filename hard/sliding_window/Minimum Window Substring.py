"""
This problem's technique is similar to "Permutation Strings" — revisit that if forgotten.

Since we only care about whether the substring `s` has **enough characters to cover all characters in string `t`**, here’s the breakdown:

1. Like before, we create two hash tables to store the character counts:
   - `t_table` for the target string `t`
   - `win_table` for the sliding window in `s`
   - But this time, we **only store characters that appear in `t`**, because any other character is irrelevant.

2. In the first loop:
   - Initialize `t_table` with character counts from `t`
   - Simultaneously initialize the same keys in `win_table` with 0 (so it’s ready for counting during the sliding window)

3. Initialize other variables:
   - `require_matches`: number of unique characters that need to match (i.e., `len(t_table)`)
   - `matches`: tracks how many characters currently match their required counts
   - `left`: the left index of the current window
   - `length`: the length of the best result found so far  
     (initialized to `len(s) + 1` so it guarantees an update if a valid window is found)
   - `result`: an array `[left, right]` storing the current best window’s indices

Main loop:
- Start sliding the window with `right` expanding from 0
- If `s[right]` is **not in `t_table`**, ignore it
- If `s[right]` **is** in `t_table`, increment `win_table[s[right]]`
   - If the count matches `t_table[s[right]]`, increment `matches`

When `matches == require_matches`:
→ A valid window is found

Now:
1. Check if the current window size is **smaller** than the current `length`  
   - If yes: update `length` and `result`  
   - If no: keep current best

2. Try to shrink the window from the left:
   - If `s[left]` is **not in `t_table`**, just move `left` forward (skip useless characters)
   - If `s[left]` **is in `t_table`**:
     - Decrement `win_table[s[left]]`
     - If `win_table[s[left]] < t_table[s[left]]` after decrement:
         → The window becomes invalid  
         → Decrement `matches`  
         → Move `left` forward and **exit** the `while` (window is no longer valid)
     - Otherwise: keep shrinking

Repeat the above until the `right` pointer has scanned all of `s`

Return value:
- If no valid window was found → `length == len(s) + 1`, return `""`
- Otherwise, return `s[result[0]:result[1] + 1]`  
  (`+1` because Python slicing excludes the right index)

"""





class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s): return ""
        t_table, win_table, require_matches, matches = {},{}, 0, 0
        
        for c in t:
            t_table[c] = 1 + t_table.get(c, 0)
            win_table[c] = win_table.get(c, 0)
        
        require_matches = len(t_table)
        left, length, result = 0, len(s) + 1, [-1,-1]

        for right in range(len(s)):
            if s[right] in t_table:
                win_table[s[right]] += 1
                if win_table[s[right]] == t_table[s[right]]:
                    matches += 1
            # start popping
            while matches == require_matches:
                if length > right - left + 1:
                    length = right-left + 1
                    result = [left, right]
                if s[left] in win_table:
                    win_table[s[left]] -= 1
                    if win_table[s[left]] < t_table[s[left]]:
                        matches -= 1
                left += 1
        
        # The string not exist if length == len(s) + 1
        return s[result[0]: result[1] + 1] if length != len(s) + 1 else  ""
                
