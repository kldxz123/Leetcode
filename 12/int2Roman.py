class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ""
        while num >= 1000:
        	s += "M"
        	num = num - 1000
        if num >= 900:
        	s += "CM"
        	num = num - 900
        if num >= 500:
        	s += "D"
        	num = num - 500
        if num >= 400:
        	s += "CD"
        	num = num - 400
        while num >= 100:
        	s += "C"
        	num = num - 100
        if num >= 90:
        	s += "XC"
        	num = num - 90
        if num >= 50:
        	s += "L"
        	num = num - 50
        if num >= 40:
        	s += "XL"
        	num = num - 40
        while num >= 10:
        	s += "X"
        	num = num - 10
        dic = {0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        s += dic[num]
        return s

sol = Solution()
print(sol.intToRoman(40))
        