  """
  Reverse the order of words in a string using a right-to-left scan.

  Summary
  -------
  Walk the string from the end. For each iteration:
  1) Skip trailing/inter-word spaces and set `r` to the last non-space index.
  2) Move `l` left until you reach the start of that word.
  3) Append the slice s[l:r+1] to `word_list`.
  4) Continue scanning left for the next word.
  Finally, join the collected words with a single space.

  How the pointers work (mapping to this implementation)
  ------------------------------------------------------
  - `r` always marks the end of the *next* word to append.
    When skipping spaces (`while l > 0 and s[l] == ' ':`), we also set `r = l`
    so `r` lands on the last non-space char (the word end).
  - We shrink `l` one step at a time. A word boundary is detected when either:
      * `l == 0 and s[l] != ' '`  → word starts at index 0
      * `l - 1 >= 0 and s[l-1] == ' '` → the char before `l` is a space
    In both cases, the current word is `s[l : r+1]`.
  - After recording the word, we continue moving `l` left to look for the
    previous word.

  Why this is correct
  -------------------
  - Every time we set `r`, it points at the last character of some word
    (we only move it after skipping spaces).
  - We only append when we have a full word `[l .. r]`:
      * The left boundary is correct because we stop at the first index `l`
        such that the previous char is a space (or `l == 0`).
      * The right boundary `r` is correct by construction.
  - Each character belongs to at most one appended slice, so each word is
    captured exactly once, in reverse order of appearance.
  - Joining with `" ".join(word_list)` collapses multiple spaces and trims
    leading/trailing spaces per the problem’s requirement.

  Complexity
  ----------
  Time:  O(n) — each index is visited O(1) times while scanning left.
  Space: O(k) — where k is the number of words (to store `word_list` before join).

  Edge cases handled
  ------------------
  - Leading/trailing/multiple spaces (they’re skipped and not copied).
  - Empty string or all spaces → returns "".
  - Single-word strings → returned unchanged.
  """


class Solution:
    def reverseWords(self, s: str) -> str:
        word_list= []
        l = len(s) - 1
        r = len(s) - 1
        while l > -1:
            while l > 0 and s[l] == " ":
                l -= 1
                r = l
            if l == 0 and s[l] != " ":
                word_list.append(s[l:r + 1])
            elif l != 0 and s[l-1] == " ":
                word_list.append(s[l:r + 1])
            l -= 1
       
        
        return " ".join(word_list)
        
