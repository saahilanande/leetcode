class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = max(piles)

        while l<=r:

            eatingRate = (l + r)//2

            hours = 0

            for i in piles:

                hours += math.ceil(i/eatingRate) //Calculating total hours we get given the eating rate

            if hours  > h:
                l = eatingRate + 1
            else:
                res = min(res,eatingRate)
                r = eatingRate - 1
        return res