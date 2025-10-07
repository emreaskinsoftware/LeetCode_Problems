class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        myStack = []
        for index, temp in enumerate(temperatures):
            while myStack and temp > myStack[-1][0]: 
                  stackTemp,StackIndex = myStack.pop()
                  answers[StackIndex] = index- StackIndex  
            myStack.append([temp,index])      
        return answers
