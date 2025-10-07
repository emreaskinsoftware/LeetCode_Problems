class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if len(operations) == 0:
            return 0
        ops = []
        
        for i in range(len(operations)):
            op = operations[i]
            if op == "C":
                ops.pop()
            elif op == "+":
                ops.append(ops[-1]+ops[-2])
            elif op == "D":
                ops.append(ops[-1]*2)
            else:
                ops.append(int(op))
        
        return sum(ops)
            