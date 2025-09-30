class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        result = next(key for key, value in count.items() if value == 1)
        return result   
       
       

        