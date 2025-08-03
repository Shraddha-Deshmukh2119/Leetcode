class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        i=0
        j=1
        ans=1
        if n == 0:
            return 0

        set1=set()
        set1.add(s[0])

        while j<n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
            set1.add(s[j])
            j+=1
            ans=max(ans,j-i)
        return ans    