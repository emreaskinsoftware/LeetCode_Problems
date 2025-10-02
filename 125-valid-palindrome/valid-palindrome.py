class Solution(object):
    def isPalindrome(self, s):
        tmp = ""
        for ch in s:
            if ch.isalnum():
                tmp += ch.lower()
        if len(tmp) <= 1:
            return True
        return tmp == tmp[::-1]
        