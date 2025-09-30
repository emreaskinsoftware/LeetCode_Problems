class Solution(object):
    def containsDuplicate(self, nums):        
        mevcut = set()
        for num in nums:
            if num in mevcut:
                return True
            mevcut.add(num)
        
        return False
        