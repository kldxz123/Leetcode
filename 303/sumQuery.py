class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.List = []
        for c,i in enumerate(nums):
            a = []
            a.append(i)
            if c == 0:
                a.append(i)
            else:
                a.append(i+self.List[c - 1][1])
            self.List.append(a)
        print(self.List)

        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.List[j][1]
        return self.List[j][1] - self.List[i - 1][1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
nums = [-2,0,3,-5,2,-1]
sol = NumArray(nums)
print(sol.sumRange(0,5))