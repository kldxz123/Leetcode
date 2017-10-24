import Queue
class Solution(object):
	def dft(self, flag, heater):
		if header - 1 not in flag and heater + 1 not in flag:
			return 1
		if heater - 1 in flag and heater + 1 not in flag:
			if flag[heater - 1] == 1:
				return 1
			else:
				flag[heater - 1] = 1
				return 1 + self.dft(flag,heater - 1)
		if heater - 1 not in flag and heater + 1 in flag:
			if flag[heater + 1] == 1:
				return 1
			else:
				flag[heater + 1] = 1
				return 1 + self.dft(flag,heater + 1)
		a = 0
		b = 0
		if flag[heater - 1] == 0:
			flag[heater - 1] = 1
			a = self.dft(flag,heater - 1)
		if flag[heater + 1] == 0:
			flag[heater + 1] = 1
			b = self.dft(flag,heater - 1)
		return max(a,b)




    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        flag = {}
        for i in houses:
        	flag[i] = 0

        q = Queue()
        max = 0
        for i in heaters:
        	q.put(i)
        	flag[i] = 1
        	tmp = dft(flag,i)
        	if tmp

        
