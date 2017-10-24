class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = set(nums1)
        b = set(nums2)
        c = []
        for i in b:
        	if i in a:
        		c.append(i)
        return c

sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersection(nums1,nums2))