class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10**(len(digits)-i-1)
            if i == len(digits)-1:
                num += 1
        num = str(num)
        return [int(i) for i in num]
        