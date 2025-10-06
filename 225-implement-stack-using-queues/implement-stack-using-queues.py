from collections import deque
class MyStack(object):

    def __init__(self):
        self.MyStack = deque()

    def push(self, x):
        self.MyStack.append(x)

    def pop(self):
        #return self.MyStack.pop()
        for i in range(len(self.MyStack)-1):
            self.MyStack.append(self.MyStack.popleft())
        return self.MyStack.popleft()        

    def top(self):
        return self.MyStack[-1]
        

    def empty(self):
        return not self.MyStack