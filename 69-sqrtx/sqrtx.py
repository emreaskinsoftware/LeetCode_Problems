class Solution(object):
    def mySqrt(self, x):
        alt = 0 
        ust = x 
        mid = (alt+ust)/2 
        if x==0: 
            return 0 
        if x == 1: 
            return 1 
        while abs(mid*mid - x) > 1e-6: 
            if mid*mid < x: 
                alt = mid 
            else: ust =mid 
            mid =(alt+ust)*0.5 
        return int(mid)