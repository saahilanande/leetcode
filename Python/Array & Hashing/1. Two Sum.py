class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

## Optimal solution

        compliMap= {} #store number as the key and index as the value
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in compliMap:
                return [i,compliMap[diff]]
            
            compliMap[nums[i]] = i

## Two pointers 
        left = 0
        right = len(nums)-1
        nums.sort()

        while left < right:

            if nums[right] - nums[left] == target:
                return [left,right]

            if nums[right] - nums[left] > target:
                left = left + 1
            
            if nums[right] - nums[left] < target:
                right = right - 1

## O^2

    def n2(self, nums,target):
        for item in range(len(nums)):
            for item2 in range(item+1,len(nums)):
                if nums[item] + nums[item2] == 9:
                    arrg=[]
                    arrg.append(item)
                    arrg.append(item2)
                    return arrg