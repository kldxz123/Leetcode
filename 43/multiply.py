class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
        	return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = ""
        def addStr(str1,str2):
        	longStr = ""
        	shortStr = ""
        	if len(str1) > len(str2):
        		longStr = str1
        		shortStr = str2
        	else:
        		longStr = str2
        		shortStr = str1
        	p = 0
        	l = ""
        	print(longStr,shortStr)
        	i = 0
        	while i <= len(shortStr) -1:
        		tmp = int(longStr[i]) + int(shortStr[i]) + p
        		#print(tmp)
        		if tmp >= 10:
        			l  += str(tmp - 10)
        			p = 1
        		else:
        			l += str(tmp)
        			p = 0
        		i += 1

        	while i <= len(longStr) - 1:
        		tmp = p + int(longStr[i])
        		if tmp >= 10:
        			l += str(tmp - 10)
        			p = 1
        		else:
        			l += str(tmp)
        			p = 0
        		i += 1

        	if p == 1:
        		l += "1"
        	return l

        def mul(charNum,stringNum):
        	result = ""
        	p = 0
        	num = int(charNum)
        	for i in range(len(stringNum)):
        		tmp = num * int(stringNum[i]) + p
        		a = tmp % 10
        		p = int(tmp/10)
        		result += str(a)
        	if p != 0:
        		result += str(p)
        	return result

        for i in range(len(num1)):
        	if num1[i] != 0:
        		r = ""
        		mulResult = mul(num1[i],num2)
        		#print(mulResult)
        		j = 0
        		while j < i:
        			r += "0"
        			j += 1
        		r += mulResult
        		result = addStr(result,r)
        	

        return result[::-1]

sol = Solution()
print(sol.multiply("0","999"))




