class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = num1[::-1]
        b = num2[::-1]
        s = ''
        if len(a) > len(b):
        	long_str = a
        	long_len = len(a)
        	short_str = b
        	short_str = len(b)
        else:
        	long_str = b
        	long_len = len(b)
        	short_str = a
        	short_len = len(a)
        flag = 0
        for i in range(short_len):
        	tmp = int(long_str[i]) + int(short_str[i]) + flag
        	if tmp < 10:
        		s = s + str(tmp)
        		flag = 0
        	else:
        		x = tmp - 10
        		flag = 1
        		s = s + str(x)
        for i in range(long_len - short_len):
        	tmp = int(long_str[i + short_len]) + flag
        	if tmp < 10:
        		s = s +str(tmp)
        		flag = 0
        	else:
        		x = tmp - 10
        		flag = 1
        		s = s + str(x)
        if flag == 1:
        	s = s + '1'
        return s[::-1]
        
sol = Solution()
num1 = "1"
num2 = "99"
print(sol.addStrings(num1,num2))