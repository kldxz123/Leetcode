class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        array = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        s = ''
        if num == 0:
        	return "0"
        sign = num & 0x80000000
        if sign == 0:
        	a = 0xf0000000
        	tmp = a & num
        	tmp = tmp >> 28
        	count = 0
        	while tmp == 0 and count < 8:
        		num = num << 4
        		tmp = a & num 
        		tmp = tmp>>28
        		count += 1
        	for i in range(8 - count):
        		s = s + array[tmp]
        		num = num << 4
        		tmp = a & num 
        		tmp = tmp >> 28
        		
        else:
        	num = num ^ 0xffffffff+1
        	a = 0x0000000f
        	tmp = a & num
        	for i in range(8):
        		s = array[tmp] + s
        		num = num >> 4
        		tmp = a & num
        return s
sol = Solution()
print(sol.toHex(1000000000))