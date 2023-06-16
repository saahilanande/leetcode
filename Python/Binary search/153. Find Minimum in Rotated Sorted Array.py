class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1

        res = max(nums)

        while l<r:
            mid = (l+r)//2
            res = min(res,nums[mid])

            if nums[mid] > nums[r]: ##If the mid is in right sorted array
                l = mid + 1
            else:                   ##if the mid is in left sorted array
                r = mid - 1
        return min(res,nums[l])