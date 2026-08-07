"""
Simplify a Unix-style absolute file path to its canonical form.

Splits the path on "/" and processes each segment with a stack:
- Empty segments (from "//" or leading/trailing "/") and "." are ignored.
- ".." pops the last directory off the stack (if any), moving up one level.
- Any other segment is treated as a valid directory/file name and pushed
  onto the stack.

The canonical path is then rebuilt by joining the stack with "/",
prefixed with a leading "/".

Args:
    path: The original absolute path (starts with "/").

Returns:
    The simplified canonical path.

Time:  O(n), where n is the length of path.
Space: O(n), for the split list and stack.
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for d in path:
            if not d or d == ".":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return "/" + "/".join(stack) 
            
        
        
        
        
        
