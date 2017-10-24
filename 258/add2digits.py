class Solution(object):
	def addDigits(self, num):
		if num < 10:
			return num
		a = 0
		while num:
			a += num % 10
			num = int(num / 10)
		return self.addDigits(a)

x = 38
sol = Solution()
print(sol.addDigits(x))  