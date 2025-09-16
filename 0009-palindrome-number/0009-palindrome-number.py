class Solution:
    def isPalindrome(self, x: int) -> bool:
       temp=x
       rev=0
       while temp>0:
        ld=temp%10
        temp//=10
        rev=(rev*10+ld)
       return rev==x            