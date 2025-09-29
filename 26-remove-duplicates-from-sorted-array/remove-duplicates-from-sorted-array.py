class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # write index (kaç tane unique yazıldı)
        k = 1  

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:   # öncekiyle aynı değilse yeni unique bulunmuş
                nums[k] = nums[i]       # yeni unique'i nums[k]'ye yaz
                k += 1                  # k'yı arttır

        return k

        