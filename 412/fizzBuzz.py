class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = []
        for i in range(n):
        	num = i + 1
        	s = ''
        	if num % 3 == 0 and num % 5 != 0:
        		s = 'Fizz'
        	elif num % 5 == 0 and num % 3 != 0:
        		s = 'Buzz'
        	elif num % 3 == 0 and num % 5 == 0:
        	    s = 'FizzBuzz'
        	else:
        	    s = str(num)
        	a.append(s)
        return a