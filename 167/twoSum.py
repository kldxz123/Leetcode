class Solution(object):
	def findNum(self,numbers,target):
		start = 0
		end = len(numbers) - 1
		while start <= end:
			middle = int((start + end)/2)
			if numbers[middle] == target:
				return middle
			if numbers[middle] > target:
				end = middle - 1
			if numbers[middle] < target:
				start = middle + 1
		return -1

	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in range(len(numbers) - 1):
			s = target - numbers[i]
			sol = Solution()
			a = self.findNum(numbers[i+1:len(numbers)],s)
			if a != -1:
				t = [i + 1,a + i + 2]
				return t



p = [2,7,11,15]
sol = Solution()
print(sol.twoSum(p,9))