class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=len(s)
        if n==0:
            return 0
        set1=set()    
        
        ans=0
        i=0
        j=0

        while j<n:
            while s[j] in set1:
                set1.remove(s[i])
                i+=1
            set1.add(s[j])
            ans=max(ans,j-i+1)
            j+=1
        return ans        
