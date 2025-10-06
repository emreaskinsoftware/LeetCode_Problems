class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = { ')': '(', ']': '[', '}': '{' }
        opens = set(mapping.values())

        for ch in s:
            if ch in opens:
                stack.append(ch)                
            else:                
                if len(stack) ==0:
                    return False               
                if stack[-1] ==mapping[ch]:               
                    stack.pop()
                else:
                    return False       
        return len(stack) == 0


            
        