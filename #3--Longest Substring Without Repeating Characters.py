class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        else:
            i = 0
            j = 1
            substring = s[i]
            len_substring = [len(substring)]
            while j < len(s):
                if s[j] not in substring:
                    j += 1
                    substring = s[i:j]
                    len_substring.append(len(substring))
                else:
                    i = s.index(s[j]) + 1
                    substring = s[i:j + 1]
                    s = s[i:]
                    j = j + 1 - i
                    i = 0
            return max(len_substring)
