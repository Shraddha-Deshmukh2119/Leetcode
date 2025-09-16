class Solution:
    def maxProfit(self, nums: List[int]) -> int:
     n=len(nums)
     if n==0:
        return 0
     profit=0
     min_price=nums[0]

     for i in range(1,n):
        curr_profit=nums[i]-min_price
        profit=max(profit,curr_profit)
        min_price=min(min_price,nums[i])
     return profit               