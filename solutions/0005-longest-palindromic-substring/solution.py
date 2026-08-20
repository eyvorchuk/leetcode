class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        longest_palindrome = s[0]
        for i in range(len(s)):
            for j in range(i + max_length, len(s)):
                sub = s[i:j+1]
                is_palindrome = True
                for k in range(len(sub) // 2):
                    if sub[k] != sub[-1 - k]:
                        is_palindrome = False
                        break
                if is_palindrome and len(sub) > max_length:
                    max_length = len(sub)
                    longest_palindrome = sub
        return longest_palindrome

