class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) == 0:
		    return False
		count = {}
		for i in nums:
			if count.get(i) == None:
				count[i] = 1
			else:
				count[i] += 1
		for i in count:
			if count[i] >= 2:
				return True
		return False

        