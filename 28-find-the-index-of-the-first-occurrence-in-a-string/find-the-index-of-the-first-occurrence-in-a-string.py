class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        n = len(haystack)
        m = len(needle)

        for l in range(n - m + 1):
            if haystack[l:l+m] == needle:
                return l

        return -1
        
        
