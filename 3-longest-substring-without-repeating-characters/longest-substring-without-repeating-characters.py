class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0
        best = 1
        for i in range(n):
            seen = set()
            for j in range(i, n):          # j dahil
                if s[j] in seen:           # tekrar gördüysek kır
                    break
                seen.add(s[j])
                best = max(best, j - i + 1)
        return best