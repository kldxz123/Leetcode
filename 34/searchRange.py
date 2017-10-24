class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def subSearch(left,right):
            if left > right:
                return [-1,-1]
            mid = int((left + right) / 2)
        	
            if nums[mid] == target:	
                if left == right:
                    return [mid,mid]

                l = subSearch(left,mid - 1)
                r = subSearch(mid + 1,right)
                if l == [-1,-1]:
                    if r == [-1,-1]:
                        return [mid,mid]
                    else:
                        return [mid,r[1]]
                else:
                    if r == [-1,-1]:
                        return [l[0],mid]
                    else:
                        return [l[0],r[1]]

        		
            elif nums[mid] > target:
                return subSearch(left,mid - 1)
            else:
                return subSearch(mid + 1,right)
        return subSearch(0,len(nums) - 1)

sol = Solution()
a = [0,0,1,1,2,2,2,2,3,3,4,4,4,5,6,6,6,7,8,8]

print(sol.searchRange(a,4))