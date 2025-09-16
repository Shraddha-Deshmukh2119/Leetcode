class Solution:
    def sortedString(self,s):
        s=list(s)
        s.sort()
        return "".join(s)
   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}

        for s in strs:
            key=self.sortedString(s)
            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key]=[s] 
        return list(dict1.values())           
                   