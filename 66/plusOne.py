class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = digits[::-1]
        b = []
        f = 1
        for i in a:
        	if f == 1:
        		tmp = i + 1	
        		if tmp == 10:
        			b.append(0)
        			f = 1
        		else:
        			b.append(tmp)
        			f = 0
        	else:
        		b.append(i)
        if f == 1:
        	b.append(1)
        return b[::-1]
sol = Solution()
digits = [9,9,9,9]
print(sol.plusOne(digits))
