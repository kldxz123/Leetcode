class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        array = [([0]*length) for i in range(length)]
        for i in range(length):
            array[i][i] = 1
        x = 0
        y = 1
        k = 1
        best_x = 0
        best_y = 0
        while x >= 0 and y <= length - 1:
            if s[x] == s[y]:
                if y - x == 1 or y - x == 2:
                    array[x][y] = 1 
                    best_x = x
                    best_y = y
                else:
                    if array[x+1][y-1] == 1:
                        array[x][y] = 1
                        best_x = x
                        best_y = y
            if k == 1:
                x += 1
                y += 1
            else:
                x -= 1
                y -= 1
            if y == length and x != 0:
                y = length - 1
                x -= 2
                k = 0
            if y != length -1 and x == -1:
                x = 0
                y += 2
                k = 1

        return s[best_x:best_y+1]

sol = Solution()
print(sol.longestPalindrome("cbbd"))
