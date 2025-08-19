class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        ans=1

        while l<=r:
            mid=(l+r)//2
            midsquared=mid*mid
            if midsquared >x:
                r=mid-1
            else:
                ans=mid
                l=mid+1
        return ans            