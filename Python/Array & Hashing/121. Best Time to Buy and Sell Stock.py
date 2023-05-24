class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprice = 0
        l , r = 0 , 1
        
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            maxprice = max((prices[r]-prices[l]),maxprice)
            r += 1
        return maxprice

        ##0(n^2)
        
        maxprice = 0
        window = 1
        
        for x in range(len(prices)):
            for j in range(x+1,len(prices)):
                maxprice = max((prices[j]-prices[x]),maxprice)
        
        return maxprice