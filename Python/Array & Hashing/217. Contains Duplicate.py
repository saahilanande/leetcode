class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
#o(n^2)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] == nums[j]:
                    return True
        return False
                    
#O(nlogn)    
    
        nums.sort()
        
        for x in range(1,len(nums)):
            if nums[x]==nums[x-1]:
                return True
        else:
            return False
#O(N)

        return len(set(nums)) < len(nums)