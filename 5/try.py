
'''
from functools import reduce
import sys
import collections
sum=reduce(lambda x,y:x+y,(1,2,3,4,5,6,7))   
print(sum) 

print(sys.maxsize)

x = [1,2,3,4,1,2,3]
x.reverse()
print(x[1:4])

print(dict(collections.Counter(x)))

x = [1,4,7]
y = [1,4,7]

for i in range(-1,2):
	print(i)
a = "asdfg"
print(a[::-1])
'''
def addStr(str1,str2):
	longStr = ""
	shortStr = ""
	if len(str1) > len(str2):
		longStr = str1
		shortStr = str2
	else:
		longStr = str2
		shortStr = str1
	p = 0
	l = ""
	print(longStr,shortStr)
	i = 0
	while i <= len(shortStr) -1:
		tmp = int(longStr[i]) + int(shortStr[i]) + p
		print(tmp)
		if tmp >= 10:
			l  += str(tmp - 10)
			p = 1
		else:
			l += str(tmp)
			p = 0
		i += 1

	while i <= len(longStr) - 1:
		tmp = p + int(longStr[i])
		if tmp >= 10:
			l += str(tmp - 10)
			p = 1
		else:
			l += str(tmp)
			p = 0
		i += 1

	if p == 1:
		l += "1"
	return l
#print(addStr("123","34"))
'''
a = [1,2,3,4,5]
a.remove(5)
print(a)
'''
'''
A = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
A[:] = map(list,zip(*A[::-1]))
print(A)
'''
'''
import collections

x = "abc"
y = "abc"
xx = dict(collections.Counter(x))
yy = dict(collections.Counter(y))
if xx == yy:
	print("OK")
else:
	print("False")
'''
string = "dshjgjh"
tmp = "".join((lambda x:(x.sort(),x)[1])(list(string)))
print(tmp)

