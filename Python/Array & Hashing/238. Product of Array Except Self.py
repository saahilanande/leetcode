class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums) #Initialize a list with base value 1

        prefix = 1
        for i in range(len(nums)): #firstPass to get all the preFix value
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1): #secondPass to multiple all the postfix value
            result[i] *= postfix
            postfix *= nums[i]
            
        return result