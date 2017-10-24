import re
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = re.search(needle,haystack)
        print(a)
sol = Solution()
needle = "tangg"
haystack = "Hi, tang tang is a good man"
sol.strStr(haystack,needle);
