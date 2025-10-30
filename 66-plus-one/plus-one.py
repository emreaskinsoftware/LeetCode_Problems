class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10**(len(digits)-i-1)
            if i == len(digits)-1:
                num += 1
        new_digits = []
        for n in str(num):
            new_digits.append(int(n))
        return new_digits