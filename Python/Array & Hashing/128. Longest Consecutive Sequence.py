class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        
        maxLength = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n-1) not in numSet:
                lenght = 1
                nex = n+1
                while (nex) in numSet:
                    nex += 1
                    lenght +=1
                maxLength = max(maxLength,lenght)
        return maxLength