class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        t = []
        t.append(x)
        if len(self.stack) == 0:
            t.append(x)
        else:
            if self.stack[-1][1] > x:
                t.append(x)
            else:
                t.append(self.stack[-1][1])
        self.stack.append(t)
        
    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()[0]
    def top(self):
        """
        :rtype: int

        """
        if len(self.stack)== 0:
            return None

        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()

minStack.push(-2)
print(minStack.getMin())

minStack.push(0)
print(minStack.getMin())

minStack.push(-3)
print(minStack.getMin())


minStack.getMin()

print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
