class Solution(object):
    def majorityElement(self, nums):
        etkin,adet = 0,0
        for num in nums:
            if adet == 0:
                etkin = num
            if num == etkin :
                adet +=1
            else:
                adet -= 1       
        return etkin