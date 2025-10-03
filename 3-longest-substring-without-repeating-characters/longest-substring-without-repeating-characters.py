class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last = {}        # karakter -> en son görüldüğü index
        start = 0        # pencerenin başlangıcı
        best = 0         # en uzun substring uzunluğu

        for j, ch in enumerate(s):
            if ch in last and last[ch] >= start:
                # karakter tekrar etti, pencereyi kaydır
                start = last[ch] + 1
            last[ch] = j  # son görüldüğü index'i güncelle
            best = max(best, j - start + 1)  # en uzunluğu güncelle

        return best