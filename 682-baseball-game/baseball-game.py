class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if len(operations) == 0:
            return 0
        ops = []       
        for op in operations:
            if op == "C":
                ops.pop()
            elif op == "+":
                ops.append(ops[-1]+ops[-2])
            elif op == "D":
                ops.append(ops[-1]*2)
            else:
                ops.append(int(op))
        
        return sum(ops)
            