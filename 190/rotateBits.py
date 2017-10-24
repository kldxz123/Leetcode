class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		b = bin(n)
		a = b[2:len(b)]
		a = a[::-1]
		for i in range(32 - len(b) + 2):
			a += '0'
		#print(len(a))
		c = int(a,2)
		#print(c)
		return c
sol = Solution()
n = 10
print(sol.reverseBits(n))
        