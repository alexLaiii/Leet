"""
This problem rotted my brain — it's a decision tree + DP sum-up problem that I failed to realize at first.

Why Decision Tree?

Consider: "2121"

                                 "2121"
                                /      \
                             "2"        "21"
                            /   \        /   \
                         "1"   "12"    "2"   "21"
                        /   \     \     |      
                     "2"   "21"   "1"  "1"     
                      |      
                    "1"   

We have 5 valid paths in this tree, so the result for "2121" is 5.
Each step gives us two options: decode 1 digit or 2 digits — each leads to a completely different path.

Why DP?

Now consider substrings:

"121"
                                "121"
                              /      \
                           "1"        "12"
                          /   \        /   
                       "2"   "21"    "1"   
→ Result = 3

"21"
                                "21"
                              /      \
                           "2"        "21"
                          /  
                       "1"   
→ Result = 2

"1"
                                "1"
                              /      
                           "1"        
→ Result = 1

Notice the pattern:
- Result("2121") = Result("121") + Result("21") = 3 + 2 = 5  
- Result("121") = Result("21") + Result("1") = 2 + 1 = 3  
- Result("21") = Result("1") + Result("") = 1 + 1 = 2  

So we model this as:  
    `dp[i] = dp[i - 1] + dp[i - 2]`  
Classic DP with overlapping subproblems.

Edge Case Handling:

Now consider: "1106"

                                 "1106"
                                /      \
                             "1"        "11"
                            /   \        /   \
                         "1"   "10"    "0"   "06"
                        /   \     \           
                     "0"   "06"   "6"    
→ Only one valid path → Result = 1  
("0" and "06" are invalid encodings)

How to handle this?

At each step:
- Take 1 digit → valid only if it's not "0"
- Take 2 digits → valid only if 10 <= value <= 26

So:
- If 1-digit is valid → add dp[i - 1]
- If 2-digit is valid → add dp[i - 2]
- If both invalid → dp[i] = 0

Example: "20011"
- '2': OK
- '0': can't use single digit; "20" is valid → OK
- next '0': "00" is invalid → dp = 0
- next '1': "01" is invalid → still dp = 0
- next '1': again, both paths blocked → dp = 0 → return 0

If still unclear, compare:

**Case: "2121"**  
                                 "2121"
                                /      \
                             "2"        "21"
                            /   \        /   \
                         "1"   "12"    "2"   "21"
                        /   \     \     |      
                     "2"   "21"   "1"  "1"     
                      |      
                    "1"   
→ Result = 5

**Case: "4121"**  
                                 "4121"
                                /      
                             "4"        
                            /   \        
                         "1"   "12"       
                        /   \     \         
                     "2"   "21"   "1"      
                      |      
                    "1"   
→ Result = 3  
("41" is invalid, so the `dp[i - 2]` part is not added — only `dp[i - 1]` survives)

**Case: "0121"**  
                                 "0121"
                                /      \
                             "0"        "01"
→ Result = 0  
("0" and "01" are both invalid → neither `dp[i - 1]` nor `dp[i - 2]` is used)

Time Complexity:
- O(n): One pass through the string

Space Complexity:
- O(1): Optimized DP with only two scalar variables
"""

class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == "0":
            return 0
        prev_double, prev_single = 1, 1
        for i in range(1, len(s)):
            curr_count = 0
            one_digits = int(s[i])
            two_digits = int(s[i - 1: i + 1])
            if 10 <= two_digits <= 26:
                curr_count += prev_double
            if one_digits > 0:
                curr_count += prev_single
            if curr_count == 0:
                return 0
     
            prev_double, prev_single = prev_single, curr_count

        return prev_single


                







