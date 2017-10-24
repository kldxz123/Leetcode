from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = Counter(nums1)
        b = Counter(nums2)
        c = []
        for i in a:
        	for j in range(min(a[i],b[i])):
        		c.append(i)
        return c
sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersect(nums1,nums2))