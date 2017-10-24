class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        tmp = []
        count_tmp = m + n -1
        while i < m and j < n:
        	if nums1[i] < nums2[j]:
        		tmp.append(nums1[i])
        		i += 1
        	else:
        		tmp.append(nums2[j])
        		j += 1
        while i < m:
        	tmp.append(nums1[i])
        	i += 1
        while j < n:
        	tmp.append(nums2[j])
        	j += 1

        while tmp:
        	nums1[count_tmp] = tmp.pop()
        	count_tmp -= 1
        
        print(nums1)


numsa = [1,0]
numsb = [2]
sol = Solution()
sol.merge(numsa,1,numsb,1)


