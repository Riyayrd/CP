#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i   
        return -1  
