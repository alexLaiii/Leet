"""Formats words into fully justified lines of exactly maxWidth characters.

Packs words greedily (as many as fit per line), then distributes
extra spaces between words as evenly as possible, with any leftover
space assigned to the leftmost gaps first. Lines with a single word,
and the final line, are left-justified with padding on the right.

Args:
    words: List of non-empty words to justify. Each word's length is
        guaranteed not to exceed maxWidth.
    maxWidth: The exact character width each output line must have.

Returns:
    A list of strings, each of length exactly maxWidth, representing
    the justified text.
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        word_count = c_count = 0
        res = []
        lines = []
        for i in range(len(words)):
            w = words[i]
            if c_count + word_count + len(w) <= maxWidth:
                lines.append(w)
                c_count += len(w)
                word_count += 1
            else:
                spaces = maxWidth - c_count
                if word_count == 1:
                    res.append(lines[0] + (" " * spaces))
                else:
                    each_gap = spaces // (word_count - 1)
                    remain_spaces = spaces % (word_count - 1)
                    s = ""
                    for j in range(len(lines) - 1):
                        gap = " " * each_gap 
                        if remain_spaces > 0:
                            gap += " "
                            remain_spaces -= 1
                        s += lines[j] + gap
                    s += lines[-1]
                    res.append(s)
                c_count = len(w)
                word_count = 1
                lines = [w]
          
            
        if lines:
            trailing_space = maxWidth - c_count - (len(lines) - 1)
            s = ""
            for j in range(len(lines) - 1):
                s += lines[j] + " "
            s += lines[-1] + (" " * trailing_space)
            res.append(s)

        return res
