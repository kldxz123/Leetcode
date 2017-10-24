###6. ZigZag Conversion 

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = []
        for i in range(numRows):
        	x = []
        	result.append(x)

        for c,i in enumerate(s):
        	a = c % (2*numRows- 2)
        	
        	if a < numRows:
        		b = a
        	else:
        		b = 2 * numRows - 2 - a
        	result[b].append(i)
            
        ss = ""
        for i in result:
            a = ""
            for x in i:
                a += x
            ss += a
        return ss

sol = Solution()

print(sol.convert("PAYPALISHIRING",4))


