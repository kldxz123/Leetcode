class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		pos ={}
		p = 0
		a = False
		for i in nums:
			if pos.get(i) == None:
				pos[i] = p
			else:
				if p - pos[i] <= k:
					a = True
				else:
				    pos[i] = p
			p += 1
		return a
a = [-2,-2]
sol = Solution()
print(sol.containsNearbyDuplicate(a,2))