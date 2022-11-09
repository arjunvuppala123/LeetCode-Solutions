class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum())
        s = s.lower()
        return s == s[::-1]