class Solution(object):
    def romanToInt(self, s):
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num = 0
        prev = 0
        for ch in s[::-1]:  
            val = values[ch]
            if val < prev:
                num -= val
            else:
                num += val
            prev = val
        return num
