class Solution(object):
    def majorityElement(self, nums):
        f = {}
        for num in nums:
            if num not in f:
                f[num] = 1
            else:
                f[num] += 1
        result = [x for x,y in f.items() if y > len(nums)/2]  
        return result[0]      