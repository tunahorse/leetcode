

# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 
 
# String, return the logest palindromic substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        # Function to expand around the center and find a palindrome
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome
            return s[left + 1:right]
            
        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            tmp = expandAroundCenter(i, i)
            if len(tmp) > len(longest):
                longest = tmp
                
            # Even length palindrome
            tmp = expandAroundCenter(i, i + 1)
            if len(tmp) > len(longest):
                longest = tmp
            
        return longest
