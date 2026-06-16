class Solution:
    def processStr(self, s: str) -> str:
        """
        Simulates the special operations while building the result in a list.

        Normal letters are appended to the result. A '#' duplicates the current
        result, '*' removes the last character if possible, and '%' reverses the
        current result. Finally, the character list is joined into a string.
        """
        res = []

        for c in s:
            if c == '#':
                res += res
            elif c == "*":
                if res:
                    res.pop()
            elif c == "%":
                res = res[::-1]
            else:
                res.append(c)

        return "".join(res)
