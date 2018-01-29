class Solution:
    def isPalindrome(self, s):
        l = len(s)
        i, j = 0, l - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s):
        if len(s) == 0:
            return None
        lp = s[0]
        for i in range(len(s)):
            p = s[i:]
            for j in range(len(p), 0, -1):
                l = p[0:j]
                if self.isPalindrome(l):
                    if len(l) > len(lp):
                        lp = l
        return lp
