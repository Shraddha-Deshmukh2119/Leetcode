class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        n=0
        while num>0:
            n=n*10
            n=n+(num%10)
            num=num//10
        if x==n:
            return True
        else:
            return False    
        