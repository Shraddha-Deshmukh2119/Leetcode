class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        rot=k%n
        for i in range(0,k):
            e=nums.pop()
            nums.insert(0,e)
    
        