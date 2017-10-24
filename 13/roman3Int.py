class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        dic = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        
        while i < len(s) - 1:
        	if s[i:i+2] in dic:
        		num += dic[s[i:i+2]]
        		i += 2
        		
        	else:
        		num += dic[s[i]]
        		i += 1
        if i == len(s) - 1:
        	num += dic[s[i]]
        return num

sol = Solution()
print(sol.romanToInt("MCCLVIII"))

        