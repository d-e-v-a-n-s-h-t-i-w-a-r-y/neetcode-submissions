class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        newStr = "".join(chars)
        return newStr == newStr[::-1]