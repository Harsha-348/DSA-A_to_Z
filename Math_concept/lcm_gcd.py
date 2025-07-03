from math import gcd
class Solution:
    def GCDandLCM(self, n1, n2):

        gcd_val = gcd(n1,n2)

        lcm_val = (a*b) / gcd_val

        return [gcd_val,lcm_val]
