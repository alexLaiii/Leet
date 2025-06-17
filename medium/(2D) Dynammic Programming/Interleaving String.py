"""
Idea:
An Interleaving String is to determine If a string s3 can form by using all the characters from s1 and s2 but perceiving their orders.

Why 3 pointer approach doesn't work. 
    First I try to maintain a 3 pointer appraoch on s1,s2,s3 respectively
    But I ran into problem quickly,Consider Example:
    s1 = "aabc"
    s2 = "abad"
    s3= "aabadabc"
    You can realize along your decision of picking from s1 or s2, you have so many choice as consider valid at that point,
    but end up only one specific way is possible to reach the end.
    So how to decide which path we take at that point?

    Thats why we use dynammic programming to cache the previous result, and only continue if the previous path that build the current path is valid

    In each DP cell, we stored:
    if we took j character from s1, and i character from s2, can we form the substring s3[i + j]?
    Since this path is taking j character from s1, and i character from s2, so the previous path of this must be one of these cases(or both):
        1. the current path is based on taking j - 1 character from s1, and i character from s2
        2. the current path is based on taking j character from s1, and i - 1 character from s2
    If one of these previous path is valid, means at least one of these can built s3[i + j - 1], then the current path is also valid if
        # want to take from s1
        1. the current path is based on taking j - 1 character from s1, and i character from s2, then the j th character of s1 must match the i + j character of s3
        # want to take from s2
        2. the current path is based on taking j character from s1, and i - 1 character from s2, the the i th character of s2 must match the i + j character of s3
    If both previous path is not valid, or the i, j of s1 s2 doesnt match s3, then the current path is not valid, and theres no way to built further, this path is Closed.

    Time complexity: O(m * n), m is the length of s2, n is the length of s1. And we travel through the entire DP grid
    Space complexity: O(m * n), DP grid with size m*n
        

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lenS1, lenS2 = len(s1),len(s2)
        if lenS1 + lenS2 != len(s3):
            return False
        dp= [[False for j in range(lenS1 + 1)] for i in range(lenS2 + 1)]
        dp[0][0] = True
        for i in range(lenS2 + 1):
            for j in range(lenS1 + 1):
                # Take from s1
                if j > 0 and dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                # Take from s2
                if i > 0 and dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
        return dp[lenS2][lenS1]
                
            

                    
        
        
        
