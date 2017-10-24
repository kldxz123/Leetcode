class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ""
        if len(strs) == 0:
            return s
        min_length = 9999999999999999
        for i in strs:
            if i == "":
                return s
            if min_length > len(i):
                min_length = len(i)
        index = 0
        while index < min_length:
            tmp = strs[0][index]
            for i in strs:
                if i[index] != tmp:
                    return s
            s += tmp
            index += 1
        return s